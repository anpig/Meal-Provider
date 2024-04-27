<template>
  <div class="login">
    <div class="overlap-wrapper">
      <div class="overlap">
        <div class="overlap-group">
          <div class="group">
            <div class="div">
              <div class="frame">
                <div class="frame-2">
                  <div class="text-wrapper">Staff ID</div>
                  <div class="div-wrapper">
                    <div class="text-wrapper-2">ex. 000001</div>
                  </div>
                </div>
                <div class="frame-3">
                  <div class="frame-2">
                    <div class="text-wrapper">Password</div>
                    <div class="div-wrapper">
                      <div class="text-wrapper-3">ex. password123</div>
                    </div>
                  </div>
                  <div class="frame-4">
                    <div class="text-wrapper-4">Login</div>
                  </div>
                </div>
              </div>
              <div class="text-wrapper-5">Forget Password</div>
            </div>
          </div>
        </div>
        <div class="frame-5">
          <img
            class="taiwan-semiconductor"
            alt="Taiwan semiconductor"
            src="@/assets/taiwan-semiconductor-manufacturing-company-logo-svg.svg"
          />
          <p class="welcome-to-TSMC-meal">
            Welcome to TSMC <br />
            Meal Provider
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserLogin",
};
</script>

<style>
.login {
  background-color: #ffffff;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}

.login .overlap-wrapper {
  background-color: #ffffff;
  height: 903px;
  width: 1440px;
}

.login .overlap {
  background-image: url('@/assets/unsplash_-YHSwy6uqvk.png');
  background-position: 50% 50%;
  background-size: cover;
  height: 903px;
  position: relative;
}

.login .overlap-group {
  background-color: #000000d4;
  height: 903px;
  left: 720px;
  position: absolute;
  top: 0;
  width: 720px;
}

.login .group {
  height: 551px;
  left: 150px;
  position: relative;
  top: 178px;
  width: 422px;
}

.login .div {
  border-radius: 60px;
  height: 551px;
  position: relative;
  width: 420px;
}

.login .frame {
  align-items: flex-start;
  background-color: #ffffff;
  border: 5px solid;
  border-color: #a5a2a2;
  border-radius: 60px;
  display: inline-flex;
  flex-direction: column;
  gap: 60px;
  left: 0;
  padding: 60px 60px 80px;
  position: absolute;
  top: 0;
}

.login .frame-2 {
  align-items: flex-start;
  display: inline-flex;
  flex: 0 0 auto;
  flex-direction: column;
  gap: 15px;
  position: relative;
}

.login .text-wrapper {
  color: #000000;
  font-family: "Inter-Medium", Helvetica;
  font-size: 30px;
  font-weight: 500;
  letter-spacing: 0;
  line-height: normal;
  margin-top: -1px;
  position: relative;
  white-space: nowrap;
  width: fit-content;
}

.login .div-wrapper {
  align-items: center;
  background-color: #ffffff;
  border: 3px solid;
  border-color: #cccccc;
  border-radius: 120px;
  display: flex;
  flex: 0 0 auto;
  gap: 10px;
  justify-content: center;
  padding: 15px 100px;
  position: relative;
  width: 300px;
}

.login .text-wrapper-2 {
  color: #a5a2a2;
  font-family: "Inter-Regular", Helvetica;
  font-size: 20px;
  font-weight: 400;
  letter-spacing: 0;
  line-height: normal;
  margin-left: -3px;
  margin-right: -3px;
  margin-top: -3px;
  position: relative;
  white-space: nowrap;
  width: fit-content;
}

.login .frame-3 {
  align-items: flex-start;
  display: inline-flex;
  flex: 0 0 auto;
  flex-direction: column;
  gap: 75px;
  position: relative;
}

.login .text-wrapper-3 {
  color: #a5a2a2;
  font-family: "Inter-Regular", Helvetica;
  font-size: 20px;
  font-weight: 400;
  letter-spacing: 0;
  line-height: normal;
  margin-left: -30px;
  margin-right: -30px;
  margin-top: -3px;
  position: relative;
  white-space: nowrap;
  width: fit-content;
}

.login .frame-4 {
  align-items: center;
  background-color: #6a9451;
  border-radius: 120px;
  display: flex;
  flex: 0 0 auto;
  gap: 10px;
  justify-content: center;
  padding: 15px 100px;
  position: relative;
  width: 300px;
}

.login .text-wrapper-4 {
  color: #000000;
  font-family: "Inter-Regular", Helvetica;
  font-size: 30px;
  font-weight: 400;
  letter-spacing: 0;
  line-height: normal;
  margin-top: -1px;
  position: relative;
  white-space: nowrap;
  width: fit-content;
}

.login .text-wrapper-5 {
  color: var(--collection-1-black);
  font-family: "Inter-Regular", Helvetica;
  font-size: 15px;
  font-weight: 400;
  left: 150px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  text-decoration: underline;
  top: 489px;
  white-space: nowrap;
}

.login .frame-5 {
  align-items: center;
  display: inline-flex;
  flex-direction: column;
  gap: 35px;
  left: 177px;
  position: absolute;
  top: 254px;
}

.login .taiwan-semiconductor {
  height: 263px;
  position: relative;
  width: 324px;
}

.login .welcome-to-TSMC-meal {
  color: var(--collection-1-black);
  font-family: "Inter-SemiBold", Helvetica;
  font-size: 40px;
  font-weight: 600;
  letter-spacing: 0;
  line-height: normal;
  position: relative;
  text-align: center;
  width: fit-content;
}
</style>
