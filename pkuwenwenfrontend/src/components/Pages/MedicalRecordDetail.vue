<template>
  <div id = 'logoimg'>
    <img alt="Vue logo" src="../../assets/logo2.jpeg" height="106" width="256">
  </div>
  <div id = 'text'>
    <p> Medical Record Detail {{MedicalRecordID}} </p>
  </div>

  <el-row :gutter="20">
    <el-col :span="12">
      <el-table :data="prescription" style="width: 80%">
        <el-table-column
            fixed
            prop="prescription"
            label="处方详情"
            width="500">
          <template #default="scope">
            <span class="message-title">
              {{scope.row.id}}  {{scope.row.pName}} {{scope.row.dName}} {{scope.row.date}} {{scope.row.medical}}
            </span>
          </template>
        </el-table-column>
      </el-table>
    </el-col>
  </el-row>

</template>

<script>
export default {
  name: "MedicalRecord",
  data() {
    return {
      MedicalRecordID: this.$route.params.id,
      prescription: Array(), //虽然是个Array但是一般来说只有一项
    }
  },
  mounted(){
    var post_request = new FormData()
    post_request.append('id', this.$route.params.id)
    this.$http
        .request({
          url: this.$url + '/medical/record/detail/info',
          method: 'post',
          data: post_request,
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then((response) =>{
          //console.log('get return data')
          console.log(response)
          this.prescription = response.data.prescription
        })
    // var post_request = new FormData()
    // post_request.append('id', this.$route.params.id)
  },
}
</script>

<style scoped>

</style>
