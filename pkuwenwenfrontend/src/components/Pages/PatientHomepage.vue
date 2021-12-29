<template xmlns:el-col="http://www.w3.org/1999/html">
<div>
  <div id = 'logoimg'>
  <img alt="Vue logo" src="../../assets/logo2.jpeg" height="106" width="256">
  </div>
  <div id = 'text'>
  <p> Patient Homepage </p>
  </div>
  <el-row>
    <el-col :span="12"><div class="grid-content bg-purple">真实姓名：{{realName}}</div></el-col>
    <el-col :span="12"><div class="grid-content bg-purple-light">患者ID：{{patientID}}</div></el-col>
  </el-row>
  <el-row>
    <el-col :span="6"><div class="grid-content bg-purple">用户名：{{userName}}</div></el-col>
    <el-col :span="6"><div class="grid-content bg-purple-light">{{gender}}</div></el-col>
    <el-col :span="12"><div class="grid-content bg-purple">身份证号：{{idCardNumber}}</div></el-col>
  </el-row>
  <el-row>
    <el-col :span="6"><div class="grid-content bg-purple-light">电话号码：{{phoneNumber}}</div></el-col>
    <el-col :span="6"><div class="grid-content bg-purple">邮箱：{{email}}</div></el-col>
    <el-col :span="6"><div class="grid-content bg-purple-light">出生日期：{{birthday}}</div></el-col>
    <el-col :span="6"><div class="grid-content bg-purple">当前预约数：{{appointmentNumber}}</div></el-col>
  </el-row>
  <el-row :gutter="20">
    <el-col :span="6">
      <el-table :data="OfficeList" style="width: 80%">
        <el-table-column
            fixed
            prop="office_name"
            label="我要挂号 全部科室/医生人数"
            width="250">
          <template #default="scope">
            <span class="message-title" @click="openOffice(scope.row.office_name)">
              {{scope.row.office_name}}  {{scope.row.doctor_num}}
            </span>
          </template>
        </el-table-column>
      </el-table>
    </el-col>
    <el-col :span="6">
      <el-table :data="AppointmentList" style="width: 80%">
        <el-table-column
          fixed
          prop="'appointment_list"
          label="我的所有预约"
          width="250">
          <template #default="scope">
            <span class="message-title" @click="openAppointment(scope.row.id)">
              {{scope.row.dRealName}} {{scope.row.pRealName}} {{scope.row.date}}
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
      OfficeList: Array(),
      AppointmentList: Array(),
      realName: '真实姓名',
      patientID: '患者编号',
      userName: '登录名',
      gender: '性别',
      idCardNumber: '身份证号',
      phoneNumber: '电话号码',
      email: '邮箱',
      birthday: '生日写这里咯',
      appointmentNumber: '预约数233',
    }
  },
  mounted(){
    var post_request = new FormData()
    post_request.append('userName', localStorage.getItem('ms_username'))
    this.$http
    .request({
      url: this.$url + '/patient/homepage/info',
      method: 'post',
      data: post_request,
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    .then((response) =>{
      //console.log('get return data')
      console.log(response)
      this.realName = response.data.realName
      this.patientID = response.data.patientID
      this.userName = response.data.userName
      this.gender = response.data.gender
      this.idCardNumber = response.data.idCardNumber
      this.phoneNumber = response.data.phoneNumber
      this.email = response.data.email
      this.birthday = response.data.birthday
      this.appointmentNumber = response.data.appointmentNumber
      this.OfficeList = response.data.OfficeList
      this.AppointmentList = response.data.AppointmentList
    })
  },

  methods: {
    openOffice (officename) {
     console.log(`dash: ${officename}`);
     this.$router.push({
       path: '/' + officename + '/DoctorIndex',
     })
    },
    openAppointment (id) {
      console.log(`dash: scan appointment id ${id}`);
      this.$router.push({
        path: '/' + id + '/AppointmentDetail',
      })
    },
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

