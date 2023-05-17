<template>
  <div>
    <NavigationBar/>    
    <h1 class="fw-bold">보고싶은 영화</h1>
    <CommunityListForm/>
    <CommunityListItem/>
  </div>
</template>

<script>
import CommunityListForm from '@/components/CommunityListForm.vue'
import CommunityListItem from '@/components/CommunityListItem.vue'
import NavigationBar from '@/components/NavigationBar.vue'


export default {
  name: 'CommunityView',
  components: {
    CommunityListForm, 
    CommunityListItem,
    NavigationBar,
  }
}
</script>

<style>

</style>