<template>
  <div id = 'logoimg'>
    <img alt="Vue logo" src="../../assets/logo2.jpeg" height="106" width="256">
  </div>
  <div id = 'text'>
    <p> Appointment Detail {{AppointmentID}} </p>
  </div>
</template>

<script>
export default {
  name: 'AppointmentDetail',
  data() {
    return {
      AppointmentID: this.$route.params.id,
    }
  },
  mounted(){
    var post_request = new FormData()
    post_request.append('id', this.$route.params.id)
  },

  methods: {
    addReply(){
      var post_request = new FormData()
      post_request.append('reply_content', this.replyContent)
      post_request.append('replyer', localStorage.getItem('ms_username'))
      post_request.append('qid', this.$route.params.id)
      this.$http
          .request({
            url: this.$url + '/addReply',
            method: 'post',
            data: post_request,
            headers: {'Content-Type': 'multipart/form-data'},
          })
          .then((response) => {
            console.log(response)
            if(response.data.retCode === 0){
              alert('回复成功！')
              location.reload() // 刷新页面
            }else{
              alert('error!回复失败！')
            }
          })
          .catch((response) => {
            console.log(response)
          })
    },
  },
}

</script>

<style>
.header{
  background-color: #f6f7f8;
  color: rgb(202, 187, 187);
  text-align: left;
  line-height: 60px;
}

.aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.main {
  background-color: #E9EEF3;
  color: #333;
  text-align: left;
  line-height: 160px;
}

.Question {
  margin-bottom: 40px;
}

.Answer {
  margin-top: auto;
}
.lower-part{
  margin-top: 30px;
}
.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}

.form-box{
  width: 700px;
}

.title{
  text-align: left;
}
</style>

