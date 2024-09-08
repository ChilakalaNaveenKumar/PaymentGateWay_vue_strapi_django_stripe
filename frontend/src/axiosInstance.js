import axios from 'axios';

// Create an Axios instance
const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000', // Django backend base URL
  withCredentials: true, // By default, send cookies for authenticated requests
});

// Helper function to get the JWT token from cookies or localStorage
function getJwtToken() {
  // Retrieve token from cookies (or localStorage if preferred)
  const token = document.cookie.split('; ').find(row => {
    console.log(row)
    return row.startsWith('jwt_token')
  })?.split('=')[1];
  return token || null;
}

// Add a request interceptor
axiosInstance.interceptors.request.use(
  config => {
    // Only include credentials (cookies) for specific paths
    const nonAuthPaths = ['/auth/login/', '/auth/register/', '/auth/forgot-password/'];
    if (!nonAuthPaths.includes(config.url)) {
      const token = getJwtToken();  // Get the token
      if (token) {
        // Attach the token to the Authorization header
        config.headers['Authorization'] = `Bearer ${token}`;
      }
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

axiosInstance.interceptors.response.use(
  response => response, // Return response if it's successful
  error => {
    if (error.response.status === 401) {
      // Redirect to login page if the user is not authenticated
      // window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
