<template>
  <div class="contatiner">
    <router-link :to="`detail/${top.movie_id}`"><img class="w-100; h-100; card-img-top" style="" :src=TopURL alt=""></router-link>
    <!-- <a href="http://localhost:8080/detail"><img :src=PlayingURL alt=""></a>
    <a href="http://localhost:8080/detail"><img :src=upcomingURL alt=""></a> -->
    <!-- <p>{{ movie.title }}</p> -->
    <!-- <p>{{ movie.overview }}</p> -->
    <!-- {{top}} -->
  </div>
</template>

<script>

export default {
  name: 'MainTopCard',
  data() {
    return {
      TopURL: `https://image.tmdb.org/t/p/w300${this.top.poster_path}`
    }
  },
  props: {
    top: Object
  }
}

</script>

<style>
.container {
  position: relative; /* 상대적인 위치 설정 */
  display: inline-block; /* 인라인 요소로 표시 */
  overflow: hidden; /* 내용이 넘칠 경우 숨김 처리 */
}

.card-img-top {
  transition: transform 0.3s ease; /* 변환 효과의 지속 시간과 가속도 설정 */
  z-index: 1;
}

.card-img-top:hover {
  transform: scale(1.1); /* 마우스를 올렸을 때 이미지 크기 확대 */
  z-index: 2; /* 다른 요소들보다 앞에 위치하여 hover 효과를 유지 */
}
</style>