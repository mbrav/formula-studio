<template>

  <navbar-comp />

  <!-- VIEWS CONTROLED BY ROUTER -->
  <main role="main">
    <div class="container-fluid mx-0 px-0">
      <router-view />
    </div>
  </main>

  <footer-comp />

</template>

<script>
export default {};
</script>

<style lang="scss">
footer {
  bottom: 0;
  width: 100%;
}
</style>
