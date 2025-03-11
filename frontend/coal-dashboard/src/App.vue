<template>
  <div>
    <nav>
      <router-link to="/signup">Signup</router-link>
      <router-link to="/login">Login</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
import API from "./api/api.js";

export default {
  data() {
    return {
      message: "Loading...",
    };
  },
  async created() {
    try {
      const response = await API.get("/");
      this.message = response.data.message;
    } catch (error) {
      this.message = "Failed to connect to backend.";
    }
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
