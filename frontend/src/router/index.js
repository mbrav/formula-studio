import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Dashboard",
    component: () =>
      import("../views/DashboardView.vue"),
  },
  {
    path: "/classes",
    name: "Classes",
    component: () =>
      import("../views/ClassesView.vue"),
  },
  {
    path: "/class-details",
    name: "Class Detail",
    component: () =>
      import("../views/ClassDetailView.vue"),
  },
  {
    path: "/Categories",
    name: "Categories",
    component: () =>
      import("../views/CategoriesView.vue"),
  },
  {
    path: "/Users",
    name: "Users",
    component: () =>
      import("../views/UsersView.vue"),
  },
  {
    path: "/profile",
    name: "User Profile",
    component: () =>
      import("../views/UserProfileView.vue"),
  },
  {
    path: "/settings",
    name: "Settings",
    component: () =>
      import("../views/SettingsView.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import("../views/LoginView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
