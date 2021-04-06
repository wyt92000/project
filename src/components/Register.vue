<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    注册
                </h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            用户名:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="username" v-model="name" @blur="checkName()"/>
                            <span id="name_msg" style="color: #CE090E"></span>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            真实姓名:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="name" v-model="real_name" @blur="check_RealName()"/>
                            <span id="rename_msg" style="color: #CE090E"></span>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            密码:
                        </td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" name="pwd" v-model="password" @blur="checkPwd()"/>
                            <span id="pwd_msg" style="color: #CE090E"></span>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            确认密码:
                        </td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" name="re_pwd" v-model="re_pwd" @blur="checkRePwd()"/>
                            <span id="repwd_msg" style="color: #CE090E"></span>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            性别:
                        </td>
                        <td valign="middle" align="left">
                            男
                            <input @click="gender=0" type="radio" class="inputgri" name="sex" value="man"
                                   checked="checked"/>
                            女
                            <input @click="gender=1" type="radio" class="inputgri" name="sex" value="woman" />
                        </td>
                    </tr>

                </table>
                <p>
                    <input type="button" class="button" value="注册" @click="user_register"/>
                    <router-link to="/login">登录</router-link>
                    <br> <span id="button_msg" style="color: #CE090E"></span>
                </p>
            </div>
        </div>
        <div id="footer">
            <div id="footer_bg">
                ABC@126.com
            </div>
        </div>
    </div>
</template>

<script>
    export default {
      name: "Register",
      data() {
        return {
          name: "",
          real_name: "",
          password: "",
          re_pwd: "",
          gender: 0,
        }
      },
      methods: {

        // 前端验证用户名
        checkName() {
          // 设置标识为false，通过验证后改为true
          let flag = false;
          // 获取用户输入的用户名
          let user_name = this.name;
          // 对用户输入的用户名格式进行判断  正则判断
          let pattern = /^[a-zA-Z0-9_-]{4,16}$/;
          // 获取提示标签
          let span = document.getElementById("name_msg")
          // 用户名不能为空
          if (user_name == null | user_name == "") {
            span.innerHTML = "<span style=\" color: red\">用户名不能为空</span>";
            // 正则校验用户名格式
          } else if (pattern.test(user_name) == false) {
            span.innerHTML = "<span style=\" color: red\">用户名格式错误</span>";
          } else {   // 代表校验通过
            span.innerHTML = "<span style=\" color: green\">用户名可以使用</span>";
            flag = true;
          }
          return flag;

        },

        // 前端验证真实姓名
        check_RealName() {
          // 设置标识为false，通过验证后改为true
          let flag = false;
          // 获取用户输入的真实姓名
          let user_real_name = this.real_name
          // 获取提示标签
          let span = document.getElementById("rename_msg")
          // 真实姓名不能为空
          if (user_real_name == null | user_real_name == "") {
            span.innerHTML = "<span style=\" color: red\">姓名不能为空</span>";
          } else {
            span.innerHTML = "<span style=\" color: green\"></span>";
            // 校验通过
            flag = true;
          }
          return flag;

        },

        // 前端验证密码
        checkPwd() {
          // 设置标识为false，通过验证后改为true
          let flag = false;
          // 获取用户输入的密码
          let user_pwd = this.password
          // 对用户输入的密码强度进行判断  正则判断
          let pattern = /^[a-zA-Z][a-zA-Z0-9\_\.\@\!\#\$\%\^\&\*\(\)]{5,16}/;
          // 获取提示标签
          let span = document.getElementById("pwd_msg")
          // 密码不能为空
          if (user_pwd == null | user_pwd == "") {
            span.innerHTML = "<span style=\" color: red\">密码不能为空</span>";
            // 正则校验密码强度
          } else if (pattern.test(user_pwd) == false) {
            span.innerHTML = "<span style=\" color: red\">密码强度太低</span>";
          } else {   // 代表校验通过
            span.innerHTML = "<span style=\" color: green\">密码可以使用</span>";
            flag = true;
          }
          return flag;

        },

        // 前端验证重复密码
        checkRePwd() {
          // 设置标识为false，通过验证后改为true
          let flag = false;
          // 获取用户输入的重复密码
          let user_pwd = this.password
          let user_repwd = this.re_pwd
          // 获取提示标签
          let span = document.getElementById("repwd_msg")
          // 重复密码不能为空
          if (user_repwd == null | user_repwd == "") {
            span.innerHTML = "<span style=\" color: red\">重复密码不能为空</span>";
          } else if (user_repwd != user_pwd) {
            span.innerHTML = "<span style=\" color: red\">重复密码输入错误</span>";
          } else {   // 代表校验通过
            span.innerHTML = "<span style=\" color: green\">输入正确</span>";
            flag = true;
          }
          return flag;
        },

        // 向后端发送注册请求
        user_register() {
          let flag1 = this.$options.methods.checkName();
          console.log(flag1);
          // let flag2 = this.$options.methods.check_RealName();
          // let flag3 = this.$options.methods.checkPwd();
          // let flag4 = this.$options.methods.checkRePwd();

          // if (flag1 ===true && flag2 === true && flag3 === true && flag4 === true) {
          if (flag1) {
            this.$axios({
              url: "http://127.0.0.1:8000/user/users/",
              method: "post",
              data: {
                name: this.name,
                real_name: this.real_name,
                password: this.password,
                re_pwd: this.re_pwd,
                gender: this.gender,
              }
            }).then(res => {
              console.log(res.data);
              this.$message({
                message: "恭喜您注册成功",
                type: "success",
                duration: 1000,
                showClose: true
              })

              // 如果注册成功，自动跳转到登录页
              this.$router.push("/login");

            }).catch(error => {
              console.log(error);
              this.$message.error("您提交的信息有误，请修改后提交~");
            })
          } else {
                let span = document.getElementById("button_msg");
                span.innerHTML = "<span style=\" color: red\">请检查表单</span>";
          }
        },

      }
    }
</script>

<style scoped>

</style>
