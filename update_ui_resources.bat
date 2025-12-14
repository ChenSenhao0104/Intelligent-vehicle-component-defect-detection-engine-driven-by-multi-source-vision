@echo on
:: 设置变量
set PROJECT_DIR=D:\steel_defect_detection\SteelDetection\SteelDetection
set RESOURCE_QRC=%PROJECT_DIR%\ui_sources.qrc
set RESOURCE_PY=%PROJECT_DIR%\ui_sources_rc.py
set TARGET_PNG=%PROJECT_DIR%\UIProgram\ui_imgs\11.png
set NEW_IMAGE=%PROJECT_DIR%\UIProgram\ui_imgs\12.png

echo 替换图片中...
copy /Y "%NEW_IMAGE%" "%TARGET_PNG%"
echo 上一步 copy 命令执行完成。
pause

echo 正在重新编译资源文件...
"D:\anaconda\anaconda3\pyrcc5.bat" "%RESOURCE_QRC%" -o "%RESOURCE_PY%"
echo 上一步 pyrcc5 执行完成。
pause

echo 编译完成，资源文件已更新：%RESOURCE_PY%
echo ---
echo ? 操作完成！请运行 MainProgram.py 查看新图是否生效。
pause