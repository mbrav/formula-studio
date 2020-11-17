import { createRouter, createWebHistory } from "vue-router";
// import DashboardView from "../views/DashboardView.vue";

const routes = [
  // {
  //   path: "/home",
  //   name: "Home",
  //   component: About
  // },
  {
    path: "/",
    name: "Dashboard",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/DashboardView.vue")
  },
  {
    path: "/classes",
    name: "Classes",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/ClassesView.vue")
  },
  {
    path: "/class-details",
    name: "Class Detail",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/ClassDetailView.vue")
  },
  {
    path: "/Categories",
    name: "Categories",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/CategoriesView.vue")
  },
  {
    path: "/Users",
    name: "Users",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/UsersView.vue")
  },
  {
    path: "/profile",
    name: "User Profile",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/UserProfileView.vue")
  },
  {
    path: "/settings",
    name: "Settings",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/SettingsView.vue")
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/LoginView.vue")
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
