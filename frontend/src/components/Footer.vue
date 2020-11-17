<template lang="html">
  <!-- FOOTER -->
  <footer id="main-footer" class="footer bg-dark text-white mt-5 p-5">
    <div class="container">
      <div class="row">
        <div class="col">
          <p class="lead text-center">
            Copyright &copy;
            <span id="year" />
            Formula Studio {{ msg }}
          </p>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  props: {
    msg: String
  }
};
</script>

<style lang="css" scoped></style>
