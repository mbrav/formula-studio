<template lang="html">
  <!-- FOOTER -->
  <footer id="main-footer" class="footer bg-dark text-white mt-4 py-4">
    <div class="container">
      <div class="row">
        <div class="col">
          <p class="lead text-center m-0">
            Copyright &copy;
            <span id="year"> {{ YearNow() }} </span>
            Formula Studio
          </p>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
var moment = require("moment");
export default {
  name: "Footer",
  methods: {
    YearNow() {
      return moment().format("YYYY");
    },
  },
};
</script>

<style lang="scss" scoped></style>
