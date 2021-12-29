<template>
<div>
  <div id = 'logoimg'>
    <img alt="Vue logo" src="../../assets/logo2.jpeg" height="391" width="626">
  </div>
  <div align="center">
    <el-button type="danger" @click="openFever()">发热患者通道</el-button>
    <el-button type="primary" @click="openUsual()">其他患者通道</el-button>
  </div>
</div>
</template>

<script>
export default {
  name: "FeverOrNot",
  data: function() {
    return {
      message: 'first',
      showHeader: false,
    }
  },

  methods: {
    openFever() {
      console.log(`dash: fever patient enter`);
      localStorage.setItem("patient_type", 'fever');
      this.$router.push('/PatientHomepage');
    },
    openUsual () {
      console.log(`dash: usual patient enter`);
      localStorage.setItem("patient_type", 'usual');
      this.$router.push('/PatientHomepage');
    },
  },
}
</script>

<style scoped>

</style>
