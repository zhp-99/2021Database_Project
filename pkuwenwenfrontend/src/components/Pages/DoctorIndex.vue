<template>
<div>
  <div id = 'logoimg'>
  <img alt="Vue logo" src="../../assets/logo2.jpeg" height="106" width="256">
  </div>
  <div id = 'text'>
  <p> {{OfficeName}} </p>
  </div>
  <div class="">
    <el-table :data="DoctorList" style="width: 50%">
      <el-table-column fixed prop="course_name" label="医师名" width="250">
        <template #default="scope">
          <span class="message-title" @click="openDoctor(scope.row.userName)">{{scope.row.realName}}</span>
        </template>
      </el-table-column>
    </el-table>
  </div>
</div>
</template>

<script>
export default {
  name: 'tabs',
  data() {
    return {
      OfficeName: this.$route.params.office,
      message: 'first',
      showHeader: false,
      DoctorList: Array(),
    }
  },

  mounted(){
    var post_request = new FormData()
    post_request.append('officeName', this.$route.params.office)
    this.$http
    .request({
      url: this.$url + '/office/info',
      method: 'post',
      data: post_request,
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    .then((response) =>{
      //console.log('get return data')
      console.log(response)
      this.DoctorList = response.data.DoctorList
    })
  },

  methods: {
    openDoctor (userName) {
       console.log(`dash: scan ${userName}`);
       this.$router.push({
         path: '/' + this.$route.params.office + '/' + userName + '/ReservationCalendar',
       })
    }
  },
}

</script>

<style>
.message-title{
  cursor: pointer;
}
.handle-row{
  margin-top: 30px;
}
</style>

