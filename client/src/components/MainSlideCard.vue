<template>
  <div class="container my-5">
    <img class="w-100 h-100 card-img-top box1"
          style="border-radius: 5%; cursor: pointer;"
          :src="SlideURL"
          alt=""
          @mouseover="showText = true"
          @mouseout="showText = false"
          @click="goToDetail(slide.movie_id)"
          @dragstart="temp"
    >
    <div class="text-overlay w-100" v-if="showText">
      <p class="text w-100">{{slide.title}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainSlideCard',
  props: {
    slide: Object
  },
  data() {
    return {
      showText: false
    };
  },
  computed: {
    SlideURL() {
      return `https://image.tmdb.org/t/p/w300${this.slide.poster_path}`;
    }
  },
  methods:{
    goToDetail(id){
      if (this.dragging){
        this.dragging = false
      } else {
      this.$router.push(`/detail/${id}`)
      }
    },
    temp() {
      this.dragging = true
    }
  }
};
</script>

<style scoped>
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
  color: rgb(0, 0, 0);
  font-size: large;
  margin: 0;
  text-shadow: -1px 0px rgb(0, 0, 0), 0px 1px rgb(0, 0, 0), 1px 0px rgb(0, 0, 0), 0pxrgb(0, 0, 0)yellow;
  font-weight: bold;  
}

.box1 {
  border-radius: 10px;
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.9);
}
</style>