<template>
	<nav class="d-flex justify-content-around" style="position:sticky;top:0;height:auto;min-height:70px;max-height:20px;z-index:1;background:rgb(150,150,150);">
		<span>
			<router-link to="/main">Main</router-link> |
			<router-link to="/movies">Movie</router-link> |
			<router-link to="/random">Random</router-link> |
			<router-link to="/community">Community</router-link> |
			<router-link to="/weather">Today's Recommended Movie</router-link>
		</span>
    <span>
      <router-link class="mx-3" to="/login">login</router-link>
      <router-link class="mx-3" to="/signup">SignUp</router-link>
    </span>
	</nav>
</template>

<script>
export default {

}
</script>

<style>

</style>