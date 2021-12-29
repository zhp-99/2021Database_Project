<template>
<div>
  <div id = 'logoimg'>
    <img alt="Vue logo" src="../../assets/logo2.jpeg" height="106" width="256">
  </div>
  <div id = 'text'>
    <p> {{office}} </p>
    <p> {{userName}} </p>
  </div>

  <el-row :gutter="20">
    <el-col :span="12">
      <el-table :data="CalendarList" style="width: 80%">
        <el-table-column
            fixed
            prop="reservation_date"
            label="日期/剩余号数"
            width="250">
          <template #default="scope">
            <span class="message-title" @click="makeReservation(scope.row.date)">
              {{scope.row.date}}  {{scope.row.reserve}}
            </span>
          </template>
        </el-table-column>
      </el-table>
    </el-col>
  </el-row>

</div>
</template>

<script>
export default {
  name: 'tabs',
  data() {
    return {
      office: this.$route.params.office,
      userName: this.$route.params.userName,
      inputdata: {
        title: '',
        content:'',
      },
      CalendarList: Array(),
    }
  },
  mounted(){
    var post_request = new FormData()
    // 注意这里的userName是医生的，不是当前正在进行操作的患者
    post_request.append('userName', this.$route.params.userName)
    this.$http
    .request({
      url: this.$url + '/reservation/calendar',
      method: 'post',
      data: post_request,
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    .then((response) =>{
      //console.log('get return data')
      console.log(response)
      this.CalendarList = response.data.CalendarList
    })
  },

  methods: {
    openQuestion (question_id) {
       console.log(`dash: ${question_id}`);
       this.$router.push({
         path: '/Question/' + question_id.toString(),
       })
    },

    makeReservation(date){
      var post_request = new FormData()
      post_request.append('pName', localStorage.getItem('ms_username'))
      post_request.append('dName', this.userName)
      post_request.append('date', date.toString())
      this.$http
          .request({
            url: this.$url + '/patient/makeAppointment',
            method: 'post',
            data: post_request,
            headers: {'Content-Type': 'multipart/form-data'},
          })
          .then((response) => {
            console.log(response)
            if(response.data.retCode === 1){
              alert('预约成功！')
              location.reload() // 刷新页面
            }else if(response.data.retCode === 2){
              alert('您已经挂过此号！')
            }else if(response.data.retCode === 3){
              alert('error!此日期已经无号！')
            }
          })
          .catch((response) => {
              console.log(response)
          })
    },
  }

}

</script>

<style>
.higher-part{
  margin-bottom: 30px;

}
.lower-part{
  margin-top: auto;
}
.message-title{
  cursor: pointer;
}
.handle-row{
  margin-top: 30px;
}

.form-box{
  width: 700px;
}

</style>

