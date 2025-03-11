import { createRouter, createWebHistory } from "vue-router";
import SignupPage from "../components/SignupPage.vue";
import LoginPage from "../components/LoginPage.vue";
import DashboardPage from "../components/DashboardPage.vue";

const routes = [
  { path: "/signup", component: SignupPage },
  { path: "/login", component: LoginPage },
  { path: "/dashboard", component: DashboardPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
