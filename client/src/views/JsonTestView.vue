<template>
  <div>
    <div>{{jsoninstance}}</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return {
      jsoninstance: ''
    }
  },
  created() {
    const djangoMovie = 'http://127.0.0.1:8000/api/m1/movies/'
    axios({
        methods: 'get',
        url: djangoMovie,
    })
    .then((response) => {
      console.log('asdsadad')
      console.log(response.data[0].title)
      this.jsoninstance = response.data[0]
    })
  }
}
  
</script>

<style>

</style>