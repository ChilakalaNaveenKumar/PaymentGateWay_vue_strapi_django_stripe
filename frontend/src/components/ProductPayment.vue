<template>
    <div>
      <h2>Payment for {{ name }}</h2>
      <form @submit.prevent="handlePayment">
        <div id="card-element"></div>
        <button type="submit">Pay Now</button>
      </form>
    </div>
  </template>
  
  <script>
  import { loadStripe } from '@stripe/stripe-js';
  import axiosInstance from '@/axiosInstance';
  
  export default {
    data() {
      return {
        stripe: null,
        elements: null,
        product: null,
      };
    },
    computed: {
      name() {
        if (this.product !== null) {
          console.log(this.product.name)
        }
        return this.product !== null ? this.product.name : ''
      }
    },
    async created() {
      this.stripe = await loadStripe('your_stripe_secret_key');
      this.elements = this.stripe.elements();
      const cardElement = this.elements.create('card');
      cardElement.mount('#card-element');
      console.log(cardElement)
  
      const productId = this.$route.params.id;
      const response = await axiosInstance.get(`http://localhost:8000/api/products/${productId}`);
      this.product = response.data;
    },
    methods: {
      async handlePayment() {
        const response = await axiosInstance.get('http://localhost:8000/auth/stripe-payment/', {
          amount: this.product.price * 100, // Stripe uses cents
        });
  
        const { clientSecret } = response.data;
        const { error } = await this.stripe.confirmCardPayment(clientSecret, {
          payment_method: {
            card: this.elements.getElement('card'),
          },
        });
  
        if (error) {
          alert('Payment failed');
        } else {
          alert('Payment successful!');
        }
      },
    },
  };
  </script>
  