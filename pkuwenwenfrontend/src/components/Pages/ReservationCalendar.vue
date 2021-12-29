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
            <span class="message-title" @click="makeReservation(this.userName, scope.row.date)">
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
    /*
      form: {
        title: '默认标题',
        date1: '',
        date2: '',
        desc: '这里应该有高赞回复的内容\n而且这个输入框是可以随着内容数量的变化改变大小的\n这个部分应该从属于每一个Question各自的字段' +
            '，但是我只是搞了排版所以让他们在这里共享了\n实际上应该在上面的read和unread的每一项里面存相应的字段\n这个可以架子搭完再微调,' +
            '\n日后还可以上传图片，不过数据库那边不好办，一个比较简单的方法是在服务器上保存图片文件，然后把文件名存到数据库里，' +
            '每次查完数据库得到图片名，再用python文件操作打开文件，比较繁琐咱们先不做了吧',
      },
    */
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

    submitQuestion(){
      var post_request = new FormData()
      post_request.append('coursename', this.$route.params.course)
      post_request.append('publisher', localStorage.getItem('ms_username'))
      post_request.append('title', this.inputdata.title)
      post_request.append('content', this.inputdata.content)
      this.$http
          .request({
            url: this.$url + '/addQuestion',
            method: 'post',
            data: post_request,
            headers: {'Content-Type': 'multipart/form-data'},
          })
          .then((response) => {
            console.log(response)
            if(response.data.addQuestion.retCode === 0){
              alert('提交问题成功！')
              location.reload() // 刷新页面
            }else{
              alert('error!提交问题失败！')
            }
          })
          .catch((response) => {
              console.log(response)
          })
    }


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

