<template>
	<div class="container">
		<div class="container-login">
			<div class="iconContainer">
                <font-awesome-icon color="#FFF" backgroundColor="#016795" size="4x" :icon="['fas', 'user-circle']" />
            </div>
			<div class="input-model">            
	            <input type="text" placeholder=" " class="input">
            	<label class="lbl-input">Email</label>
        	</div>
			<div class="input-model">            
	            <input type="password" placeholder=" " class="input">
            	<label class="lbl-input">Senha</label>
        	</div>
			<button>Entrar</button>
		</div>
	</div>
</template>

<script>
export default {

}
</script>

<style scoped>
	.container {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		height: 100%;
		background: rgb(27,36,49);
		background: linear-gradient(90deg, rgba(27,36,49,1) 0%, rgba(1,103,149,1) 100%);
	}
	.container-login {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		background-color: #fff;
		border-radius: 5px;
		width: 450px;
		height: 370px;
	}
	button {
		font-size: 14px;
		font-weight: bolder;
		margin-top: 50px;
		width: 300px;
		height: 35px;
		border: none;
		border-radius: 3px;
		color: #fff;
		background-color: rgba(1,103,149,1);
		cursor: pointer;
	}
</style>