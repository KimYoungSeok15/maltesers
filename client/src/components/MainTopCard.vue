<template>
  <div class="container">
    <router-link :to="`detail/${top.movie_id || top.id}`">
      <img class="w-100 h-100 card-img-top"
           style="border-radius: 5%;"
           :src="TopURL"
           alt=""
           @mouseover="showText = true"
           @mouseout="showText = false"
      >
      <div class="text-overlay w-100" v-if="showText">
        <p class="text w-100">{{top.title}}</p>
      </div>
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
  opacity: 0.5;
}

.text-overlay {
  position: absolute;
  top: 90%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 10px;
  border-radius: 5px;
  pointer-events: none; /* 텍스트 영역에 마우스 이벤트를 비활성화 */
  --bs-bg-opacity: .2;
}

.text {
  color: #ffffff;
  font-size: large;
  margin: 0;
  text-shadow: -1px 0px rgb(0, 0, 0), 0px 1px rgb(0, 0, 0), 1px 0px rgb(0, 0, 0), 0pxrgb(0, 0, 0)yellow;
  font-weight: bold;  
}
</style>