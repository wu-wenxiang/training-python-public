# 安装 Sublime

## 注意事项

- 本文是 Sublime 的安装文档
- 适用的操作系统：Win7 / Win10

## 安装步骤

- 下载 [Sublime](https://www.sublimetext.com/3)
- 安装 Sublime，一路默认安装
- 安装 Package Controller
  - [参考](https://packagecontrol.io/installation#st3)
  - Sublime -> View -> Show Console
  - 在控制台中粘贴如下内容，回车

    ```python
    import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path();urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
    ```
- 安装 Anaconda 插件
  - [参考](http://damnwidget.github.io/anaconda/)
  - Sublime -> Tools -> Command Palette
  - 输入：install package

    ![](http://damnwidget.github.io/anaconda/img/screenshots/command_palette.png)
  - 输入：anaconda，回车

    ![install_anaconda.png](http://damnwidget.github.io/anaconda/img/screenshots/install_anaconda.png)
  - 安装完成后，重启Sublime程序，可以代码补全

    ![auto_completion.png](http://damnwidget.github.io/anaconda/img/screenshots/auto_completion.png)
