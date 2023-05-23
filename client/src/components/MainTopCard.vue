<template>
  <div class="container">
    <router-link :to="`detail/${top.movie_id}`">
      <img class="w-100 h-100 card-img-top"
           style="border-radius: 5%;"
           :src="TopURL"
           alt=""
           :data-text="showText ? '마우스를 올려보세요' : ''"
           @mouseover="showText = true"
           @mouseout="showText = false"
      >
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'MainTopCard',
  props: {
    top: Object
  },
  data() {
    return {
      showText: false
    };
  },
  computed: {
    TopURL() {
      return `https://image.tmdb.org/t/p/w300${this.top.poster_path}`;
    }
  }
};
</script>

<style>
.container {
  position: relative; /* 상대적인 위치 설정 */
  display: inline-block; /* 인라인 요소로 표시 */
}

.card-img-top {
  transition: transform 0.3s ease; /* 변환 효과의 지속 시간과 가속도 설정 */
}

.card-img-top:hover {
  transform: scale(1.1); /* 마우스를 올렸을 때 이미지 크기 확대 */
}

.text-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  padding: 10px;
  border-radius: 5px;
}

.text {
  color: #000;
}
</style>