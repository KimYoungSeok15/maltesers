<template>
  <div id="app" >
    <router-view/>
  </div>
</template>

<script>
export default {
  data() {
    return {
      entered: false,
    }
  },
}
</script>

<style>

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: rgb(31, 31, 31);
  background-color:rgb(219, 223, 234);
  font-family: line;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #ffffff;
}

nav a.router-link-exact-active {
  color: #42b983;
}

@font-face {
    font-family: 'line';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/LINESeedKR-Bd.woff2') format('woff2');
    font-weight: 600;
    font-style: normal;
}
@font-face {
    font-family: 'content';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/GangwonEdu_OTFBoldA.woff') format('woff');
    font-weight: 700;
    font-style: normal;
}
</style>
