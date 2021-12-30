<template>
  <div id = 'logoimg'>
    <img alt="Vue logo" src="../../assets/logo2.jpeg" height="106" width="256">
  </div>
  <div id = 'text'>
    <p> Appointment Detail {{AppointmentID}} </p>
  </div>

  <el-row :gutter="20">
    <el-col :span="6">
      患者用户名：{{pName}}
    </el-col>
    <el-col :span="6">
      患者真实姓名：{{pRealName}}
    </el-col>

  </el-row>

  <el-row :gutter="20">
    <el-col :span="6">
      <el-table :data="AppointmentList" style="width: 80%">
        <el-table-column
            fixed
            prop="'appointment_list"
            label="该患者的历史预约"
            width="250">
          <template #default="scope">
            <span class="message-title" @click="openAppointment(scope.row.id)">
              {{scope.row.dRealName}} {{scope.row.pRealName}} {{scope.row.date}}
            </span>
          </template>
        </el-table-column>
      </el-table>
    </el-col>
    
    <el-col :span="6">
      <el-container class="开药">
        <div class="form-box">
          <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="药方">
              <el-input type="textarea" :rows="10" 
                placeholder="开药处方"
                v-model="PrescriptionContent"></el-input>
            </el-form-item>
            <!-- <el-form-item>
              <el-button type="primary" @click="addPrescription">开药</el-button>
            </el-form-item> -->
          </el-form>
        </div>
      </el-container>
    </el-col>

    <el-col :span="6">
      <el-container class="WenZhenJielun">
        <div class="form-box">
          <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="问诊结论">
              <el-input type="textarea" :rows="10" 
                placeholder="请务必先开药再保存病历"
                v-model="MedicalRecordContent"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="addMedicalRecord">保存病历并开药</el-button>
            </el-form-item>
          </el-form>
        </div>
      </el-container>
    </el-col>

  </el-row>
  
</template>

<script>
export default {
  name: 'AppointmentDetail',
  data() {
    return {
      AppointmentID: this.$route.params.id,
      pName: '',
      pRealName: '',
      AppointmentList: Array(),
      PrescriptionContent: '',
      MedicalRecordContent: '',
    }
  },
  mounted(){
    var post_request = new FormData()
    post_request.append('id', this.$route.params.id)
    this.$http.request({
      url: this.$url+'/appointment/detail/info',
      method: 'post',
      data: post_request,
      headers: {'Content-Type': 'multipart/form-data'},
    })
    .then((response) => {
      this.pName = response.data.pName
      this.pRealName = response.data.pRealName
      this.AppointmentList = response.data.AppointmentList
    })
  },

  methods: {
    addMedicalRecord(){ // 保存病历和处方
      var post_request = new FormData()
      post_request.append('Pcontent', this.PrescriptionContent)
      post_request.append('Mcontent', this.MedicalRecordContent)
      post_request.append('id', this.$route.params.id)  // Appointment ID
      this.$http
          .request({
            url: this.$url + '/doctor/addMedicalRecord',
            method: 'post',
            data: post_request,
            headers: {'Content-Type': 'multipart/form-data'},
          })
          .then((response) => {
            console.log(response)
            if(response.data.retCode === 0){
              alert('添加成功')
              location.reload() // 刷新页面
            }else{
              alert('error!添加失败')
            }
          })
          .catch((response) => {
            console.log(response)
          })
    },
    addReply(){
      var post_request = new FormData()
      post_request.append('reply_content', this.PrescriptionContent)
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

.higher-part{
  margin-bottom: 30px;

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

