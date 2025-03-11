<template>
  <div>
    <h2>Login</h2>
    <input v-model="username" placeholder="Username" />
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="login">Login</button>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import API from "../api/api.js";
import { useRouter } from "vue-router";

export default {
  data() {
    return {
      username: "",
      password: "",
      message: "",
    };
  },
  setup() {
    const router = useRouter(); // Use Vue Router for navigation
    return { router };
  },
  methods: {
    async login() {
      try {
        const response = await API.post("/login", {
          username: this.username,
          password: this.password,
        });

        localStorage.setItem("token", response.data.token); // Store token
        this.message = "Login successful!";
        
        this.router.push("/dashboard"); // Redirect to Dashboard
      } catch (error) {
        this.message = error.response.data.error || "Login failed!";
      }
    },
  },
};
</script>
