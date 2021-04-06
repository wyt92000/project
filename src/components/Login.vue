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
                <h1>login</h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            username:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" v-model="name" @blur="check_Name()"/>
                            <span id="name_msg" style="color: #CE090E"></span>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            password:
                        </td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" v-model="password" @blur="check_Pwd()"/>
                            <span id="pwd_msg" style="color: #CE090E"></span>
                        </td>
                    </tr>
                </table>
                <p>
                    <input type="submit" class="button" value="登录" @click="user_login"/>
                    &nbsp;&nbsp;
                    <router-link to="/register">注册</router-link>
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
        name: "Login",
        data() {
            return {
                name: "",
                password: "",
            }
        },
        methods: {

            // 前端验证用户名
            check_Name(){
              // 设置标识为false，通过验证后改为true
              let flag = false;
              // 获取用户输入的用户名
              let user_name = this.name
              // 获取提示标签
              let span = document.getElementById("name_msg")
              // 用户名不能为空
              if (user_name == null | user_name == "") {
                  span.innerHTML = "<span style=\" color: red\">用户名不能为空</span>";
              } else {
                 span.innerHTML = "<span style=\" color: green\"></span>";
                  // 校验通过
                  flag = true;
              }
              return flag;

            },

            // 前端验证密码
            check_Pwd(){
              // 设置标识为false，通过验证后改为true
              let flag = false;
              // 获取用户输入的密码
              let user_pwd = this.password
              // 获取提示标签
              let span = document.getElementById("pwd_msg")
              // 密码不能为空
              if (user_pwd == null | user_pwd == "") {
                  span.innerHTML = "<span style=\" color: red\">密码不能为空</span>";
              } else {
                 span.innerHTML = "<span style=\" color: green\"></span>";
                  // 校验通过
                  flag = true;
              }
              return flag;

            },

            // 发送登录请求
            user_login() {
                this.$axios({
                    url: "http://127.0.0.1:8000/user/users/",
                    method: "get",
                    params: {
                        name: this.name,
                        password: this.password
                    }
                }).then(res => {
                    if (res.data.message) {
                      console.log(res.data);
                      this.$message.success("恭喜你，登录成功")
                        // 将用户的信息保存至 sessionStorage  用于展示用户信息
                        sessionStorage.id = res.data.results["id"];
                        sessionStorage.name = res.data.results["name"];
                        // 登录成功则跳转到首页
                        this.$router.push("/index")
                    } else {
                        this.$message.error("您的登录信息有误")
                    }
                }).catch(error => {
                    console.log(error);
                    this.$message.error("您的登录信息有误")
                })
            },
        }
    }
</script>

<style scoped>

</style>
