<template xmlns:el-col="http://www.w3.org/1999/html">
<div>
  <div id = 'logoimg'>
  <img alt="Vue logo" src="../../assets/logo2.jpeg" height="106" width="256">
  </div>
  <div id = 'text'>
  <p> Doctor Homepage </p>
  </div>
  <el-row>
    <el-col :span="6"><div class="grid-content bg-purple">真实姓名：{{realName}}</div></el-col>
    <el-col :span="6"><div class="grid-content bg-purple-light">医生编号：{{doctorID}}</div></el-col>
    <el-col :span="6"><div class="grid-content bg-purple">出生日期：{{birthday}}</div></el-col>
    <el-col :span="6"><div class="grid-content bg-purple-light">性别：{{gender}}</div></el-col>
  </el-row>
  <el-row>
    <el-col :span="6"><div class="grid-content bg-purple">身份证：{{idCardNumber}}</div></el-col>
    <el-col :span="6"><div class="grid-content bg-purple-light">邮件：{{email}}</div></el-col>
    <el-col :span="12"><div class="grid-content bg-purple">电话：{{phoneNumber}}</div></el-col>
  </el-row>
  <el-row>
    <el-col :span="12"><div class="grid-content bg-purple">登录名：{{userName}}</div></el-col>
    <el-col :span="6"><div class="grid-content bg-purple-light">毕业院校：{{college}}</div></el-col>
    <el-col :span="6"><div class="grid-content bg-purple">学位：{{degree}}</div></el-col>
  </el-row>
  <!-- <el-row>
    <el-col :span="12"><div class="grid-content bg-purple">技术职称：{{FieldName}}</div></el-col>
    <el-col :span="12"><div class="grid-content bg-purple-light">专业特长：{{Specialty}}</div></el-col>
  </el-row> -->
  <el-row>
    <el-col :span="6"><div class="grid-content bg-purple">科室：{{office}}</div></el-col>
    <el-col :span="6"><div class="grid-content bg-purple-light">科长姓名：{{officeLeaderName}}</div></el-col>
    <el-col :span="12"><div class="grid-content bg-purple">科长联系电话：{{LeaderphoneNumber}}</div></el-col>
  </el-row>
  <el-row :gutter="20">

    <el-col :span="6">
      <el-table :data="TodayAppointmentList" style="width: 80%">
        <el-table-column
            fixed
            prop="office_name"
            label="今日预约患者: 编号: 姓名"
            width="250">
          <template #default="scope">
            <span class="message-title" @click="openAppointmentDetail(scope.row.id)">
              {{scope.row.id}}  {{scope.row.pRealName}}
            </span>
          </template>
        </el-table-column>
      </el-table>
    </el-col>

    <el-col :span="6">
      <el-table :data="HistoryPatientList" style="width: 80%">
        <el-table-column
          fixed
          prop="'appointment_list"
          label="历史治疗患者 病例编号；患者姓名"
          width="250">
          <template #default="scope">
            <span class="message-title" @click="openHistoryPatient(pName = scope.row.pName)">
              {{scope.row.pRealName}}
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
  data: function() {
    return {
      message: 'first',
      showHeader: false,
      TodayAppointmentList: Array(),
      HistoryPatientList: Array(),
      realName: '真实姓名',
      DoctorID: '医生编号',
      birthday: '生日',
      gender: '性别',
      idCardNumber: '身份证号',
      phoneNumber: '电话号码',
      email: '邮箱',
      userName: '登录名',
      college: '毕业院校',
      degree: '学位',
      FieldName: '技术职称',
      Specialty: '专业特长',
      office: '科室',
      officeLeaderName: '科长姓名',
      LeaderphoneNumber: '科长电话',
    }
  },
  mounted(){
    var post_request = new FormData()
    post_request.append('userName', localStorage.getItem('ms_username'))
    this.$http
    .request({
      url: this.$url + '/doctor/homepage/info',
      method: 'post',
      data: post_request,
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    .then((response) =>{
      //console.log('get return data')
      console.log(response)
      this.realName = response.data.realName
      this.doctorID = response.data.doctorID
      this.birthday = response.data.birthday
      this.gender = response.data.gender
      this.idCardNumber = response.data.idCardNumber
      this.phoneNumber = response.data.phoneNumber
      this.email = response.data.email
      this.userName = response.data.userName
      this.college = response.data.college
      this.degree = response.data.degree
      this.FieldName = response.data.FieldName
      this.Specialty = response.data.Specialty
      this.office = response.data.office
      this.officeLeaderName = response.data.officeLeaderName
      this.LeaderphoneNumber = response.data.LeaderphoneNumber
      this.TodayAppointmentList = response.data.AppointmentList
      this.HistoryPatientList = response.data.PatientList
    })
  },

  methods: {
    openAppointmentDetail (id) {
     console.log(`dash: ${id}`);
     this.$router.push({
       path: '/' + id + '/AppointmentDetail',
     })
    },
    openAppointment (id) {
      console.log(`dash: scan appointment id ${id}`);
      this.$router.push({
        path: '/' + id + '/AppointmentDetail',
      })
    },
    openHistoryPatient(pName = scope.row.pName, dName = localStorage.getItem('ms_username')){
      console.log(`dash: scan appointment id ${id}`);
      this.$router.push({
        path: '/' + id + '/HistoryDetail',
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
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
/*
#logoimg {
  text-align: left;
}
#text {
  text-align: right;
}
*/
</style>

