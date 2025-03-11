<template>
  <div>
    <h2>Signup</h2>
    <input v-model="username" placeholder="Username" />
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="register">Register</button>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import API from "../api/api.js";

export default {
  data() {
    return {
      username: "",
      password: "",
      message: "",
    };
  },
methods: {
    async register() {
      try {
        const response = await API.post("/register", {
          username: this.username,
          password: this.password,
        });

        if (response && response.data) {
          this.message = response.data.message;
        } else {
          this.message = "Unexpected response from server.";
        }
      } catch (error) {
        console.error("Signup Error:", error);
        this.message =
          (error.response && error.response.data.error) ||
          "Registration failed!";
      }
    },
  },
};
</script>
