<template lang="html">
  <!-- HEADER -->
  <header id="main-header" class="py-2 bg-primary text-white">
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <h1><i class="fas fa-user" /> Login</h1>
        </div>
      </div>
    </div>
  </header>

  <!-- ACTIONS -->
  <section id="actions" class="py-4 mb-4 bg-light">
    <div class="container">
      <div class="row" />
    </div>
  </section>

  <!-- LOGIN -->
  <section id="login">
    <div class="container">
      <div class="row">
        <div class="col-md-6 mx-auto">
          <div class="card">
            <div class="card-header">
              <h4>Account Login</h4>
            </div>
            <div class="card-body">
              <form action="index.html">
                <div class="form-group">
                  <label for="email">Email</label>
                  <input type="text" class="form-control" />
                </div>
                <div class="form-group">
                  <label for="password">Password</label>
                  <input type="password" class="form-control" />
                </div>
                <input
                  type="submit"
                  value="Login"
                  class="btn btn-primary btn-block"
                />
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "LoginView",
  props: {
    msg: String
  }
};
</script>

<style lang="scss" scoped></style>
