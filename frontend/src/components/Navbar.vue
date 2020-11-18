<template lang="html">
  <!-- NAVBAR -->
  <nav class="navbar navbar-expand-md navbar-dark bg-dark p-0">
    <div class="container">
      <router-link to="/" class="navbar-brand">
        <img
          id="logo"
          class="d-inline-block align-top"
          src="../assets/logo.png"
          width="46"
          height="46"
          alt="Formula Studio logo"
          loading="lazy"
        />
      </router-link>
      <button
        class="navbar-toggler"
        data-toggle="collapse"
        data-target="#navbarCollapse"
      >
        <span class="navbar-toggler-icon" />
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav">
          <li class="nav-item px-2">
            <router-link to="/" class="nav-link">Dashboard</router-link>
          </li>
          <li class="nav-item px-2">
            <a href="/classes" class="nav-link">Classes</a>
          </li>
          <li class="nav-item px-2">
            <a href="/categories" class="nav-link">Categories</a>
          </li>
          <li class="nav-item px-2">
            <a href="/users" class="nav-link">Users</a>
          </li>
        </ul>

        <ul class="navbar-nav ml-auto">
          <li class="nav-item dropdown mr-3">
            <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown">
              <i class="fas fa-user" /> Welcome User
            </a>
            <div class="dropdown-menu">
              <router-link to="/profile" class="dropdown-item">
                <i class="fas fa-user-circle" /> Profile
              </router-link>
              <router-link to="/settings" class="dropdown-item">
                <i class="fas fa-cog" /> Settings
              </router-link>
              <a href="/settings" class="dropdown-item"> </a>
            </div>
          </li>
          <li class="nav-item">
            <a href="/login" class="nav-link">
              <i class="fas fa-user-times" /> Logout
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar"
};
</script>

<style lang="scss" scoped></style>
