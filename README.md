# Iskakbay Nurzhan
Django store project

# api:
* [**api/**](#api)
	* [**api/user/**](#apiuser) 

	* [**api/product/**](#apiproduct)
		* [**api/product/?search={query}**](#apiproductsearchquery)
	* [**api/category/**](#apicategory)
		* [**api/category/?search={query}**](#apicategorysearchquery)
	
	* [**api/cart/**](#apicart)
		* [**api/cart/?search={query}**](#apicartsearchquery)
	* [**api/cart/add/**](#apicartadd)
	* [**api/cart/delete/{pk}/**](#apicartdeletepk)
	* [**api/cart/add_one/{pk}/**](#apicartadd_onepk)
	* [**api/cart/reduce_one/{pk}/**](#apicartreduce_onepk)


* [**auth/**](#auth)
	* [**auth/register/**](#authregister)
	* [**auth/login/**](#authlogin)

	* [**auth/change_password/{pk}/**](#authchange_passwordpk)
	* [**auth/update_profile/{pk}/**](#authupdate_profilepk)
	* [**auth/upload_image/**](#authchange_image)

	* [**auth/forgot_password/{pk}/**](#authdelete_profilepk)
	* [**auth/confirm/**](#authdelete_profilepk)
	* [**auth/reset_password/{pk}/**](#authdelete_profilepk)

	* [**auth/logout/**](#authlogout)

___	
## api/
### api/product/
**Allowed Methods** : GET {public}

#### api/product/?search={query}
**Allowed Methods** : GET {public}


### api/category/
**allowed methods** : GET {public}

#### api/category/?search={query}
**Allowed Methods** : GET {public}


### api/user/
**allowed methods** : GET {admin}


### api/cart/
**allowed methods** : GET {authorized users}

#### api/cart/?search={query}
**Allowed Methods** : GET {authorized users}


### api/cart/add/
**allowed methods** : POST {authorized users}
<br>**fields :** 'required': {'quantity', 'product_id'}

### api/cart/delete/{pk}/
**allowed methods** : DELETE {authorized users}

### api/cart/add_one/{pk}/
**allowed methods** : GET {authorized users}

### api/cart/reduce_one/{pk}/
**allowed methods** : GET {authorized users}


## auth/
### auth/login/
**allowed methods** : POST {public}
<br>**fields :** 'required': {'username', 'password'}

### auth/register/
**allowed methods** : POST {public}
<br>**fields :** 'required': {'username', 'password1', 'password2', 'email', 'first_name', 'last_name'}

### auth/change_password/{pk}/
**allowed methods** : PUT {authorized users}
<br>**fields :** 'required': {'old_password', 'password1', 'password2'}

### auth/update_profile/{pk}/
**allowed methods** : PUT {authorized users}
<br>**fields :** 'optional': {'username', 'first_name', 'last_name', 'email'}

### auth/logout/
**allowed methods** : POST {authorized users}
<br>**fields :** 'required': {'refresh_token'}

### auth/change_image/{pk}/
**allowed methods** : PUT {authorized users}
<br>**fields :** 'required': {'image'}

### auth/delete_profile/{pk}/
**allowed methods** : DELETE {authorized users}
<br>**fields :** 'required': {'password'}