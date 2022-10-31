@echo off
echo 通过http方式clone扣1，通过ssl方式clone扣2
set /p branch=(输入选择方式：)

pushd %BN_SERVER_PATH%
if /i %branch% equ 1 (
	echo server\bn-game
	if not exist "bn-game" (
		git clone https://gitlab.bt/projectbn/server/bn-game.git
	)

	echo server\bn-common
	if not exist "bn-common" (
		git clone https://gitlab.bt/projectbn/server/bn-common.git
	)

	echo server\bn-pbdefine
	if not exist "bn-pbdefine" (
		git clone https://gitlab.bt/projectbn/server/bn-pbdefine.git
	)

	echo server\bn-config
	if not exist "bn-config" (
		git clone https://gitlab.bt/projectbn/server/bn-config.git
	)
	echo server\bn-job
	if not exist "bn-job" (
		git clone https://gitlab.bt/projectbn/server/bn-job.git
	)

	echo server\bn-battle
	if not exist "bn-battle" (
		git clone https://gitlab.bt/projectbn/server/bn-battle.git
	)

	echo server\bn-iface
	if not exist "bn-iface" (
		git clone https://gitlab.bt/projectbn/server/bn-iface.git
	)
	echo server\bn-app
	if not exist "bn-app" (
		git clone https://gitlab.bt/projectbn/server/bn-app.git
	)

	echo server\bn-bgm
	if not exist "bn-bgm" (
		git clone https://gitlab.bt/projectbn/server/bn-bgm.git
	)

	echo server\bn-parent
	if not exist "bn-parent" (
		git clone https://gitlab.bt/projectbn/server/bn-parent.git
	)

	echo server\bn-web-login
	if not exist "bn-web-login" (
		git clone https://gitlab.bt/projectbn/server/bn-web-login.git
	)

	echo server\bn-web-common
	if not exist "bn-web-common" (
		git clone https://gitlab.bt/projectbn/server/bn-web-common.git
	)

	echo server\bn-all
	if not exist "bn-all" (
		git clone https://gitlab.bt/projectbn/server/bn-all.git
	)
	
	echo server\bn-db
	if not exist "bn-db" (
		git clone https://gitlab.bt/projectbn/server/bn-db.git
	)

	echo server\bn-web-pay
	if not exist "bn-web-pay" (
		git clone https://gitlab.bt/projectbn/server/bn-web-pay.git
	)

	echo server\bn-web-activity
	if not exist "bn-web-activity" (
		git clone https://gitlab.bt/projectbn/server/bn-web-activity.git
	)

	echo server\bn-mock
	if not exist "bn-mock" (
		git clone https://gitlab.bt/projectbn/server/bn-mock.git
	)

	echo server\bn-bomberman
	if not exist "bn-bomberman" (
		git clone https://gitlab.bt/projectbn/server/bn-bomberman.git
	)

	echo server\bn-upload-mock
	if not exist "bn-upload-mock" (
		git clone https://gitlab.bt/projectbn/server/bn-upload-mock.git
	)

    pushd ..\
    if not exist "common" (
        md common
    )
    pushd common

    echo common\bn-static
    if not exist "bn-static" (
		git clone https://gitlab.bt/projectbn/common/bn-static.git
	)

    echo common\cmddefine
    if not exist "cmddefine" (
		git clone https://gitlab.bt/projectbn/common/cmddefine.git
	)

    echo common\tools
    if not exist "tools" (
		git clone https://gitlab.bt/projectbn/common/tools.git
	)
	
) else if /i %branch% equ 2 (

	echo server\bn-game
	if not exist "bn-game" (
		git clone git@gitlab.bt:projectbn/server/bn-game.git
	)


	echo server\bn-common
	if not exist "bn-common" (
		git clone git@gitlab.bt:projectbn/server/bn-common.git
	)

	echo server\bn-pbdefine
	if not exist "bn-pbdefine" (
		git clone git@gitlab.bt:projectbn/server/bn-pbdefine.git
	)

	echo server\bn-config
	if not exist "bn-config" (
		git clone git@gitlab.bt:projectbn/server/bn-config.git
	)
	echo server\bn-job
	if not exist "bn-job" (
		git clone git@gitlab.bt:projectbn/server/bn-job.git
	)
	
	echo server\bn-battle
	if not exist "bn-battle" (
		git clone git@gitlab.bt:projectbn/server/bn-battle.git
	)

	echo server\bn-iface
	if not exist "bn-iface" (
		git clone git@gitlab.bt:projectbn/server/bn-iface.git
	)
	echo server\bn-app
	if not exist "bn-app" (
		git clone git@gitlab.bt:projectbn/server/bn-app.git
	)

	echo server\bn-bgm
	if not exist "bn-bgm" (
		git clone git@gitlab.bt:projectbn/server/bn-bgm.git
	)

	echo server\bn-parent
	if not exist "bn-parent" (
		git clone git@gitlab.bt:projectbn/server/bn-parent.git
	)

	echo server\bn-web-login
	if not exist "bn-web-login" (
		git clone git@gitlab.bt:projectbn/server/bn-web-login.git
	)

	echo server\bn-web-common
	if not exist "bn-web-common" (
		git clone git@gitlab.bt:projectbn/server/bn-web-common.git
	)

	echo server\bn-all
	if not exist "bn-all" (
		git clone git@gitlab.bt:projectbn/server/bn-all.git
	)
	
	echo server\bn-db
	if not exist "bn-db" (
		git clone git@gitlab.bt:projectbn/server/bn-db.git
	)

	echo server\bn-web-pay
	if not exist "bn-web-pay" (
		git clone git@gitlab.bt:projectbn/server/bn-web-pay.git
	)

	echo server\bn-web-activity
	if not exist "bn-web-activity" (
		git clone git@gitlab.bt:projectbn/server/bn-web-activity.git
	)

	echo server\bn-mock
	if not exist "bn-mock" (
		git clone git@gitlab.bt:projectbn/server/bn-mock.git
	)

	echo server\bn-bomberman
	if not exist "bn-bomberman" (
		git clone git@gitlab.bt:projectbn/server/bn-bomberman.git
	)

	echo server\bn-upload-mock
	if not exist "bn-upload-mock" (
		git clone git@gitlab.bt:projectbn/server/bn-upload-mock.git
	)

    pushd ..\
    if not exist "common" (
        md common
    )
    pushd common

    echo common\bn-static
    if not exist "bn-static" (
		git clone git@gitlab.bt:projectbn/common/bn-static.git
	)

    echo common\cmddefine
    if not exist "cmddefine" (
		git clone git@gitlab.bt:projectbn/common/cmddefine.git
	)

    echo common\tools
    if not exist "tools" (
		git clone git@gitlab.bt:projectbn/common/tools.git
	)

)
pause

