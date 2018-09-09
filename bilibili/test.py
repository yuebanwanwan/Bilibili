#coding:utf-8
from lxml import etree


text2 = '''
<!DOCTYPE html>
<html lang="zh-Hans">
<head>
<meta charset="utf-8">
<title>小林家的龙女仆 _ 全部短评</title>
<meta name="description"
	content="在单身的辛苦OL小林身边突然出现的女仆装束的美少女托尔。
长着角和尾巴的她的身姿正是所谓的龙娘。
在醉酒的小林邀请下说要到家里去的托尔，鬼使神差地开始以小林家女仆的身份工作……！？
“女仆”+“龙”=">
<meta name="keywords" content="小林家的龙女仆,小林,女仆,龙,女仆龙,妹抖,妹抖龙,龙女仆">
<meta name="author" content="哔哩哔哩番剧">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta property="og:title" content="小林家的龙女仆">
<meta property="og:url"
	content="//www.bilibili.com/bangumi/media/md5800/">
<meta property="og:image"
	content="http://i0.hdslb.com/bfs/bangumi/320a6c9893a874e7db755ecb7316a0d0abccec49.jpg">
<meta name="spm_prefix" content="666.19">
<link rel="dns-prefetch" href="//s1.hdslb.com">
<link rel="dns-prefetch" href="//s2.hdslb.com">
<link rel="dns-prefetch" href="//s3.hdslb.com">
<link rel="dns-prefetch" href="//i0.hdslb.com">
<link rel="dns-prefetch" href="//i1.hdslb.com">
<link rel="dns-prefetch" href="//i2.hdslb.com">
<link rel="dns-prefetch" href="//static.hdslb.com">
<link rel="shortcut icon" href="//static.hdslb.com/images/favicon.ico">
<link rel="search" type="application/opensearchdescription+xml"
	href="//static.hdslb.com/opensearch.xml" title="哔哩哔哩">
<script type="text/javascript" src="//static.hdslb.com/js/jquery.min.js"></script>
<script type="text/javascript"
	src="//static.hdslb.com/vip/dist/js/vipPlugin.v2.js"></script>
<script type="text/javascript"
	src="//static.hdslb.com/js/promise.auto.min.js"></script>
<script type="text/javascript"
	src="//s1.hdslb.com/bfs/seed/jinkela/header/header.js"></script>
<link rel="stylesheet"
	href="//s1.hdslb.com/bfs/static/review/media/css/review-media.0.9e4277a5b0e7c1f34cf60b1599cf8adac23d7798.css">
<style type="text/css">
.bili-footer input, .bili-footer button {
	outline: none;
	resize: none;
}

.bili-footer ul, .bili-footer li {
	margin: 0;
	padding: 0;
	list-style-type: none;
}

.bili-footer img {
	border: none;
	vertical-align: middle;
}

.bili-footer a {
	outline: none;
	text-decoration: none;
	cursor: pointer;
	white-space: nowrap;
}

.bili-footer a:focus {
	-moz-outline-style: none;
}

.bili-footer a img {
	border: none;
}

.bili-footer p, .bili-footer span {
	margin: 0;
	padding: 0;
}

.bili-footer .clearfix:after {
	content: "";
	display: block;
	visibility: hidden;
	height: 0;
	clear: both;
	font-size: 0;
}

.bili-footer .clearfix {
	zoom: 1;
}

.bili-footer {
	width: 100%;
	padding-top: 20px;
	color: #99a2aa;
	text-align: center;
	font-size: 12px;
}

.bili-footer .footer-wrp {
	background-color: #f6f9fa;
	padding-top: 40px;
	padding-bottom: 60px
}

.bili-footer a {
	color: #222
}

.bili-footer a:hover {
	color: #00a1d6
}

.bili-footer .icons-footer.icons-footer-report {
	display: inline-block;
	*display: inline;
	*zoom: 1;
	vertical-align: middle;
	width: 16px;
	height: 16px;
	margin-right: 3px;
	background: url(//static.hdslb.com/images/base/icons.png) no-repeat;
	background-position: -1367px -89px
}

.bili-footer .partner .left, .bili-footer .partner .right {
	line-height: 24px;
	*line-height: 24px
}

.bili-footer .partner .left a, .bili-footer .partner .right a {
	color: #99a2aa
}

.bili-footer .partner .left a:hover, .bili-footer .partner .right a:hover
	{
	color: #222
}

.bili-footer .right {
	float: right
}

.bili-footer .footer-cnt {
	width: 980px;
	margin: 0 auto
}

.bili-footer .boston-postcards {
	list-style: none;
	margin: 0 auto;
	float: left;
	margin-bottom: 30px
}

.bili-footer .boston-postcards li:first-child {
	border-left: 0;
	padding-left: 0 !important
}

.bili-footer .boston-postcards li:last-child {
	width: 280px;
	padding-right: 0
}

.bili-footer .boston-postcards li {
	float: left;
	text-align: left;
	list-style: none;
	width: 300px;
	height: 112px;
	padding-right: 25px;
	padding-left: 24px;
	line-height: 1;
	border-left: solid 1px #e5e9ef;
	font-size: 14px
}

.bili-footer .boston-postcards li .tips {
	margin-bottom: 22px
}

.bili-footer .boston-postcards li .cards {
	float: left;
	width: 100px;
	position: relative;
	margin-bottom: 16px
}

.bili-footer .boston-postcards li .cards.taobao {
	position: relative;
	width: 100px;
	height: 40px;
	margin-bottom: -23px
}

.bili-footer .boston-postcards li .cards.longer {
	width: 100px
}

.bili-footer .boston-postcards li .cards.wide {
	margin-right: 20px
}

.bili-footer .partner {
	padding: 0;
	text-align: left;
	margin: 0 auto;
	height: 80px
}

.bili-footer .partner .left {
	float: left;
}

.bili-footer .partner .partner-banner {
	background:
		url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABxCAMAAAAdzFY0AAAA9lBMVEUAAAD7+/tAQENFRkb///8AAAABW6H39/fCADr09PW7vLxkZGXBwcHl5eVijLiwsLDO2uXt7e0TEhP4///g4ODw8PHGxsfU1NTc3Ny2tbbr6uqhudPNzc2Jp8ikpKUTY6VfX2CsrKyysrOJiYsAT5pJfbCUlJTY19dpamq1Ome+y96Pjo8xMDElb6ucm5w8PDyuwtigoKAkJCSoqKhPUFArKyxvbm+MjI3KycrG0eF0dHVKSkvT3+rp7PHh5+50mcB4eHnQ0NCEhIV8fHxaWls3NzeXl5iBgIFdXV5WV1fd4+yuKlbAWX3ixtTPlazz5ezFcJC9AC/NNtTYAAAAAXRSTlMAQObYZgAADmhJREFUaN5slL2uwyAMRi/LV7FY3CETQl7wgmSJNVJI9r7/A11+Sm7b5KhSW0N8sJ3kx9zjyH0GJNRA1uMttIZsLuSwtyXxZlAFj8unIhip5v8NyDM68Uw9Y2cGidvJDoRTcItHhG/ZpyJAFuPA5WMT9YwxRuZTgCqwjGUKbgtIjMzs/wuw3HwESZ289m4MAbLz4Ln1wN5WNAz22wo2jdkkVMPEA9asiKzoeLOHIC3NStjMBhoDUGWoJkHsgN2lgkrSGNoX+LCmszPQJwC4TjGbiIJFcuuJmwIigEhYNtcQVMEFr/AvEXT8OgDYA7o0z8A+dwXtz+VdsJQErIVjXudAfr7PvwmipsHBkZX6SABXLzNA+S3ltxdWgFbhFAxajZZoVS1T8EnmKCHiRcitW0+OBFiXHwbghh8zBms5BWcvlWwJOGYFXyMoFGp/J9Y882KsSHr1BvCNNB6VinwKAoCIZJj3oPauAlPsntYTN861u1PwqFjb7wFANObjTeCYBRQlIxipHoL9qmAMmTHg883wLzATgYJSKAw7BbsgEFbvWKwJNcYwd3cRyA8C6CJIndYMbcvWgs0UbBBLcI8DUAW4AJd3URf4x8DdCAZ1V8weNHJPgV2ffSQhKh0+RgfcV5DN4I+wKtaBEISh54JhIS5Ml8alLCYmriSoO///QYeW5+HZ5Bq1pKU8XgnPrAAIt7LYYk8AZ94CMORLi7Ypr76jRRjcCAhAoJ2OxykAwu0Su2jG7UiHLswJALBowpNBX+rmUE0BuB/WMBo60yMZtjeAqegSk8qAaROb+AJgPr04ALAbinwczXfMvEuLuAIk5tFt2hnEPeJOLBhlknLa10ZVlmhjkpkpJS93JlmIQsqr+j+w3n77BfO+uh6pNo3Ys65l8H+2FgEf+eJFSGWAVFMiCXgsq24DHqOXskVf/W+nrO0+VJCxigUhDEWxehgSgqDJRGRAG7sHg820Nvv/n7SZhWXfpgiEa87BpM/gN/0c/+W/AswPFareRMUxlh3lJfr0alVmikGboKKGCmSUYmKzYTxfNYHUWioPMWYKIU+VZxu8uj6CkR/QIcwGuaBdCJAq4mDE7Q9nby2Rb59rtWgnXw6iNdWRUhBOQGz5hMF2TscdsaeQRASl4yMwB6fj1g4ODpM3EL2SGkyd2RfRjXp07mtxyZcLFkTq28ksISK3JpXeeC+4ZtiQ4oZA6LRmP4KBc8a6Z0cb8wVdzt1SiHIxS7zXffPWnFnAoxLhfb4vLjTKuFQk7DfD6ERLbPRxZK5IATFKZ96IfyeawoCggZouPZ6Ptbo5FpiEMAoxj+trtQK9n2MQsYqRSh6dwdhnXDePGtMB4YgpIBwsLogl8vSWLHNflsM24mk15G/2qR3FghiGjavBwSYE8hsTApMm3cCQJu1r3v2PtGKvsSswGCwkIbAPVAeRTJKx6XRrr+8VdTxv/74l9p17kczmEQwG7xZxF8r3ua6GfAuO4g5U3S93tSJUcn8VRrJYio5Ke2UIT5q34ynZ7/vTUFUezX/i49xwrxD3kspSvbl5kGh2JwKjEpPupx0WoyomJGLWeDJyK9aA3mpNRIaDRbbAliqnUHFitTQNqAqWkdaTlYIyGyVIsfLvM1jh4x9/AD+0kEEKwEAIA2Xm/39u0Tawt70YF8xKSERB7HdPuacluyiWUejmiSy3AxgCOuMZ0Bjjv7/g/0d79Gjbrav4EPNkDAtNSoQCsT61ZqPCLh62qWW3bRgIlus5UOKhNdhDgAYGAV7q6uKDIAENigZt0MBw6qb//zPdh5ZlkIxJU3xoR7OzjPHyoA8uUbv9b+yNuqXCZXWBXYo2N1mn8ciIhstlbt/VXul0t/A9vf48vCszD4wtcvhGMYToaaEu8a/CuHkvqdtpJfCMlKgQiuchXJmge9OEOpfL60Y7pIM3J2iKIkNFDCHwQ1PO7c0i8fkrh/y4EnD3I9HwFBBEhix7O3/Bz/8FvOQ8W8C7vJCbkwDq/PKb3N0Njx8GfXDt3zMUWRbOn7bZPe/dB0CPzHjPmzfIh/PpNJ4yXIqWaafgLxfSgN/mtX3OCRiBNempcYSgPujWVGudpoq8BGCmOw2zjHLItRuB0jE0/wHPm9W6PqeUFnxMgs/EfwWYkoyF6BaEXwQUdQLfvGCR3TIm6MpQwu6B61EJjlZDHAtIBkrdbCYCdgABSZMJHMDQwZiMQJOlzQxAiAbdKTlnIBsov5wB2nSlECCNpMFy0pssnYMGAOGqVy5aHawVuKnruta10qPMDmsVfBU9eOSOQ8IPIuQdBMSD+aomd9fEKhQhPGmOtos5A5PY+QHEqNhPjJorUSmFCQqQCMkTtnMFmyHvjEtFxP2fTUM0BYqA2ySAEmwO/GO3jFUbiGEwnIu11DeVLh0yBAqBkKVDCOWObIFOR+n7v0xlyd9JR18hySW2ZUu/9Vs6+VsuGrJ4sG8AfhxiI4ncTkW/LI35tkRdUADPzEmkatu1Dn1zo1y0kSo3m3AP3mzrCcAKDsdBog2CC8bQrEZea/s0YgcFsMFBlKIiOlKr70UBilNUOGTKRapoCUCWnge3x772sFGtT7XJ4NLcmGU0TopT9PjQUHCAuLakYvd7VmIWwQWXK0C1lZyBBfjYAIwaOWmjbV/gHgz5XeQAeHDGBfXA5Hggzj4eKEXHYtzLrPA9ikoHENPd5oG2DuAIrR64tE5OYTUNudq+xpM15ba/m51J+19r9tbWEkX09I9y82MI5/ziDyK3RTKXAUpFNLyLurbaBqIBvJgc+FxWrCF7GFHzmCP4d101GCKWBldfH5TwAHN5kLJ2zQMuO3M3za2iyp3tR7HPVvDFbfND0td7Hph9NXq8zvnidEo0QDd04guYAAV26VLyYFu+AQkRZwYCy+KKFSGA39SDdEA8LAUGw4zB2BrMsFiDopiik33HEl+IQ+/f9SjYaADMBzNQ6tLA2Yhgk7UJtqTZHX12ymzwCBRE0WWjOSGxElKjiC++gMTmsLgJdfzJqmkR++L6jjRHIk/eAWwwSs7kHAjJ7vn50yigHDDSGNDcAvR5NDgNYyIQpgxhhOEDFilBCM3Cq6jOgioHlWDkkSTJB2BNcO2A4sy11VEYCMPVzrDEKsXg7YiIrZAKiqL1UvSLR2sv//8PbZKu2112YffLssM5ick082TeZNpCzSaUAy9tUIPvG3m/iGgRbkH5yfNrgu88JcD3VwQ8qQViSY1Ine9cGYXI7gMRnz85gPw0gtdWRC+NAyCsJvKaPeNe9krEAcF7o6DExdUXaJ0DInhvF4JazWHdum0YPnzqAPAZ2PoH/4XBEgArotlRIH1av3KBdAWsG3siytyMBvHxdkhiAi89AG7D8PjoRscCbzyMyTgP4QaE2QmNXIDHAi8TStALvEWFCTGQ4m0l4H0ARoU7+FGuMFu2T8smn0kdJc1to41J0s495et2WI0Jtz6EgCLVQVl3BnBA1CU6eQHekqv45J2c8qc07S95ao0BO3jtbpcM5Ual1yh6JOPUP3Zz/4ii6NpQ4jdItfXkXT11AsSjYrkeMMR6dRB9f4OIjw3PNcUdL7NnF3SpPXunNGfx7cbmzcLskN1Yzo3lNz6Ve3plgMoDflMCpqZqfYqaXgyDSGW7AoylqOwYVYiG4iAFZLoO15z0Hjhz9Ih2Sb1R9zFmWZM1DW+qLMvo4BQWPBDDNU5Oqxoy3Gs0K0CnWAC8HErWUDfEDOqmygVAOztP73ryE4Nc922cl3O+UQ+PiJimbfq+TxTTJ3n2UXgwI95WgENpBlvMHVo1YFXYfFk9NaVHDSlcKWWggNn283WZwVCJ08PhUU6RxQFRCwAu4Y2T8+YoATfEeA3jn/WApzQbrGRAMmz81aMfHTtANLSSiTtnHz6MciFdFsHIrOB5He4nAUiIVohbD0eaBXAWACH1/P32BVOnjBiBq3kABVbeCjDPs+5T/CT6xZYTAIYFWmiA5h5C7aIfmQCMDNUPIakSqMj2EuBQTGDV+onolviwM1TFgAarQ6d4hQq9EGn4beplvDflsykl0g9yTrin+FAcOcCjWMMXkAwYkZ8wbhWuDoFeVIRcLKusABUvPN8UZPgTIcYX0/hiETAtUE6KlEjUjwZJAKKcw0ZkYDdIa/WadLoiq4x5mMEgACni8tzuZq6D1Eu5Ij9o7ATAdePTsUy61N2HXhlp+fVDAHYAsGQMoxQ/OUBIJJa+jG5zxaI42ljBFRsbzqujSi7QIjVazIPXlYDyPPaOtuS6TzotvKtjFwpAzwGfRfMsmlS8Db0ANSJWDQobrAUjhVIerjFBo4i0oJKxDxE/O5wsihMHkKTvD2zo28Q9eX48Pu9jJ+vAsCzz5BBXNw3LzLOjACSI2PphJCLdExygQrvDyoRAzDinuyoIIUUtxJ5IAHj9XLNrfzneNbbzkrksx5ZX8oxVVjWF2ixqU/HaLC4CMCPiFsAV4RjDDAo8hVj5YIiZI0ArUgwqcfxXaGQGyilgpJ3y2xSQ4bJLpniXbLLJKuOcpYyl4j+PmatVJ4AOkQtyrni3kCNSssWPPVYGEKFbSCLkVnIsc7GABe+gAIn16ba9x+FdhzpIpvA8tZsBl2gcFrUoVLVQF7VvC8rDQCkUkFFqCwKkrn639ogGKKqY2wp3DvDAXulyyLDlgE8Gw3xOtjGzzMK9x+fDdN9cyprusM9TYSyn9VKVR0WBPUqjdSiKptybAOA+EhtgQWnZyPNUHPYJ3Lp6zwFfvFtv7et4jN1uaJN7183tBoBs6QyrHWjlyOIKsmoZdqkO62e4aKUnqTL1OZ6Nl+NHjzmlyinhKJYHBkv6tu3bDZ83dPL+jLq4r2dyci1b1utqK8dwPUNG/NHkyHQ5xBQusZKYwjjgj/ZlbX/v+fJ3302/rH/r89vxbn7vWR3/6cvvv7av5EG6VSdVr0sAAAAASUVORK5CYII=)
		no-repeat;
	width: 100px;
	height: 80px
}

.bili-footer .partner #cert img {
	width: 100px;
}

.bili-footer .block.right {
	position: relative;
	width: 100%
}

.bili-footer .block.right div {
	position: relative;
	width: 82px;
	height: 80px;
	float: left
}

.bili-footer .block.right em {
	position: absolute;
	width: 82px;
	line-height: 14px;
	float: left;
	bottom: 0;
	left: 0;
	text-align: center;
	font-weight: normal;
}

.bili-footer .block.right .pic {
	position: relative;
	margin-left: 11px;
	width: 60px;
	height: 60px
}

.bili-footer .block.right .phone .pic {
	background: url("//static.hdslb.com/images/base/icons.png") no-repeat
		-1024px -194px
}

.bili-footer .block.right .phone .pic:hover {
	background-position: -1090px -194px
}

.bili-footer .block.right .weibo .pic {
	background: url("//static.hdslb.com/images/base/icons.png") no-repeat
		-1024px -322px
}

.bili-footer .block.right .weibo .pic:hover {
	background-position: -1090px -322px
}

.bili-footer .block.right .weixin .pic {
	color: #222;
	background: url("//static.hdslb.com/images/base/icons.png") no-repeat
		-1024px -66px
}

.bili-footer .block.right .weixin .pic:hover {
	background-position: -1090px -66px
}

.bili-footer .block.right .qrcode-box-wrp {
	width: 130px;
	height: 130px;
	background: #fff;
	margin-top: -146px;
	right: -23px;
	position: absolute;
	visibility: hidden;
	opacity: 0;
	transition: .2s;
	z-index: 100000
}

.bili-footer .block.right .qrcode-box {
	width: 128px;
	height: 128px;
	border: 1px solid #e5e9ef
}

.bili-footer .block.right .qrcode-box.qrcode-app {
	background:
		url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGEAAABhCAIAAABJZFj0AAADKklEQVR4nO2c0W7DIAxFk6n//8vdQyU0mZpzbaimTfe8TMsIUO86gO3mfj6fl1ny9dsT+AM8Xj/u+2538VLi3MNQ6PhT1nK+JRBuyXoujYWMPq0jxjZiHuF3/RGe6X9mdoRqn/sLS/tzXdaRgm3ERF8bZH6BS89i0cm6ysbKeliMhVQ/12UdKdhGTOprVRpLD7pMw5U+gXXEHNOR8q8WtTY3wxs/ejK3jhjbiEl9rarexlkcfQp3WI0QQsMrrSPGNmKir7V3IspZ5HVFb5CNsnBSPNY0sI4Y24i5T+2+dqLU2XKGHS6C6Aexjpiyjhr/Otzm7N+YzaqxWZuvWEeMbcTcVU0O8EE7Owhuf94OPXeuPLOzvRjOf56edcTYRky6rlXl3ciL6IcVHAvnr3yQrE/riLGNmFhbo8eSM9HqTtceS1mt9mtrBtYRYxsx5dzRTsWYuNZgmY5eM7dokF33ea0D6wjrprLnaOO4r29/sklWs5VKCYp1xNhGTDyL4PZ/Bs8ioeWbScilxdmNWYxhMbTPIiexjRj2tcCOaPFGcfujHPdF91TSOdYRYxsxvIcMmmw4YwAXo52VUY8Q6EFE64hJ8yKxXf052oiWVmuxjkR1EeuIsY2YY3mR1RhywFQ/1qx7aExmcaN1xNhGjFoPuV/msug83Iux2sVYep3zeg6XzyIlbCOmX+ffSO/pR+0wRDVKPY/STv9f1pEC57Kx8DxcHzQqrDDAmt04/6ldDzljHTG2EcPfXc8etKGBsqmp5rLbRVyLoRspFuuIsY0YNd+P+h8sWlYdoXHu1+vB9GlbR4xtxMR49kAPV+vVKtXSgY+i74GtI8Y2Ys5/DxKT8Y0GehC6mgRTerCOmGPvh1RqObKxDmaosYcwqDIZ64ixjZhj74dUntnV7U/mU0dSknon1hFjGzHH3g+5UxCgd45DtGvJFl9PsI4Y24g59l6/mezcr6811UD4fAXzVNne8ifWEfNBHTVKUPYP2PthXz+zO9hGzLH3QzZ6aJQmihsoZVZibcFlHSnYRkyaF9FpR8jSOZ0o09n//sLAOmJsI+ZYXuQfYx0xthHzDclyLbJnpcixAAAAAElFTkSuQmCC)
		center center no-repeat
}

.bili-footer .block.right .qrcode-box.qrcode-weibo {
	background:
		url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkAQMAAABKLAcXAAAABlBMVEX///8AAABVwtN+AAABPklEQVQ4y5XTsW3DMBCF4WewYGOYCwjQGtfdShLSGiaNtIa1EjuuIYALyB0Lwi9SShdk8ndfeYc7tFLWi0WuLpGhKcH5As0LE0xHfMAmVp80d+WKmPAnTYgDLrYrnF2R9TpZmLaUdU6SH3MiP7XnKcAFe21V90rFPG4qHcnw9UQyXGjH0BTgA8quCLZlzQbEXG/g2FE+Ng/3KtqRAp5pdRv2PiQjg0Z+3yN74janZPiWwtARn2B1m8rY1jGRTQNutlQ0BbO8VU09Uda2pH4xEsdNoKPBv6hmeaqtn1JuN6RcXbQ5NAX4IFKnycaOLDApGU6FY1sC/4p2uM4sHe3NKa7+HgVoSlknLYNfkg5tHd8vclyk1k/9/nvh5lj68pH1PJeEriaLXE+0a0c4n4rmzSfk0JSyQuzgnkqgoX/0Awm1JF4V4zroAAAAAElFTkSuQmCC)
		center center no-repeat
}

.bili-footer .block.right .qrcode-box.qrcode-weixin {
	background: url(//s1.hdslb.com/bfs/static/base/img/wx.ed20cfb.gif)
		center center no-repeat
}

.bili-footer .block.right .qrcode-box .qrcode-box-arrow {
	width: 130px;
	height: 141px;
	background:
		url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAOCAMAAAAR8Wy4AAAAXVBMVEUAAADf39/d3d3e3t7e3t7d3d3d3d3d3d3d3d3d3d3d3d3g4ODd3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3////7+/vw8PDm5ub09PTz8/Pq6uri4uL4+Ph7FEonAAAAFnRSTlMA+nfy7dvEVTghGvzRvLech2daLgwGJIBjEgAAAF9JREFUCNddzUcSgCAABMEx5xzA+P9nWgoK2Lc5bC3zD7vbG9Fqt/BICzEbiw/tYlpWwFRub59hDjB4eiSOhIevR3uDFsu712hEywJxP6Z8ukM9GrWUMbY8DDIcSY9yAeUiCzzIjqapAAAAAElFTkSuQmCC)
		bottom center no-repeat
}

.bili-footer .block.right .phone:hover .qrcode-box-wrp, .bili-footer .block.right .weibo:hover .qrcode-box-wrp,
	.bili-footer .block.right .weixin:hover .qrcode-box-wrp {
	visibility: visible;
	opacity: 1
}

.bili-footer .block.right .bigvip-qrcode {
	width: 260px;
	height: 150px;
	margin-top: -166px
}

.bili-footer .block.right .bigvip-qrcode .qrcode-box {
	width: 258px;
	height: 148px
}

.bili-footer .block.right .bigvip-qrcode .qrcode-box .qrcode-box-arrow {
	margin-left: 128px;
	margin-top: 20px
}

@media screen and (min-width: 1400px) {
	.bili-footer .footer-cnt {
		width: 1160px
	}
	.bili-footer .boston-postcards li {
		padding-right: 40px;
		padding-left: 39px;
		width: 360px
	}
	.bili-footer .boston-postcards li:first-child {
		border-left: 0;
		padding-left: 0 !important
	}
	.bili-footer .boston-postcards li:last-child {
		width: 280px;
		padding-right: 0
	}
	.bili-footer .boston-postcards li .cards {
		width: 120px
	}
}
</style>
<style type="text/css">
.bili-header-m {
	font: 12px Helvetica Neue, Helvetica, Arial, Microsoft Yahei, Hiragino
		Sans GB, Heiti SC, WenQuanYi Micro Hei, sans-serif;
	position: relative;
	z-index: 10000;
	background: #fff
}

.bili-header-m, .bili-header-m article, .bili-header-m aside,
	.bili-header-m blockquote, .bili-header-m button, .bili-header-m code,
	.bili-header-m dd, .bili-header-m details, .bili-header-m dl,
	.bili-header-m dt, .bili-header-m fieldset, .bili-header-m figcaption,
	.bili-header-m figure, .bili-header-m footer, .bili-header-m form,
	.bili-header-m h1, .bili-header-m h2, .bili-header-m h3, .bili-header-m h4,
	.bili-header-m h5, .bili-header-m h6, .bili-header-m header,
	.bili-header-m hgroup, .bili-header-m hr, .bili-header-m input,
	.bili-header-m legend, .bili-header-m li, .bili-header-m menu,
	.bili-header-m nav, .bili-header-m ol, .bili-header-m p, .bili-header-m pre,
	.bili-header-m section, .bili-header-m td, .bili-header-m textarea,
	.bili-header-m th, .bili-header-m ul {
	margin: 0;
	padding: 0
}

.bili-header-m input, .bili-header-m select, .bili-header-m textarea {
	font-size: 100%
}

.bili-header-m table {
	border-collapse: collapse;
	border-spacing: 0
}

.bili-header-m th {
	text-align: inherit
}

.bili-header-m fieldset, .bili-header-m img {
	border: none;
	vertical-align: middle
}

.bili-header-m abbr, .bili-header-m acronym {
	border: none;
	font-variant: normal
}

.bili-header-m del {
	text-decoration: line-through
}

.bili-header-m address, .bili-header-m caption, .bili-header-m cite,
	.bili-header-m code, .bili-header-m dfn, .bili-header-m em,
	.bili-header-m th, .bili-header-m var {
	font-style: normal;
	font-weight: 400
}

.bili-header-m ol, .bili-header-m ul {
	list-style: none
}

.bili-header-m caption, .bili-header-m th {
	text-align: left
}

.bili-header-m h1, .bili-header-m h2, .bili-header-m h3, .bili-header-m h4,
	.bili-header-m h5, .bili-header-m h6 {
	font-size: 100%;
	font-weight: 400
}

.bili-header-m q:after, .bili-header-m q:before {
	content: ""
}

.bili-header-m sub, .bili-header-m sup {
	font-size: 75%;
	line-height: 0;
	position: relative;
	vertical-align: baseline
}

.bili-header-m sup {
	top: -.5em
}

.bili-header-m sub {
	bottom: -.25em
}

.bili-header-m a {
	transition: color 0s
}

.bili-header-m a, .bili-header-m a:hover, .bili-header-m ins {
	text-decoration: none
}

.bili-header-m :focus, .bili-header-m a:focus {
	outline: none
}

.bili-header-m .clearfix:after, .bili-header-m .clearfix:before {
	content: "";
	display: table
}

.bili-header-m .clearfix:after {
	clear: both;
	overflow: hidden
}

.bili-header-m .clearfix {
	zoom: 1
}

.bili-header-m .clear {
	clear: both;
	display: block;
	font-size: 0;
	height: 0;
	line-height: 0;
	overflow: hidden
}

.bili-header-m .hide {
	display: none
}

.bili-header-m .block {
	display: block
}

.bili-header-m .fl, .bili-header-m .fr {
	display: inline
}

.bili-header-m .fl {
	float: left
}

.bili-header-m .fr {
	float: right
}

.bili-header-m .bili-icon {
	display: inline-block;
	background-image: url(//static.hdslb.com/images/base/icons.png)
}

.bili-header-m .bili-wrapper {
	margin: 0 auto;
	width: 1160px
}

@media screen and (max-width:1400px) {
	.bili-header-m .bili-wrapper {
		width: 980px
	}
}

.bili-header-m .bili-wrapper .l-con {
	float: left;
	width: 900px
}

@media screen and (max-width:1400px) {
	.bili-header-m .bili-wrapper .l-con {
		width: 720px
	}
}

.bili-header-m .bili-wrapper .r-con {
	width: 260px;
	float: right
}

.bili-header-m .bi-btn {
	display: inline-block;
	background: #00a1d6;
	color: #fff;
	font-size: 14px;
	padding: 4px 18px;
	border-radius: 4px;
	transition: all .3s;
	user-select: none;
	border: 1px solid #00a1d6;
	text-align: center;
	cursor: pointer
}

.bili-header-m .bi-btn:hover {
	color: #fff;
	background: #00b5e5;
	border-color: #00b5e5
}

.bili-header-m .bi-btn:active {
	background: #01769c;
	border-color: #01769c
}

.bili-header-m .nav-menu {
	position: relative;
	z-index: 200;
	height: 42px;
	color: #222
}

.bili-header-m .nav-menu .blur-bg {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-position: center -10px;
	background-repeat: no-repeat;
	filter: blur(4px)
}

.bili-header-m .nav-menu .nav-mask {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: hsla(0, 0%, 100%, .4);
	box-shadow: 0 1px 2px rgba(0, 0, 0, .1)
}

.bili-header-m .nav-menu .nav-con .nav-item {
	float: left;
	text-align: center;
	line-height: 42px;
	height: 42px;
	position: relative;
	background-color: hsla(0, 0%, 100%, 0)
}

.bili-header-m .nav-menu .nav-con .nav-item .t {
	color: #222;
	height: 100%;
	display: block;
	padding: 0 8px
}

.bili-header-m .nav-menu .nav-con .nav-item .t .num {
	height: 12px;
	line-height: 12px;
	color: #fff;
	background-color: #f25d8e;
	border-radius: 10px;
	position: absolute;
	padding: 1px 2px;
	font-size: 12px;
	top: 1px;
	right: -4px;
	min-width: 16px;
	z-index: 30;
	text-align: center
}

.bili-header-m .nav-menu .nav-con .nav-item .t .dot {
	width: 6px;
	height: 6px;
	background-color: #f25d8e;
	border-radius: 50%;
	position: absolute;
	right: 5px;
	top: 8px
}

.bili-header-m .nav-menu .nav-con .nav-item .new {
	position: absolute;
	top: 6px;
	right: -6px;
	width: 22px;
	height: 9px;
	background-position: -851px -412px
}

.bili-header-m .nav-menu .nav-con .nav-item .bml-beijing {
	position: absolute;
	top: 2px;
	right: -4px;
	width: 24px;
	height: 12px;
	background:
		url(//s1.hdslb.com/bfs/seed/jinkela/header/images/beijing.png)
		no-repeat
}

.bili-header-m .nav-menu .nav-con .nav-item .red_point {
	height: 8px;
	width: 8px;
	border-radius: 100%;
	position: absolute;
	right: 6px;
	top: 7px;
	background-color: #f25d8e
}

.bili-header-m .nav-menu .nav-con .nav-item:hover {
	background-color: hsla(0, 0%, 100%, .3)
}

.bili-header-m .nav-menu .nav-con .nav-item.profile-info:hover {
	background: none
}

.bili-header-m .nav-menu .nav-con .nav-item.home {
	margin-left: -10px;
	padding-left: 12px
}

.bili-header-m .nav-menu .nav-con .nav-item.home a {
	padding-left: 20px
}

.bili-header-m .nav-menu .nav-con .nav-item.home i {
	position: absolute;
	width: 17px;
	height: 14px;
	left: 10px;
	top: 12px;
	background-position: -919px -88px
}

.bili-header-m .nav-menu .nav-con .nav-item.mobile {
	padding: 0 10px
}

.bili-header-m .nav-menu .nav-con .nav-item.mobile a {
	display: inline-block;
	padding: 0
}

.bili-header-m .nav-menu .nav-con .nav-item .i-frame {
	position: absolute;
	left: 0;
	top: 42px
}

.bili-header-m .nav-menu .nav-con .nav-item .bml-box {
	position: absolute;
	background: #fff;
	width: 375px;
	padding: 12px;
	border-bottom-left-radius: 4px;
	border-bottom-right-radius: 4px
}

.bili-header-m .nav-menu .nav-con .nav-item .bml-box .bml-link {
	display: block;
	position: relative
}

.bili-header-m .nav-menu .nav-con .nav-item .bml-box .bml-link img {
	width: 100%;
	height: 110px;
	border-radius: 4px
}

.bili-header-m .nav-menu .nav-con .nav-item .bml-box .bml-link span {
	position: absolute;
	color: #fff;
	left: 0;
	bottom: 0;
	width: 375px;
	line-height: 24px;
	padding-left: 10px;
	border-radius: 4px;
	text-align: left;
	box-sizing: border-box;
	background: linear-gradient(transparent, rgba(0, 0, 0, .6))
}

.bili-header-m .nav-menu .nav-con .nav-item .bml-box .bml-link:first-child
	{
	margin-bottom: 12px
}

.bili-header-m .nav-menu .nav-con .nav-item .app-orcode-box {
	position: absolute;
	background: red;
	left: -20px;
	top: 42px;
	width: 259px;
	height: 174px;
	background:
		url(//s1.hdslb.com/bfs/seed/jinkela/header/images/orcode-frame.png)
}

.bili-header-m .nav-menu .nav-con .nav-item .app-orcode-box:before {
	content: "";
	position: absolute;
	width: 97px;
	height: 97px;
	left: 82px;
	top: 30px;
	background:
		url(//s1.hdslb.com/bfs/seed/jinkela/header/images/app-orcode.png)
}

.bili-header-m .nav-menu.blur-black .nav-mask {
	background-color: rgba(0, 0, 0, .4)
}

.bili-header-m .nav-menu.blur-black .nav-con .nav-item .t {
	color: #fff
}

.bili-header-m .nav-menu.blur-black .nav-con .nav-item.home i {
	background-position: -855px -88px
}

.bili-header-m .nav-menu .up-load {
	position: relative;
	width: 58px;
	height: 42px;
	margin-left: 8px
}

.bili-header-m .nav-menu .up-load .u-link {
	display: block;
	width: 100%;
	height: 48px;
	line-height: 42px;
	text-align: center;
	font-size: 14px;
	color: #fff;
	background-color: #fb7299;
	border-radius: 0 0 6px 6px
}

.bili-header-m .nav-menu .up-load .upload-new-icon {
	position: absolute;
	width: 54px;
	height: 34px;
	top: 4px;
	right: -53px;
	background:
		url(//s1.hdslb.com/bfs/seed/jinkela/header/images/up-new-iocn.png)
		no-repeat;
	z-index: 20
}

.bili-header-m .nav-menu .up-load:hover .u-link {
	background-color: #ff85ad
}

.bili-header-m .nav-menu .up-load .up-nav {
	width: 360px;
	position: absolute;
	right: 0;
	top: 42px;
	background: #fff;
	border-radius: 0 0 4px 4px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, .16);
	overflow: hidden;
	z-index: 1
}

.bili-header-m .nav-menu .up-load .up-nav li {
	cursor: pointer;
	text-align: center;
	width: 72px;
	height: 64px;
	transition: .2s;
	float: left;
	position: relative;
	background: #fff
}

.bili-header-m .nav-menu .up-load .up-nav li a {
	color: #f25d8e;
	display: block;
	width: 100%;
	height: 100%
}

.bili-header-m .nav-menu .up-load .up-nav li a .rect {
	display: block;
	width: 20px;
	height: 20px;
	margin: 15px auto 2px;
	transition: .2s
}

.bili-header-m .nav-menu .up-load .up-nav li a .rect.i-art {
	background-position: -534px -919px
}

.bili-header-m .nav-menu .up-load .up-nav li a .rect.i-ap {
	background-position: -534px -983px
}

.bili-header-m .nav-menu .up-load .up-nav li a .rect.i-vp {
	background-position: -471px -919px
}

.bili-header-m .nav-menu .up-load .up-nav li a .rect.i-vm {
	background-position: -471px -982px
}

.bili-header-m .nav-menu .up-load .up-nav li a .rect.i-vc {
	background-position: -471px -1751px
}

.bili-header-m .nav-menu .up-load .up-nav li:hover {
	background: #e5e9ef
}

.bili-header-m .nav-menu .up-load .up-nav li:hover .rect {
	transform: translateY(-2px)
}

.bili-header-m .nav-menu .up-load .up-nav li .new {
	position: absolute;
	top: 6px;
	right: 0;
	width: 22px;
	height: 9px;
	background-position: -851px -412px
}

.bili-header-m .nav-menu .up-load .up-nav li .beta {
	position: absolute;
	top: 6px;
	right: 0;
	width: 22px;
	height: 9px;
	background-position: -854px -1307px
}

.bili-header-m .nav-menu .dd-bubble {
	position: absolute;
	z-index: 1
}

.bili-header-m .profile-info {
	width: 58px
}

.bili-header-m .profile-info .i-face {
	position: absolute;
	z-index: 20;
	width: 36px;
	height: 36px;
	left: 11px;
	top: 0;
	transition: .3s
}

.bili-header-m .profile-info .i-face .face {
	border: 0 solid #fff;
	width: 100%;
	height: 100%;
	border-radius: 50%
}

.bili-header-m .profile-info .i-face .legalize {
	background-image:
		url(//s1.hdslb.com/bfs/seed/jinkela/header/images/user-auth.png);
	width: 20px;
	height: 20px;
	position: absolute;
	bottom: 10px;
	right: 7px;
	visibility: hidden;
	transition-delay: 0s
}

.bili-header-m .profile-info .i-face .legalize.vip {
	background-position: -72px -52px
}

.bili-header-m .profile-info .i-face .legalize.p-ver {
	background-position: -38px -52px
}

.bili-header-m .profile-info .i-face .legalize.e-ver {
	background-position: -4px -52px
}

.bili-header-m .profile-info .i-face .pendant {
	position: absolute;
	width: 84px;
	height: 84px;
	left: -11px;
	bottom: -3px;
	visibility: hidden;
	transition-delay: 0s
}

.bili-header-m .profile-info.on .i-face {
	left: -4px;
	top: 15px;
	height: 64px;
	width: 64px
}

.bili-header-m .profile-info.on .i-face .face {
	border: 2px solid #fff
}

.bili-header-m .profile-info.on .i-face .legalize {
	bottom: -4px;
	right: -3px;
	transition-delay: .28s;
	visibility: visible
}

.bili-header-m .profile-info.on .scale-in .face {
	width: 48px;
	height: 48px
}

.bili-header-m .profile-info.on .scale-in .legalize {
	bottom: 10px;
	right: 7px;
	transition-delay: .28s;
	visibility: visible
}

.bili-header-m .profile-info.on .scale-in .pendant {
	transition-delay: .28s;
	visibility: visible
}

.bili-header-m .head-banner {
	position: relative;
	z-index: 199;
	height: 170px;
	margin-top: -42px;
	background: #eee;
	background-position: center -10px;
	background-repeat: no-repeat
}

.bili-header-m .head-banner .banner-link {
	position: absolute;
	left: 0;
	top: 0;
	height: 100%;
	width: 100%
}

.bili-header-m .head-banner .head-content {
	position: relative;
	height: 170px
}

.bili-header-m .head-banner .head-content .head-title {
	position: absolute;
	top: 114px;
	left: 255px;
	line-height: 20px;
	padding: 6px 10px;
	background-color: rgba(0, 0, 0, .68);
	color: #fff;
	border-radius: 4px;
	font-size: 14px;
	max-width: 350px;
	opacity: 0;
	transition: all .2s
}

.bili-header-m .head-banner .head-content .head-logo {
	position: absolute;
	width: 220px;
	height: 105px;
	left: 24px;
	top: 55px;
	background: transparent no-repeat 0;
	z-index: 10
}

.bili-header-m .head-banner:hover .head-content .head-title {
	opacity: 1
}

.bili-header-m .b-icon {
	display: inline-block;
	vertical-align: middle;
	width: 12px;
	height: 12px;
	background: url(//static.hdslb.com/images/base/icons.png) no-repeat
}

.bili-header-m .b-icon.b-icon-p-account, .bili-header-m .b-icon.b-icon-p-live,
	.bili-header-m .b-icon.b-icon-p-member, .bili-header-m .b-icon.b-icon-p-wallet
	{
	width: 16px;
	height: 16px
}

.bili-header-m .b-icon.b-icon-p-member {
	background-position: -472px -344px
}

.bili-header-m .b-icon.b-icon-p-account {
	background-position: -472px -407px
}

.bili-header-m .b-icon.b-icon-p-wallet {
	background-position: -472px -472px
}

.bili-header-m .b-icon.b-icon-p-live {
	background-position: -473px -855px
}

.bili-header-m .b-icon.b-icon-vp {
	background-position: -471px -919px
}

.bili-header-m .b-icon.b-icon-vm {
	background-position: -471px -982px
}

.bili-header-m .b-icon.b-icon-vc {
	background-position: -471px -1751px
}

.bili-header-m .b-icon.b-icon-arrow-r {
	background-position: -478px -218px;
	width: 6px;
	height: 12px;
	margin: -2px 0 0 5px
}

.bili-header-m .b-icon.b-icon-ap {
	background-position: -534px -983px
}

.bili-header-m .b-icon.b-icon-art {
	background-position: -534px -919px
}

.bili-header-m .b-icon.b-icon-app {
	background-position: -1371px -1175px;
	width: 16px;
	height: 21px
}

.bili-header-m .mini-wnd-nav {
	position: absolute;
	left: 0;
	top: 42px;
	background-color: #fff;
	width: 320px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, .16);
	border: 1px solid #e5e9ef;
	border-radius: 0 0 4px 4px;
	z-index: 200
}

.bili-header-m .mini-wnd-nav a {
	color: #222;
	transition: color .2s
}

.bili-header-m .mini-wnd-nav .list {
	padding-top: 10px
}

.bili-header-m .mini-wnd-nav .list.history li {
	clear: both;
	position: relative;
	padding-left: 38px
}

.bili-header-m .mini-wnd-nav .list.history li:before {
	left: 26px
}

.bili-header-m .mini-wnd-nav .list.history li.timeline {
	color: #99a2aa;
	overflow: visible;
	height: 0;
	padding: 0;
	margin: 10px 0;
	border-top: 1px solid #e5e9ef;
	position: relative
}

.bili-header-m .mini-wnd-nav .list.history li.timeline:before {
	display: none
}

.bili-header-m .mini-wnd-nav .list.history li.timeline .date {
	background-color: #fff;
	position: absolute;
	top: -6px;
	left: 0;
	z-index: 10;
	padding: 0 10px;
	height: 12px;
	line-height: 12px
}

.bili-header-m .mini-wnd-nav .list.history li.no-data {
	border: none;
	padding: 0
}

.bili-header-m .mini-wnd-nav .list.history li a {
	max-width: none;
	float: inherit
}

.bili-header-m .mini-wnd-nav .list li {
	height: 28px;
	line-height: 28px;
	text-align: left;
	font-size: 12px;
	overflow: hidden;
	white-space: nowrap;
	text-overflow: ellipsis;
	padding: 0 12px 0 22px;
	position: relative
}

.bili-header-m .mini-wnd-nav .list li:before {
	content: "";
	display: block;
	position: absolute;
	top: 13px;
	left: 10px;
	width: 4px;
	height: 4px;
	border-radius: 2px;
	background-color: #6d757a
}

.bili-header-m .mini-wnd-nav .list li:hover {
	background-color: #e5e9ef
}

.bili-header-m .mini-wnd-nav .list li.no-data {
	text-align: center;
	color: #aaa
}

.bili-header-m .mini-wnd-nav .list li a {
	overflow: hidden;
	white-space: nowrap;
	text-overflow: ellipsis;
	display: block
}

.bili-header-m .mini-wnd-nav .list li a:hover {
	color: #00a1d6
}

.bili-header-m .mini-wnd-nav .list li .link {
	overflow: hidden;
	white-space: nowrap;
	text-overflow: ellipsis;
	display: inline-block
}

.bili-header-m .mini-wnd-nav .read-more {
	display: block;
	margin: 4px 12px 12px;
	background-color: #e5e9ef;
	text-align: center;
	border: 1px solid #e0e6ed;
	height: 22px;
	line-height: 22px;
	color: #222;
	border-radius: 4px
}

.bili-header-m .mini-wnd-nav .read-more:hover {
	background-color: #ccd0d7
}

.bili-header-m .mini-wnd-nav .m-w-loading {
	height: 100px;
	line-height: 100px;
	text-align: center
}

.slide-fade-enter-active, .slide-fade-leave-active {
	transition: all .3s
}

.slide-fade-enter, .slide-fade-leave-to {
	transform: translateY(5px);
	opacity: 0
}

.stardust-video .nav-menu {
	height: 50px
}

.stardust-video .nav-menu .nav-con .nav-item {
	line-height: 50px;
	height: 50px
}

.stardust-video .nav-menu .nav-con .nav-item .t .num {
	top: 5px
}

.stardust-video .nav-menu .nav-con .nav-item.home {
	margin-left: 80px;
	padding-left: 0
}

.stardust-video .nav-menu .nav-con .nav-item.home a {
	padding-left: 8px
}

.stardust-video .nav-menu .nav-con .nav-item.home i {
	position: absolute;
	width: 70px;
	height: 32px;
	left: -80px;
	top: 8px;
	background:
		url(//s1.hdslb.com/bfs/seed/jinkela/header/images/logo_blue.png)
		no-repeat;
	background-size: contain
}

.stardust-video .nav-menu .nav-con .nav-item .app-orcode-box,
	.stardust-video .nav-menu .nav-con .nav-item .i-frame {
	top: 50px
}

.stardust-video .nav-menu .up-load {
	height: 50px
}

.stardust-video .nav-menu .up-load .u-link {
	height: 54px;
	line-height: 48px
}

.stardust-video .nav-menu .up-load .up-nav {
	top: 50px
}

.stardust-video .head-banner {
	margin-top: -50px
}

.stardust-video .mini-wnd-nav {
	top: 50px
}

.stardust-video .profile-m {
	top: 50px !important
}

.stardust-video .nav-search {
	margin: 9px 12px 5px 0 !important
}

@media screen and (max-width:1341px) {
	.hbili {
		display: none
	}
}
</style>
<style type="text/css">
.bili-header-m .nav-search {
	position: relative;
	float: right;
	height: 32px;
	margin: 5px 12px 5px 0;
	width: 90px
}

.bili-header-m .nav-search #nav_searchform {
	display: block;
	background-color: #fff;
	border-radius: 16px;
	padding-right: 30px;
	height: 30px;
	transition: border-color .2s;
	border: 1px solid #ccd0d7
}

.bili-header-m .nav-search #nav_searchform:hover {
	border-color: #99a2aa
}

.bili-header-m .nav-search .nav-search-keyword {
	float: left;
	width: 40px;
	color: #99a2aa;
	font-size: 12px;
	overflow: hidden;
	height: 30px;
	line-height: 30px;
	padding: 0 0 0 10px;
	border: none;
	box-shadow: none;
	background-color: transparent;
	transition: width .2s
}

.bili-header-m .nav-search .nav-search-keyword::-ms-clear {
	display: none
}

.bili-header-m .nav-search .nav-search-keyword:focus {
	color: #222
}

.bili-header-m .nav-search .nav-search-submit {
	display: block;
	position: absolute;
	top: 0;
	right: 0;
	width: 30px;
	min-width: 0;
	cursor: pointer;
	height: 32px;
	background: url(//static.hdslb.com/images/base/icons.png) -786px -721px;
	margin: 0;
	padding: 0;
	border: none
}

.bili-header-m .nav-search .nav-search-submit:hover {
	background-position: -723px -721px
}
</style>
<style type="text/css">
.bili-header-m .bilibili-suggest {
	position: relative;
	border: 1px solid #e5e9ef;
	margin-top: 2px;
	background: #fff;
	z-index: 99999;
	border-radius: 4px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, .16);
	padding-bottom: 5px;
	font-size: 12px
}

.bili-header-m .bilibili-suggest.nav {
	width: 150px
}

.bili-header-m .bilibili-suggest.nav .suggest-item a {
	max-width: 100px
}

.bili-header-m .bilibili-suggest .suggest-item {
	padding: 6px 10px;
	cursor: pointer;
	word-wrap: break-word;
	word-break: break-all;
	display: block;
	color: #222;
	position: relative
}

.bili-header-m .bilibili-suggest .suggest-item.focus, .bili-header-m .bilibili-suggest .suggest-item:hover
	{
	background-color: #e5e9ef
}

.bili-header-m .bilibili-suggest .suggest-item a {
	max-width: 200px;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
	color: #222;
	display: block
}

.bili-header-m .bilibili-suggest .suggest-item a.link-wrp {
	display: block
}

.bili-header-m .bilibili-suggest .suggest-item .suggest_high_light {
	color: #f25d8e
}

.bili-header-m .bilibili-suggest .b-line {
	border-top: 1px solid #e5e9ef;
	position: relative;
	height: 10px;
	margin: 10px 10px 0
}

.bili-header-m .bilibili-suggest .b-line.history-t {
	margin: 20px 10px 0;
	height: 20px
}

.bili-header-m .bilibili-suggest .b-line p {
	margin-top: -10px;
	text-align: center
}

.bili-header-m .bilibili-suggest .b-line span {
	display: inline-block;
	padding: 0 10px;
	height: 18px;
	text-align: center;
	cursor: pointer;
	color: #99a2aa;
	background: #fff
}
</style>
<style type="text/css">
.bili-header-m .bilibili-suggest {
	position: relative;
	border: 1px solid #e5e9ef;
	margin-top: 2px;
	background: #fff;
	z-index: 99999;
	border-radius: 4px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, .16);
	padding-bottom: 5px;
	font-size: 12px
}

.bili-header-m .bilibili-suggest.nav {
	width: 150px
}

.bili-header-m .bilibili-suggest.nav .suggest-item a {
	max-width: 100px
}

.bili-header-m .bilibili-suggest .suggest-item {
	padding: 6px 10px;
	cursor: pointer;
	word-wrap: break-word;
	word-break: break-all;
	display: block;
	color: #222;
	position: relative
}

.bili-header-m .bilibili-suggest .suggest-item.focus, .bili-header-m .bilibili-suggest .suggest-item:hover
	{
	background-color: #e5e9ef
}

.bili-header-m .bilibili-suggest .suggest-item a {
	color: #222;
	display: block;
	max-width: 200px;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap
}

.bili-header-m .bilibili-suggest .suggest-item a.link-wrp {
	display: block
}

.bili-header-m .bilibili-suggest .b-line {
	border-top: 1px solid #e5e9ef;
	position: relative;
	height: 10px;
	margin: 10px 10px 0
}

.bili-header-m .bilibili-suggest .b-line.history-t {
	margin: 20px 10px 0;
	height: 20px
}

.bili-header-m .bilibili-suggest .b-line p {
	margin-top: -10px;
	text-align: center
}

.bili-header-m .bilibili-suggest .b-line span {
	display: inline-block;
	padding: 0 10px;
	height: 18px;
	text-align: center;
	cursor: pointer;
	color: #99a2aa;
	background: #fff
}

.bili-header-m .bilibili-suggest .cancel {
	position: absolute;
	right: 10px;
	top: 0;
	width: 38px;
	height: 28px;
	background: url(//static.hdslb.com/images/base/icons.png) -461px -530px
		no-repeat
}

.bili-header-m .bilibili-suggest .cancel:hover {
	background-position: -525px -530px
}
</style>
<script type="text/javascript" charset="utf-8" async=""
	src="//s1.hdslb.com/bfs/seed/log/report/2.0ab54.function.chunk.js"></script>
<style type="text/css">
.bili-header-m .i_menu_login {
	background: #fff;
	left: 50%;
	margin-left: -130px;
	width: 260px;
	padding-bottom: 0;
	padding-top: 50px;
	border-top: none;
	width: 320px;
	margin-left: -160px;
	padding: 12px;
	text-align: left;
	line-height: normal;
	border: 1px solid #e5e9ef
}

.bili-header-m .i_menu_login .tip {
	font-size: 12px;
	color: #6d757a
}

.bili-header-m .i_menu_login .img {
	width: 320px;
	height: 200px;
	margin: 12px 0;
	overflow: hidden;
	position: relative;
	background: url(//static.hdslb.com/images/base/danmu.png) no-repeat 50%
}

.bili-header-m .i_menu_login .img img {
	width: 320px;
	height: 200px;
	position: absolute;
	top: 0;
	left: 0
}

.bili-header-m .i_menu_login .login-btn {
	display: block;
	height: 43px;
	line-height: 43px;
	text-align: center;
	background: #00a1d6;
	border-radius: 4px;
	font-size: 14px;
	color: #fff
}

.bili-header-m .i_menu_login .login-btn:hover {
	background: #00b5e5
}

.bili-header-m .i_menu_login .reg {
	margin-top: 8px;
	text-align: center;
	font-size: 12px;
	color: #282828
}

.bili-header-m .i_menu_login .reg a {
	color: #00a1d6
}

.bili-header-m .i_menu_login .reg a:hover {
	color: #00b5e5
}
</style>
</head>
<body>
	<div class="bili-header-m report-wrap-module">
		<div class="nav-menu">
			<!---->
			<div class="nav-mask"></div>
			<div class="bili-wrapper clearfix">
				<div class="nav-con fl">
					<ul>
						<li report-id="playpage_main" class="nav-item home"><a
							href="//www.bilibili.com" title="主站" class="t"><i
								class="bili-icon"></i>主站</a></li>
						<li report-id="playpage_huahua" class="nav-item hbili"><a
							href="//h.bilibili.com" target="_blank" title="画友" class="t">画友</a></li>
						<li report-id="Webtab_click_audio" class="nav-item mbili"><a
							href="//www.bilibili.com/audio/home/?type=10" target="_blank"
							title="来探索bilibili音乐的世界吧~" class="t">音频</a></li>
						<li report-id="playpage_game" class="nav-item game"><a
							href="//game.bilibili.com" target="_blank" title="游戏中心" class="t">游戏中心</a>
							<!----></li>
						<li report-id="playpage_live" class="nav-item live"><a
							href="//live.bilibili.com" target="_blank" title="直播" class="t">直播</a>
							<!----></li>
						<li report-id="playpage_buy" class="nav-item buy"><a
							href="//show.bilibili.com/platform/home.html?msource=pc_web"
							target="_blank" title="会员购" class="t">会员购</a></li>
						<li report-id="playpage_bml" class="nav-item nav-bml"><a
							href="//bml.bilibili.com/2018/index.html#/bmlbj" target="_blank"
							title="BML" class="t">BML<i class="bml-beijing"></i></a> <!----></li>
						<li class="nav-item moe"><a
							href="//www.bilibili.com/moe/2018/jp/home" target="_blank"
							title="萌战" class="t">萌战</a></li>
						<li report-id="playpage_download" class="nav-item mobile"><i
							class="b-icon b-icon-app"></i> <a id="header-mobile-app"
							href="//app.bilibili.com" target="_blank" title="下载APP" class="t">下载APP</a>
							<!----></li>
					</ul>
				</div>
				<div report-id="playpage_contribution" class="up-load fr">
					<a href="//member.bilibili.com/v/video/submit.html" target="_blank"
						class="u-link">投 稿</a>
					<!---->
				</div>
				<div class="nav-con fr">
					<ul>
						<li class="nav-item profile-info"><a
							href="//passport.bilibili.com/login" class="t"><div
									class="i-face">
									<img src="//static.hdslb.com/images/akari.jpg" class="face">
								</div></a>
							<div class="i_menu i_menu_login" style="display: none;">
								<p class="tip">登录后你可以：</p>
								<div class="img">
									<img src="//static.hdslb.com/images/danmu.png"
										style="left: -1px;"> <img
										src="//static.hdslb.com/images/danmu.png" style="left: 320px;">
								</div>
								<a href="//passport.bilibili.com/login" class="login-btn">登录</a>
								<p class="reg">
									首次使用？<a href="//passport.bilibili.com/register/phone.html">点我去注册</a>
								</p>
							</div></li>
						<li report-id="playpage_history" class="nav-item"><a
							href="//www.bilibili.com/account/history" target="_blank"
							class="t">历史</a> <!----></li>
					</ul>
				</div>
				<div class="nav-con fr">
					<!---->
					<div class="nav-search">
						<form id="nav_searchform">
							<input type="text" autocomplete="off" accesskey="s"
								x-webkit-speech="" x-webkit-grammar="builtin:translate"
								placeholder="筋肉少女的养成（老母亲微笑！" class="nav-search-keyword">
							<button type="submit" class="nav-search-submit"></button>
						</form>
						<!---->
						<!---->
					</div>
				</div>
			</div>
		</div>
		<!---->
		<!---->
	</div>
	<div id="app" class="media-detail-wrp">
		<div class="media-info-wrp">
			<div class="bangumi-info-bg-wrp">
				<div class="bangumi-info-blurbg-wrapper">
					<div class="bangumi-info-blurbg blur"
						style="background-image: url(https://i0.hdslb.com/bfs/bangumi/320a6c9893a874e7db755ecb7316a0d0abccec49.jpg@260w_350h.webp);"></div>
				</div>
				<!---->
			</div>
			<div class="media-info-content">
				<div class="media-info-inner clearfix">
					<div class="media-preview">
						<div class="common-lazy-img">
							<img alt="小林家的龙女仆"
								src="//i0.hdslb.com/bfs/bangumi/320a6c9893a874e7db755ecb7316a0d0abccec49.jpg@450w_600h.webp"
								lazy="loaded">
						</div>
						<div class="tag-exclusive"></div>
					</div>
					<div class="media-info-r">
						<div class="media-info-title">
							<span class="media-info-title-t">小林家的龙女仆</span><span
								class="media-tags" style="opacity: 1;"><span
								class="media-tag">萌系</span><span class="media-tag">搞笑</span><span
								class="media-tag">日常</span><span class="media-tag">百合</span><span
								class="media-tag">漫改</span></span>
						</div>
						<div class="media-info-datas">
							<div class="media-info-count">
								<span class="media-info-count-item media-info-count-item-play"><span
									class="media-info-label">总播放</span><em>1亿</em></span><span
									class="media-info-count-item media-info-count-item-fans"><span
									class="media-info-label">追番人数</span><em>341.9万</em></span><span
									class="media-info-count-item media-info-count-item-review"><span
									class="media-info-label">弹幕总数</span><em>338.3万</em></span>
							</div>
							<div class="media-info-score-wrp">
								<div class="media-info-score">
									<div class="media-info-score-content">
										<div>9.3</div>
									</div>
									<span class="review-stars"><i
										class="icon-star icon-star-light"><i></i></i><i
										class="icon-star icon-star-light"><i></i></i><i
										class="icon-star icon-star-light"><i></i></i><i
										class="icon-star icon-star-light"><i></i></i><i
										class="icon-star icon-star-light"><i></i></i></span>
									<div class="media-info-review-times">9719人评</div>
									<div class="to-review-btn">
										<i class="icon-edit"></i> 我要点评
									</div>
								</div>
								<!---->
							</div>
						</div>
						<div class="media-info-time">
							<span>2017年1月11日 开播</span><span> 已完结, 全13话 </span>
						</div>
						<div class="media-info-intro">
							<span class="media-info-intro-text">简介：在单身的辛苦OL小林身边突然出现的女仆装束的美少女托尔。长着角和尾巴的她的身姿正是所谓的龙娘。在醉酒的小林邀请下说要到家里去的托尔，鬼使神差地开始以小林家女仆的身份工作……！？“女仆”+“龙”=“女仆龙”有着笨手笨脚的可爱之处！龙娘与人类之间基本上很温暖、偶尔有些黑暗的异种族间交流喜剧！！</span>
							<!---->
							<!---->
						</div>
						<div class="media-info-btns">
							<!---->
							<div class="bangumi-btn">
								<div class="btn-follow">
									<i></i>追番
								</div>
							</div>
							<div class="share-module">
								<ul class="share-list clearfix" data-module="share_module_0">
									<li share-type="app" class="share-btn btn-wchat"><div
											class="weixin-share-modal">
											<canvas class="qrcode-wrapper" id="app-qrcode-wrapper"
												height="140" width="140"></canvas>
											<p class="share-name">小林家的龙女仆</p>
											<p class="share-tips">
												用<a href="https://app.bilibili.com/" target="_blank">哔哩哔哩客户端</a>或其他应用扫描二维码
											</p>
										</div></li>
									<li share-type="weibo" class="share-btn btn-weibo"></li>
									<li share-type="qqzone" class="share-btn btn-qqzone"></li>
									<li share-type="qq" class="share-btn btn-qq"></li>
									<li share-type="baidu" class="share-btn btn-baidu"></li>
								</ul>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="media-tab-wrp">
			<div class="media-tab-nav">
				<ul class="clearfix">
					<li class="">作品详情</li>
					<li class="">长评 ( 42 )</li>
					<li class="on">短评 ( 3632 )</li>
					<li class="">相关视频</li>
				</ul>
			</div>
			<div class="media-tab-content">
				<div class="media-tab-detail-wrp clearfix">
					<div class="media-tab-detail-l-wrp">
						<!---->
						<div class="media-tab-detail-l" style="">
							<div class="media-tab-module-wrp">
								<div class="media-tab-module-title">短评</div>
								<div class="media-tab-module-sort">
									<div class="sort-type-wrp">
										<div>
											默认<i></i>
										</div>
										<ul style="display: none;">
											<li>默认</li>
											<li>最新</li>
										</ul>
									</div>
								</div>
								<div class="media-tab-module-write type-btn">去写短评</div>
								<div class="media-tab-module-content">
									<div class="mtlr-list-wrp">
										<div class="review-list-wrp type-short" first-load="true">
											<ul>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="杀错了酱"
																	src="//i2.hdslb.com/bfs/face/666d8fa71e9635a43f5c4db194dc10882dac7c7e.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">杀错了酱</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">07-24</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">赶紧出第二季吧！没有托尔看的我快要变成咸鱼了！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>197
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="苍白书生"
																	src="//i1.hdslb.com/bfs/face/1ea3bb82f7599a6e951d8ca3caf795980392b2bd.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">苍白书生</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-08</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">敲喜欢！希望有第二季！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>3
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="丶卤迅"
																	src="//i1.hdslb.com/bfs/face/9efcd681dbe0510e68f429fc49cee432d46fd516.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">丶卤迅</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">11小时前</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">唉～为了康娜又看了一遍……</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="o依旧孤单o" src="">
															</div>
														</div>
														<div class="review-author-name">o依旧孤单o</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">11小时前</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">轻松愉快的剧情里还穿插着一些主线，表面严肃内心温柔的小林，快意恩仇的托尔，懂事的康纳，每个人都能给人留下深刻的印象，并从中看到自己的影子，也许我们都是恶龙，直到遇见愿意为其卸下鳞片，甘愿平凡的那个人。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="风微王凯亚" src="">
															</div>
														</div>
														<div class="review-author-name">风微王凯亚</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">13小时前</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">好想要一只</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="仔崽あ" src="">
															</div>
														</div>
														<div class="review-author-name">仔崽あ</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">21小时前</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">第二遍啦</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="时酒丶" src="">
															</div>
														</div>
														<div class="review-author-name">时酒丶</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">22小时前</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">最喜欢的漫之一，贼好看！！！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="智障酱喵" src="">
															</div>
														</div>
														<div class="review-author-name">智障酱喵</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">23小时前</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">感谢对我的陪伴，有你的时光很开心</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="slient灬浅漠" src="">
															</div>
														</div>
														<div class="review-author-name">slient灬浅漠</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">昨天</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">一部看着很温馨的番，并且能戳中我的笑点</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="寒月烬" src="">
															</div>
														</div>
														<div class="review-author-name">寒月烬</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">昨天</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">希望还有下一季</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="KiNoMotuのSakura" src="">
															</div>
														</div>
														<div class="review-author-name">KiNoMotuのSakura</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-08</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">超喜欢看！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="龙龙虾仁" src="">
															</div>
														</div>
														<div class="review-author-name">龙龙虾仁</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-08</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">期待第二季</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="绍丞s" src="">
															</div>
														</div>
														<div class="review-author-name">绍丞s</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-08</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">很喜欢的一部百合番。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="天气晴ヽ" src="">
															</div>
														</div>
														<div class="review-author-name">天气晴ヽ</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-08</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">驯龙高手</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="生铁zhuazi" src="">
															</div>
														</div>
														<div class="review-author-name">生铁zhuazi</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-29</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">喜欢康娜，康娜超可爱！至今我还没有觉得谁这么可爱捏(///▽///)</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>10
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="SNKS" src="">
															</div>
														</div>
														<div class="review-author-name">SNKS</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-07</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">冷血无情康纳酱，卡哇伊～～～</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="吾乃咸鱼是也" src="">
															</div>
														</div>
														<div class="review-author-name">吾乃咸鱼是也</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-07</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">平静的生活日常，偶尔会有一点点波澜，然而这不能阻止我与小林成亲ಥ≜ಥ</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="根本起不了一个好名字"
																	src="//i1.hdslb.com/bfs/face/f01af7f4c6f7ca1bc06afaaea1780cafec53e8da.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">根本起不了一个好名字</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-07</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">老少适宜</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="吃不胖的小黑猫"
																	src="//i2.hdslb.com/bfs/face/36f6c927bd7e128e55d85b0a94732b3dfb3d7b96.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">吃不胖的小黑猫</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-07</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">_(:ᗤ」ㄥ)_</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="吃披萨不吃圈"
																	src="//i1.hdslb.com/bfs/face/bb18eab724c6557d6643be6b8b9d17c8838d9f1e.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">吃披萨不吃圈</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-07</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">希望早点出第二季。每一对cp都好甜呐！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="永存于心底"
																	src="//i1.hdslb.com/bfs/face/535f308f9ef92644b74372516a8dce717f6bcb63.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">永存于心底</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-07</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">康娜赛高</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="稽菌ya"
																	src="//i1.hdslb.com/bfs/face/dfdb40f2ef92632b2196d6c9739ca957e4729ecc.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">稽菌ya</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-06</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">看过漫画，再看动漫好看。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="軒三岁"
																	src="//i0.hdslb.com/bfs/face/091b2b810ec1b22629b3ccc45b225f9bf8468ae1.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">軒三岁</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-06</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">期待第二部</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="BaLrecat"
																	src="//i1.hdslb.com/bfs/face/43da8b9a58f715fdd241396dd7b51d5292c7514e.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">BaLrecat</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-06</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">没第二季可惜啦</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="原生h曼巴" src="">
															</div>
														</div>
														<div class="review-author-name">原生h曼巴</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-06</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">萌炸的番</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="我吃黄焖鸭米饭" src="">
															</div>
														</div>
														<div class="review-author-name">我吃黄焖鸭米饭</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-06</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">超棒！！最爱的日常番没有之一</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="拾柒不迷糊" src="">
															</div>
														</div>
														<div class="review-author-name">拾柒不迷糊</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-06</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">真的敲好看</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="JERRY_PILOT" src="">
															</div>
														</div>
														<div class="review-author-name">JERRY_PILOT</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-06</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">龙女仆赛高！！！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="拖更狂魔柳安牧" src="">
															</div>
														</div>
														<div class="review-author-name">拖更狂魔柳安牧</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-06</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">轻松，可爱，搞笑，有一点点俏皮的抒情，真诚而朴实的讲点道理。好番。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="Alice丶疯狂回归" src="">
															</div>
														</div>
														<div class="review-author-name">Alice丶疯狂回归</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-06</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">好看</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="沐之轩雨" src="">
															</div>
														</div>
														<div class="review-author-name">沐之轩雨</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-05</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">我的入宅番，永远支持</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="今朝有酒祈未醉" src="">
															</div>
														</div>
														<div class="review-author-name">今朝有酒祈未醉</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-05</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">说起来还是因为康娜的表情包我才过来看这个番的。这个番就是简单的日常番，但是因为有了好几条龙而产生了意想不到的感觉。很喜欢的一部动漫</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="love丶myheart" src="">
															</div>
														</div>
														<div class="review-author-name">love丶myheart</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-05</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">好看！！！！！！！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="伊莉雅い" src="">
															</div>
														</div>
														<div class="review-author-name">伊莉雅い</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-05</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">也是超级喜欢的日常番了</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="无敌的我也无邪" src="">
															</div>
														</div>
														<div class="review-author-name">无敌的我也无邪</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-05</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">超级可爱超级好看</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="将于无所希望中得救" src="">
															</div>
														</div>
														<div class="review-author-name">将于无所希望中得救</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-05</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">日常番里，龙女仆真的很温馨，虽然没有什么太多的深度，不过真的很温暖，像是在汹涌的现实大潮中找到了一个避风港一样让人心安</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="色烺君" src="">
															</div>
														</div>
														<div class="review-author-name">色烺君</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-05</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">这是一部让我不舍得快进的动漫。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="たちばなかの推し" src="">
															</div>
														</div>
														<div class="review-author-name">たちばなかの推し</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star"><i></i></i></span>
														</div>
														<div class="review-author-time">09-04</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">想写很多又懒，，嘿嘿，总之谢谢陪伴</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="Minisoda动画工作室"
																	src="//i2.hdslb.com/bfs/face/7bad84487642c633695d8be06b36a51eddf8c5ed.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">Minisoda动画工作室</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-04</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">很有爱的一部番，很治愈，大爱。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="叶月星的红"
																	src="//i2.hdslb.com/bfs/face/8c628e75e91d55e2018209dba9e050f3570e9c82.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">叶月星的红</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star"><i></i></i><i class="icon-star"><i></i></i></span>
														</div>
														<div class="review-author-time">09-04</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">这番打发时间看看还行，几个人物都很有特点，康娜很萌，日常搞笑的部分还凑活，结尾很差，托尔和她父亲的纠葛以及战斗跟闹着玩似的，毫无诚意。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="星恋心语" src="">
															</div>
														</div>
														<div class="review-author-name">星恋心语</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-04</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">非常温馨喜感的番，op和ed也十分完美，刚追完，好看，期待下一季</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="牛奶糖ヽ咖啡" src="">
															</div>
														</div>
														<div class="review-author-name">牛奶糖ヽ咖啡</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-04</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">哇⊙∀⊙！真的很好看，这是我看过很多番剧里最喜欢的几部，很搞笑，很感动，很热血，虽然每天都有很多事发生但是依然是围绕这一个普通人起床，上班，下班，回家，吃饭，睡觉。我非常喜欢过着这种很平淡的小事很真实</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="昊神仙IOVOI" src="">
															</div>
														</div>
														<div class="review-author-name">昊神仙IOVOI</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-04</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">超棒</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="再重名切腹" src="">
															</div>
														</div>
														<div class="review-author-name">再重名切腹</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-04</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">终于一亿播放量了！**即正义！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="贫穷限制幻想象" src="">
															</div>
														</div>
														<div class="review-author-name">贫穷限制幻想象</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star"><i></i></i></span>
														</div>
														<div class="review-author-time">09-04</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">萌是真的萌，不过感觉其它的还不够</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="雨下旧亭" src="">
															</div>
														</div>
														<div class="review-author-name">雨下旧亭</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-04</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">这部番我喜欢，只叹太短，emmm</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="123の木" src="">
															</div>
														</div>
														<div class="review-author-name">123の木</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-04</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">敲好看</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="我不是异朽君" src="">
															</div>
														</div>
														<div class="review-author-name">我不是异朽君</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-04</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">好！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="张可爱や" src="">
															</div>
														</div>
														<div class="review-author-name">张可爱や</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-04</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">世界第一萌的康娜</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="某个孤傲的中二病患者" src="">
															</div>
														</div>
														<div class="review-author-name">某个孤傲的中二病患者</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-03</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">大部分人都是不想长大的，只是不能继续当小孩了。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="艹尼玛的提莫队长" src="">
															</div>
														</div>
														<div class="review-author-name">艹尼玛的提莫队长</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-03</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">看不够啊！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="空梦灬幻尐" src="">
															</div>
														</div>
														<div class="review-author-name">空梦灬幻尐</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-03</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">好看好看好看(ง •̀_•́)ง有第二部就好了</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="机智的房东大人" src="">
															</div>
														</div>
														<div class="review-author-name">机智的房东大人</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-03</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">欠你的评分</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="恢宏之翼" src="">
															</div>
														</div>
														<div class="review-author-name">恢宏之翼</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-03</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">什么时候有第二季呢。。。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="金宥真的小跟班" src="">
															</div>
														</div>
														<div class="review-author-name">金宥真的小跟班</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-02</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">我想要一只托尔和康娜！！！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="灵怿" src="">
															</div>
														</div>
														<div class="review-author-name">灵怿</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-01</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">这么好看的动漫居然没上9.5分不科学！另外op真的好听！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>2
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="绛曲拎着小猎枪" src="">
															</div>
														</div>
														<div class="review-author-name">绛曲拎着小猎枪</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-01</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">曾经虐哭我无数次，托尔对小林的感情真挚，至死不渝。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>2
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="Dr友人A" src="">
															</div>
														</div>
														<div class="review-author-name">Dr友人A</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">超喜欢的百合轻喜剧！因为评分只有9.3来着一直没有下决心补，现在看完感觉非常棒的嘛，另外，贺突破一亿大关！ps:你们一个个的都强康娜，我就把托尔抱走啦～～～(*°∀°)=3</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>3
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="8分音符ちやん"
																	src="//i1.hdslb.com/bfs/face/4f7187051c86473838f621ef9416df7e5fc6a84a.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">8分音符ちやん</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">有欢快有感动，剧情节奏张弛有度，好番无疑。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>3
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="热评゚゙゚゙゚゙゚゙"
																	src="//i0.hdslb.com/bfs/face/11f217565887b25bb3a9ab515134043feab9eeeb.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">热评゚゙゚゙゚゙゚゙</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">很不错的一部日常番，顺便求出第二季啊！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>4
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="依沐怜" src="">
															</div>
														</div>
														<div class="review-author-name">依沐怜</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-02</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">1亿！！！！！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="风花酱雪月" src="">
															</div>
														</div>
														<div class="review-author-name">风花酱雪月</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-02</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">看了一遍又一遍，剧情温馨又合理，每个人物都生动可爱有个性，好作品很难得！(｡･ω･｡)</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="釉色千年" src="">
															</div>
														</div>
														<div class="review-author-name">釉色千年</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-02</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">戳中各种萌点，日常轻松不乏哲理</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="Kyoko_Toshinou" src="">
															</div>
														</div>
														<div class="review-author-name">Kyoko_Toshinou</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star"><i></i></i></span>
														</div>
														<div class="review-author-time">09-02</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">日常，乡愁，不太喜欢康娜以外的人设。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="默默吻痕" src="">
															</div>
														</div>
														<div class="review-author-name">默默吻痕</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-01</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">很轻松的番剧，闲下来的时候，累的时候可以看一看。我倒是觉得看的时候不用想太多，开心就好了。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="9火龙9" src="">
															</div>
														</div>
														<div class="review-author-name">9火龙9</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-01</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">这部作品给我的感觉就是很温馨，很温暖，每次看完都给了我追求美好生活的动力，顺便说一句“康纳好萌！”</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="トール昀丶" src="">
															</div>
														</div>
														<div class="review-author-name">トール昀丶</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-01</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">大爱托尔</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="野渡无人_" src="">
															</div>
														</div>
														<div class="review-author-name">野渡无人_</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-01</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">太可爱了</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="烤糊的德棍" src="">
															</div>
														</div>
														<div class="review-author-name">烤糊的德棍</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star"><i></i></i></span>
														</div>
														<div class="review-author-time">09-01</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">真是不得了啊</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="Mrs锦城" src="">
															</div>
														</div>
														<div class="review-author-name">Mrs锦城</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-01</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">很暖很可爱</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="秋名山上的神烦狗" src="">
															</div>
														</div>
														<div class="review-author-name">秋名山上的神烦狗</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-01</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">？？？？？怎么被顶上排行榜来了</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="樱花の时祁" src="">
															</div>
														</div>
														<div class="review-author-name">樱花の时祁</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-01</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">美好就足够了</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="紫川翾缘" src="">
															</div>
														</div>
														<div class="review-author-name">紫川翾缘</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-01</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">每季只追一个番的我~已经沉溺于日常温情中啦~</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="劳登sama" src="">
															</div>
														</div>
														<div class="review-author-name">劳登sama</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-01</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">好看好看</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="こ晓风残月i" src="">
															</div>
														</div>
														<div class="review-author-name">こ晓风残月i</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">希望龙不是神话，而是真真实实的存在，并且能和我们和睦相处。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="中二_清酒" src="">
															</div>
														</div>
														<div class="review-author-name">中二_清酒</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">09-01</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">很棒的日常，康纳真萌\(//∇//)\，内容受众很广泛，要是有三次元的朋友要我给他推荐日常番，绝对是这部！果然京阿尼从来没有让我失望过！！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="墨色苍凉" src="">
															</div>
														</div>
														<div class="review-author-name">墨色苍凉</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">很温馨的一部日常番，京阿尼不愧是京阿尼</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="夏至的玻璃瓶"
																	src="//i1.hdslb.com/bfs/face/d44d3cfb9e8b1544a53487faee1787d3c2adc392.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">夏至的玻璃瓶</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">真的是我近年来看过最好的日常番了，非常喜欢！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="夜慕寒檀"
																	src="//i0.hdslb.com/bfs/face/0effe755204ab6aeafa20c2502b1beed2928a926.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">夜慕寒檀</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">看完酷教信者老师的关公说事回来又刷了一遍</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="涂山荭荭"
																	src="//i2.hdslb.com/bfs/face/3fe328cce68864602fc642852e65132acb99a47f.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">涂山荭荭</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">迟来的好评！龙女仆简直是我看过的最好看的番了！超级超级好看啊！画风也炒鸡喜欢！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="正经小伙" src="">
															</div>
														</div>
														<div class="review-author-name">正经小伙</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">祝有生之年幸福</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="你丫呦" src="">
															</div>
														</div>
														<div class="review-author-name">你丫呦</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">好看</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="C6H806-" src="">
															</div>
														</div>
														<div class="review-author-name">C6H806-</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">刷了好多遍啦，口口李快出第二季吧</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="U陌路" src="">
															</div>
														</div>
														<div class="review-author-name">U陌路</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">非常轻松的一个番,值得一看</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="盐渍榛子盐" src="">
															</div>
														</div>
														<div class="review-author-name">盐渍榛子盐</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">我永远喜欢……！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="今天依然不会画画" src="">
															</div>
														</div>
														<div class="review-author-name">今天依然不会画画</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">超可爱的，很喜欢(一亿助攻！！)</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="lobebibi" src="">
															</div>
														</div>
														<div class="review-author-name">lobebibi</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">康娜真的非常非常非常可爱啊</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="欧密罗先生" src="">
															</div>
														</div>
														<div class="review-author-name">欧密罗先生</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">阔爱</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="ICEBERG-" src="">
															</div>
														</div>
														<div class="review-author-name">ICEBERG-</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">康娜很可爱</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="Sorrow长情" src="">
															</div>
														</div>
														<div class="review-author-name">Sorrow长情</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">一不小心，看了三四遍了，苏福苏</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="轩嗲嗲灬" src="">
															</div>
														</div>
														<div class="review-author-name">轩嗲嗲灬</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">好好看！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="我妈说名字长了很牛逼" src="">
															</div>
														</div>
														<div class="review-author-name">我妈说名字长了很牛逼</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">***好看</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="小侴丑" src="">
															</div>
														</div>
														<div class="review-author-name">小侴丑</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-31</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">百合赛高！！！！！！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="想吃一口粥" src="">
															</div>
														</div>
														<div class="review-author-name">想吃一口粥</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">康娜超可爱！！！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="盐味の砂糖" src="">
															</div>
														</div>
														<div class="review-author-name">盐味の砂糖</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">赞赞赞！！！没有任何异议给五星！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="指尖赋相思" src="">
															</div>
														</div>
														<div class="review-author-name">指尖赋相思</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">个人来说的话就是结局之前都很有趣，然后到结局了感觉剧情有点收不住了跑的有点偏个人不是很喜欢，但是整体来说这个番的各个方面都是很强的，毕竟京阿尼出品，但是京阿尼自己剧本方面不是很擅长这个也是老问题</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="喜欢你呀希尔薇么么" src="">
															</div>
														</div>
														<div class="review-author-name">喜欢你呀希尔薇么么</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">很好看！喜欢里面的每一个人物。快点出第二季吧。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="尼禄我老公"
																	src="//i0.hdslb.com/bfs/face/2cf8dcfa9ecf33cc26367682d8893f9b15e570fa.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">尼禄我老公</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">托尔，托尔。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="安无趣"
																	src="//i2.hdslb.com/bfs/face/c0c0e0f35688a781b03818e047ff5fe520b77177.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">安无趣</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">好看的日常，让人感觉很轻松</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="诚不自意"
																	src="//i1.hdslb.com/bfs/face/36e12ae5de9ef189605faa433368b415974c1a1b.jpg@60w_60h.webp"
																	lazy="loaded">
															</div>
														</div>
														<div class="review-author-name">诚不自意</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">很温馨的故事 轻松愉快</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="小小小小小小小泉同学" src="">
															</div>
														</div>
														<div class="review-author-name">小小小小小小小泉同学</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">真的很期待第二季</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="蓝鸟bird9" src="">
															</div>
														</div>
														<div class="review-author-name">蓝鸟bird9</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">我——爱——龙——女——仆——！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="東雲黄泉" src="">
															</div>
														</div>
														<div class="review-author-name">東雲黄泉</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">只有满分才能聊表我的评价，销量上的暴死可能是一个遗憾，但是我很庆幸其中有一份是我的，又萌又暖心的日常
															。4刷可能不够，以后会继续温习的</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="丶Gabriel丶丶" src="">
															</div>
														</div>
														<div class="review-author-name">丶Gabriel丶丶</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">托儿老婆赛高</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="澜槿Raylion" src="">
															</div>
														</div>
														<div class="review-author-name">澜槿Raylion</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">太好看了</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="Inori酱的猜谜时" src="">
															</div>
														</div>
														<div class="review-author-name">Inori酱的猜谜时</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">第四周目，不知道为什么，看过那么多遍，再看还是那么好看，笑点依然会笑，甚至有的地方来回回放看</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="摇头娃娃" src="">
															</div>
														</div>
														<div class="review-author-name">摇头娃娃</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">分两个时间段补完的！康纳是我的！！！！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="绝尘居士" src="">
															</div>
														</div>
														<div class="review-author-name">绝尘居士</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">很不错，就是这个世界的人类可能都是星际玩家</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="あ蓝魅·人生" src="">
															</div>
														</div>
														<div class="review-author-name">あ蓝魅·人生</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">我也补完了呢，呀，看得很舒服，京阿尼的作品真棒呢，康娜赛高</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="魔法少女゙゙゙" src="">
															</div>
														</div>
														<div class="review-author-name">魔法少女゙゙゙</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">第二季！第二季！第二季！还是那句话，只要你敢出第二季，我就敢继续买周边！还不出么?那么，我只能去再看一遍了|･ω･｀)</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="QAQ你大爷" src="">
															</div>
														</div>
														<div class="review-author-name">QAQ你大爷</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">看起来很轻松愉悦的番，累了的时候就来这里放松一下。也是入站第一部番，第一个五星短评就留在这里了</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="三笑突然当一痴" src="">
															</div>
														</div>
														<div class="review-author-name">三笑突然当一痴</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">很怀念番里的人物</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="冲锋枪快速扩容弹夹" src="">
															</div>
														</div>
														<div class="review-author-name">冲锋枪快速扩容弹夹</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">神番</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="美利坚民主基金会" src="">
															</div>
														</div>
														<div class="review-author-name">美利坚民主基金会</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">终于一亿啦！五星好评！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="玖玖麦" src="">
															</div>
														</div>
														<div class="review-author-name">玖玖麦</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">龙女仆破亿啦！！！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="ALTERGTR" src="">
															</div>
														</div>
														<div class="review-author-name">ALTERGTR</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">超好看的番 已经回味了几次了</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="菜鸡小枫泾" src="">
															</div>
														</div>
														<div class="review-author-name">菜鸡小枫泾</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">今天正好看完，但很舍不得，希望出第二季，还有就是......一亿贺电！*٩(๑´∀`๑)ง*</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="15是条咸鱼QvQ" src="">
															</div>
														</div>
														<div class="review-author-name">15是条咸鱼QvQ</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-30</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">4周目完成！为什么只有9.3分啊喂！那么好一部番！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="身处樊笼不自知" src="">
															</div>
														</div>
														<div class="review-author-name">身处樊笼不自知</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-29</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">当年追番的时候只是当做一部放松娱乐的日常番来看的，印象最深的也当然是康娜，然而现在二刷的时候才发现这里充满了温情以及淡淡的忧伤，当初只是草草看完的我真是暴殄天物。</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
												<li class="clearfix"><div class="review-author-info">
														<div class="review-author-face">
															<div class="common-lazy-img">
																<img alt="丶妳的专属伯约" src="">
															</div>
														</div>
														<div class="review-author-name">丶妳的专属伯约</div>
														<div class="review-author-star">
															<span class="review-stars"><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i><i
																class="icon-star icon-star-light"><i></i></i></span>
														</div>
														<div class="review-author-time">08-29</div>
													</div>
													<div class="review-detail">
														<!---->
														<div class="review-content">恭喜破亿！</div>
													</div>
													<!---->
													<div class="review-data">
														<div class="review-data-like">
															<i class="icon-zan"></i>1
														</div>
														<div class="review-data-unlike">
															<i class="icon-cai"></i>
														</div>
													</div>
													<div class="review-contro">
														<!---->
														<div class="review-contro-chigua">
															<div class="review-contro-report">举报</div>
														</div>
													</div></li>
											</ul>
											<!---->
										</div>
									</div>
								</div>
							</div>
						</div>
						<!---->
					</div>
					<div class="media-tab-detail-r">
						<div class="review-feed-wrapper">
							<div class="feed-header clearfix">
								<h4>点评动态</h4>
								<span><i class="icon-refresh"></i>换一换</span>
							</div>
							<ul class="feed-list">
								<div class="review-feed-item clearfix">
									<div class="feed-left">
										<div class="review-info">
											<a target="_blank"
												href="//www.bilibili.com/bangumi/media/md102392/review/ld32138/"
												title="轻松愉悦的课堂" class="review-title">轻松愉悦的课堂</a><a
												target="_blank"
												href="//www.bilibili.com/bangumi/media/md102392/review/ld32138/"
												class="review-content">对于这种好番，不能看过就算了，我的脑细胞强烈要求我写点东西---说实话近来都没有看过像这种轻松愉悦的番了。我作为一个吃瓜群众，不懂二次元，但我就觉得，这部作品就是好番，无愧于它九点八分的高分。首先本作品拥有大量的专业知识，这就与许多作品都不一样了。不瞒大家说，我还会暂停仔细看一遍批注，明明我上生物课都没这么认真，可能这就是这部作品的魔力吧。其次本作品节奏轻快，不乏笑点，我看剧的时候甚至会笑出声来吵醒舍友，舍友问我在笑什么，我说我在笑红细胞哈哈哈。再次本作品积极、开朗、阳光。细胞们团结一心一致对外，且每次都能胜利，我真的感到非常安心，真</a>
										</div>
										<div class="review-about">
											<a target="_blank" href="//space.bilibili.com/40672294/"
												class="author-info">我真的就是制杖233</a> 评 <a target="_blank"
												href="//www.bilibili.com/bangumi/media/md102392/"
												class="media-title">工作细胞</a>
										</div>
									</div>
									<div class="feed-right">
										<a href="//www.bilibili.com/bangumi/media/md102392/"
											target="_blank"><img
											src="//i0.hdslb.com/bfs/bangumi/f5d5f51b941c01f8b90b361b412dc75ecc2608d3.png@120w_160h.webp"
											alt=""></a>
										<div class="likes">赞：60</div>
									</div>
								</div>
								<div class="review-feed-item clearfix">
									<div class="feed-left">
										<div class="review-info">
											<a target="_blank"
												href="//www.bilibili.com/bangumi/media/md2572/review/ld36201/"
												title="不多说了，直接五星" class="review-title">不多说了，直接五星</a><a
												target="_blank"
												href="//www.bilibili.com/bangumi/media/md2572/review/ld36201/"
												class="review-content">不知道为什么，我看动漫从来没有像看夏洛特那样，看完的那一段时间，我感觉自己的情绪都已经陷入了里面，我的情绪完全是跟着主角的经历走的，从有宇因为有能力而到处作弊，撩妹，揍人，到被奈绪他们发现加入了学生会，再一点一点揭开作为能力者所背负的“命运”。第七集时看着有宇黑化我心里也难过直到奈绪出来的那一刻，有宇才知道原来一直有人在陪着他，“陪伴是最长情的告白”从这开始，我才真正地相信了这句话。最后的时候陪伴有宇的则变成了奈绪留给他的单词本（老婆本），他以为能力过多忘记了一切包括他自己却仍然没有忘记那个约定。当奈绪说出:乙坂有宇，欢迎回来的时候我</a>
										</div>
										<div class="review-about">
											<a target="_blank" href="//space.bilibili.com/113937248/"
												class="author-info">您的设备不支持查看ll</a> 评 <a target="_blank"
												href="//www.bilibili.com/bangumi/media/md2572/"
												class="media-title">Charlotte</a>
										</div>
									</div>
									<div class="feed-right">
										<a href="//www.bilibili.com/bangumi/media/md2572/"
											target="_blank"><img
											src="//i0.hdslb.com/bfs/bangumi/9c3e77244687a81e4b75e88ec22eeb8dbaa26380.jpg@120w_160h.webp"
											alt=""></a>
										<div class="likes">赞：10</div>
									</div>
								</div>
								<div class="review-feed-item clearfix">
									<div class="feed-left">
										<div class="review-info">
											<a target="_blank"
												href="//www.bilibili.com/bangumi/media/md102892/review/ld36485/"
												title="第九话部分风评爆炸的原因" class="review-title">第九话部分风评爆炸的原因</a><a
												target="_blank"
												href="//www.bilibili.com/bangumi/media/md102892/review/ld36485/"
												class="review-content">以下仅为个人观点，同时含有部分剧透1.时空轮回过分拔高期望说到时空轮回类作品，印象最让人深刻的，往往是小圆和石头门，前期本就精彩的演出配合时空轮回的关键集更加提升了作品的质量，让一个85分的作品有提升到90分的能量于是歌剧中出现了时空轮回后，原本前六话就已经让人心潮澎湃，已经能作为佳作，在第七话的轮回内容出现后更是让人过分的拔高了对歌剧的期望，可能是观众被神展开养刁了，以至于看到轮回就觉得背后没有些精彩的剧情就对不上轮回这个要素一样另外一方面，如同小圆第十话放出后因事故暂停了更新成功酝酿了观众的感情，让后两集的放出更加成功一样，少歌的</a>
										</div>
										<div class="review-about">
											<a target="_blank" href="//space.bilibili.com/9175795/"
												class="author-info">钻地菇</a> 评 <a target="_blank"
												href="//www.bilibili.com/bangumi/media/md102892/"
												class="media-title">少女☆歌剧 Revue Starlight</a>
										</div>
									</div>
									<div class="feed-right">
										<a href="//www.bilibili.com/bangumi/media/md102892/"
											target="_blank"><img
											src="//i0.hdslb.com/bfs/bangumi/e5b3fca7ea7ef660caa810924c44518513636f9d.jpg@120w_160h.webp"
											alt=""></a>
										<div class="likes">赞：3</div>
									</div>
								</div>
								<div class="review-feed-item clearfix">
									<div class="feed-left">
										<div class="review-info">
											<a target="_blank"
												href="//www.bilibili.com/bangumi/media/md79312/review/ld19227/"
												title="出乎意料的第一集，以及对之后的担忧" class="review-title">出乎意料的第一集，以及对之后的担忧</a><a
												target="_blank"
												href="//www.bilibili.com/bangumi/media/md79312/review/ld19227/"
												class="review-content">当初公布动画化消息的时候，玩家们都不知道这剧情如何拿捏，稍有脱节整个故事就畸形了。毕竟总共90小时左右的游戏时间，不是13集能讲全的。但从第一话来看，A1对原版剧情的取舍很得当。赌场部分游戏教程略过得毫不犹豫，相当符合动画的需求。还有一些细节添加得很好，如高卷杏拿下主角头发上的花瓣，龙司谈话时不小心说中了导航的关键词（这里的分镜是关键，很出彩），这两处都是让人能一看就懂。不知道是半年番还是季番，虽然第一集表现突出，但如果只拍13集，是不可能不赶进度的，肯定会在某部分节奏加速。而这个部分可能就是在游戏的后期---也就是有些赶工的奥村春部</a>
										</div>
										<div class="review-about">
											<a target="_blank" href="//space.bilibili.com/12225852/"
												class="author-info">Satania丶</a> 评 <a target="_blank"
												href="//www.bilibili.com/bangumi/media/md79312/"
												class="media-title">女神异闻录5 动画版</a>
										</div>
									</div>
									<div class="feed-right">
										<a href="//www.bilibili.com/bangumi/media/md79312/"
											target="_blank"><img
											src="//i0.hdslb.com/bfs/bangumi/bd69c56891f6e9cea0056a01c013b36d9a3e2abb.png@120w_160h.webp"
											alt=""></a>
										<div class="likes">赞：3</div>
									</div>
								</div>
								<div class="review-feed-item clearfix">
									<div class="feed-left">
										<div class="review-info">
											<a target="_blank"
												href="//www.bilibili.com/bangumi/media/md102252/review/ld36516/"
												title="美式rpg的背景，却被一个日本人创造了出来" class="review-title">美式rpg的背景，却被一个日本人创造了出来</a><a
												target="_blank"
												href="//www.bilibili.com/bangumi/media/md102252/review/ld36516/"
												class="review-content">本作是一个设定极其丰富的类trpg/crpg的世界，对于一个老玩家都很难写出那么丰富的设定，而作者一个日本人居然能写的那么ok，本身就几乎是奇迹。何为trpg呢？一个如雷贯耳的大名：龙与地下城就是其代表，这种游戏是所有rpg的起源，大家用纸笔来扮演一个个的角色，来进行角色扮演，而crpg，便是trpg的电子化产物，将纸笔上的，用想象驱动的产物用程序驱动了起来。其中最为著名的是博德之门，如今也有另一款名为神界原罪的游戏成为了新的名作（但我不喜欢神界原罪崩坏的数值）在这些rpg里面，你有不止一个职业，可以自由分配自己的技能，可以几乎干任何</a>
										</div>
										<div class="review-about">
											<a target="_blank" href="//space.bilibili.com/15062729/"
												class="author-info">丽赛特酱可愛い</a> 评 <a target="_blank"
												href="//www.bilibili.com/bangumi/media/md102252/"
												class="media-title">OVERLORD Ⅲ</a>
										</div>
									</div>
									<div class="feed-right">
										<a href="//www.bilibili.com/bangumi/media/md102252/"
											target="_blank"><img
											src="//i0.hdslb.com/bfs/bangumi/b308ed7b60b8f7ff70f8a122adeb75914702611f.jpg@120w_160h.webp"
											alt=""></a>
										<div class="likes">赞：16</div>
									</div>
								</div>
								<!---->
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="short-review-masker" style="display: none;">
			<div class="short-review-content">
				<div class="dialog-close"></div>
				<div class="review-header-wrap">
					<div class="review-edit-header">
						<a href="//www.bilibili.com/bangumi/media/md5800/" target="_blank"
							class="media-img"><img
							src="//i0.hdslb.com/bfs/bangumi/320a6c9893a874e7db755ecb7316a0d0abccec49.jpg@100w_133h.jpg"
							alt=""></a>
						<div class="media-info">
							<h4>小林家的龙女仆</h4>
							<p class="rate-tip">请发表你对这部作品的评分</p>
							<div class="rate-wrap">
								<ul class="rate-star clearfix">
									<li><i class="icon-star"></i></li>
									<li><i class="icon-star"></i></li>
									<li><i class="icon-star"></i></li>
									<li><i class="icon-star"></i></li>
									<li><i class="icon-star"></i></li>
								</ul>
								<!---->
							</div>
						</div>
					</div>
				</div>
				<div class="review-body-wrap">
					<textarea name="short-review" placeholder=""></textarea>
					<span class="tip" style="color: #99a2aa;">0/100</span>
					<button class="mr-btn">发表短评</button>
				</div>
				<a href="//www.bilibili.com/bangumi/media/md5800/edit"
					target="_blank" class="mr-long-review">想写长评，点这里 &gt;</a>
			</div>
		</div>
		<!---->
		<!---->
		<!---->
		<!---->
		<!---->
		<!---->
		<!---->
	</div>
	<script
		src="//s1.hdslb.com/bfs/static/review/media/manifest.9e4277a5b0e7c1f34cf60b1599cf8adac23d7798.js"
		defer=""></script>
	<script
		src="//s1.hdslb.com/bfs/static/review/media/vendor.9e4277a5b0e7c1f34cf60b1599cf8adac23d7798.js"
		defer=""></script>
	<script
		src="//s1.hdslb.com/bfs/static/review/media/review-media.9e4277a5b0e7c1f34cf60b1599cf8adac23d7798.js"
		defer=""></script>
	<script type="text/javascript">
		0
	</script>
	<div class="footer bili-footer report-wrap-module" id="home_footer">
		<div class="footer-wrp">
			<div class="footer-cnt clearfix report-wrap-module">
				<ul class="boston-postcards">
					<li><div class="tips">bilibili</div>
						<div class="cards">
							<a target="_blank"
								href="//www.bilibili.com/blackboard/aboutUs.html">关于我们</a>
						</div>
						<div class="cards">
							<a target="_blank"
								href="//www.bilibili.com/blackboard/contact.html">联系我们</a>
						</div>
						<div class="cards">
							<a target="_blank" href="//www.bilibili.com/blackboard/join.html">加入我们</a>
						</div>
						<div class="cards">
							<a target="_blank"
								href="//www.bilibili.com/blackboard/friends-links.html">友情链接</a>
						</div>
						<div class="cards">
							<a target="_blank"
								href="//account.bilibili.com/account/official/home">bilibili认证</a>
						</div>
						<div class="cards">
							<a target="_blank" href="http://ir.bilibili.com">Investor
								Relations</a>
						</div></li>
					<li><div class="tips">传送门</div>
						<div class="cards">
							<a target="_blank" href="//www.bilibili.com/blackboard/help.html">帮助中心</a>
						</div>
						<div class="cards">
							<a target="_blank" href="//www.bilibili.com/video/av120040/">高级弹幕</a>
						</div>
						<div class="cards">
							<a target="_blank"
								href="//www.bilibili.com/blackboard/activity_list.html">活动专题页</a>
						</div>
						<div class="cards">
							<a target="_blank"
								href="//www.bilibili.com/blackboard/copyright.html">侵权申诉</a>
						</div>
						<div class="cards">
							<a target="_blank" href="//activity.bilibili.com/">活动中心</a>
						</div>
						<div class="cards">
							<a target="_blank" href="http://link.acg.tv">用户反馈论坛</a>
						</div>
						<div class="cards">
							<a target="_blank" href="//space.bilibili.com/6823116#/album">壁纸站</a>
						</div>
						<div class="cards">
							<a target="_blank"
								href="//www.bilibili.com/blackboard/activity-S1jfy69Jz.html">名人堂</a>
						</div></li>
					<li><div class="block right">
							<a target="_blank" href="//app.bilibili.com/"><div
									class="phone">
									<div class="pic" id="footer-mobile-app"></div>
									<em>客户端下载</em>
									<div class="qrcode-box-wrp">
										<div class="qrcode-box qrcode-app">
											<div class="qrcode-box-arrow"></div>
										</div>
									</div>
								</div></a><a target="_blank" href="http://weibo.com/bilibiliweb"><div
									class="weibo">
									<div class="pic"></div>
									<em>新浪微博</em>
									<div class="qrcode-box-wrp">
										<div class="qrcode-box qrcode-weibo">
											<div class="qrcode-box-arrow"></div>
										</div>
									</div>
								</div></a><a id="weixin"><div class="weixin">
									<div class="pic"></div>
									<em>官方微信</em>
									<div class="qrcode-box-wrp bigvip-qrcode">
										<div class="qrcode-box qrcode-weixin">
											<div class="qrcode-box-arrow"></div>
										</div>
									</div>
								</div></a>
						</div></li>
				</ul>
				<div class="partner">
					<div class="block left" style="padding-top: 0px;">
						<div class="partner-banner"></div>
						<a id="jvs-cert"
							href="https://webcert.cnmstl.net/cert/grade?sn=d3ec53ae63a84350945198bab0251d59"
							target="_blank" style="display: block; max-width: 132px;"><div
								id="jvs-certifyOuter" class="jvs-certifyOuter"
								style="width: 100%; position: relative;">
								<img id="certify-img1" class="  " crossorigin="anonymous"
									src="//backup.hdslb.com/bfs/mainfront/websafe.png"
									style="position: absolute; left: 0px; top: 0px; display: block; width: 100%; height: auto; opacity: 0; max-height: none; border: none;"><img
									id="certify-img2" class="  act" crossorigin="anonymous"
									src="//backup.hdslb.com/bfs/mainfront/confirm.png"
									style="position: absolute; left: 0px; top: 0px; display: block; max-height: none; width: 100%; height: auto; opacity: 1; border: none;">
							</div></a>
					</div>
					<div class="block left"
						style="margin: 0px 68px 0 115px; line-height: 24px; float: none;">
						<p>
							广播电视节目制作经营许可证：<span>（沪）字第1248号</span> | 网络文化经营许可证：<span>沪网文[2016]2296-134号</span>
							| 信息网络传播视听节目许可证：<span>0910417</span> | 互联网ICP备案：<a
								href="http://www.miitbeian.gov.cn/" target="_blank">沪ICP备13002172号-3</a>
							沪ICP证：<span>沪B2-20100043</span> | 违法不良信息举报邮箱：help@bilibili.com |
							违法不良信息举报电话：4000233233转3 | <a
								href="//static.hdslb.com/images/yyzz.png" target="_blank">营业执照</a>
						</p>
						<p>
							<a href="http://www.shjbzx.cn" target="_blank"><i
								class="icons-footer icons-footer-report"></i><span>
									上海互联网举报中心</span></a> |<a href="http://jb.ccm.gov.cn/" target="_blank">12318
								全国文化市场举报网站</a> |<a target="_blank"
								href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011002002436"><img
								src="//static.hdslb.com/images/base/beiantubiao.png"
								style="vertical-align: top;"> 沪公网安备 31011002002436号 |</a><a
								href="mailto:userreport@bilibili.com">儿童色情信息举报专区</a>
						</p>
						<p>
							<a
								href="http://report.12377.cn:13225/toreportinputNormal_anis.do"
								target="_blank">网上有害信息举报专区：<img
								src="//static.hdslb.com/images/12377.png" width="16" height="16"
								style="vertical-align: sub;"> 中国互联网违法和不良信息举报中心
							</a>
						</p>
						<p>公司名称：上海宽娱数码科技有限公司 | 公司地址：上海市杨浦区政立路485号 | 客服电话：4000233233</p>
					</div>
				</div>
			</div>
		</div>
	</div>
	<script type="text/javascript" charset="utf-8"
		src="//static.hdslb.com/common/js/footer.js"></script>
	<script type="text/javascript">
		window.bid = 13, window.spmReportData = {}, window.reportConfig = {
			sample : 1,
			scrollTracker : !0,
			msgObjects : "spmReportData"
		}
	</script>
	<script src="//s1.hdslb.com/bfs/seed/log/report/log-reporter.js"></script>
	<script src="//static.hdslb.com/common/js/xazx.min.js"></script>
</body>
</html>
'''

# if response.status_code == 200:
#     print('111')
#     html = etree.HTML(response.text)
#     #html.xpath()返回的是一个节点类型组成的list
#     fllowers = html.xpath('//li[@class="bangumi-item"]')
#     print(type(fllowers))
#     if fllowers:
#         print('222')
#         print(fllowers)
html = etree.HTML(text2)
fllowers = html.xpath('//div[@class="review-list-wrp type-short"]//li')
print(type(fllowers))
if fllowers:
    print('222')
    print(fllowers)
    username = html.xpath('//div[@class="review-list-wrp type-short"]//li//div[@class="review-author-name"]//text()')
    comment = html.xpath('//div[@class="review-list-wrp type-short"]//li//div[@class="review-content"]//text()')
    print(username)
    print(comment)