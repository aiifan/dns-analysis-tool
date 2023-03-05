#!/usr/bin/env python3
# coding:utf-8
'''
Date: 2023-03-03 12:19:54
Author: aiifan aiifan@126.com
LastEditTime: 2023-03-05 15:52:01
FilePath: /dns-analysis-tool/dns-analysis-tool.py
'''

import ui_untitled 
import sys
from PySide6 import QtCore, QtWidgets, QtGui
import dns.resolver
import dns.exception


def analysis(dns_server: str, domain: str, cord: str) -> list:

    my_resolver = dns.resolver.Resolver()
    my_resolver.nameservers = [dns_server]
    try:
        my_answers = my_resolver.resolve(domain, cord)
    except dns.resolver.NXDOMAIN:
        # the domain does not exist so dns resolutions remain empty
        return "域名不存在"
    except dns.resolver.NoAnswer as e:
        # domains existing but not having AAAA records is common
        return "域名没有AAAA记录"
    except dns.resolver.NoNameservers as e:
        return "DNS服务器不可达"
    res = [dns_respose.to_text() for dns_respose in my_answers.response.answer]
    return sp(res)


def sp(lis: list) -> list:
    list = []
    for l in lis:
        if "\n" in l:
            a = l.split("\n")
            list += a
        else:
            list.append(l)
    return list


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = ui_untitled.Ui_Form()  # 实例化UI对象
        self.ui.setupUi(self)  # 初始化

        self.ui.dns.setText("240e:4b::88")

        self.ui.domain.setText("qq.com,baidu.com")

    @QtCore.Slot()  # 槽函数用它装饰
    def run(self):  # 在Qt Designer中为登录按钮命名的槽函数；

        self.ui.respose.clear()
        dns_servers = self.ui.dns.text()
        # self.ui.dns.
        domains = self.ui.domain.toPlainText()
        cord = self.ui.comboBox.currentText()
        for dns_server in dns_servers.split(','):
            for domain in domains.split(','):
                v = analysis(dns_server, domain, cord)
                if type(v) != list:
                    self.ui.respose.insertPlainText(
                        dns_server + " : " + domain + " : " + v + "\n")
                else:
                    for i in v:
                        self.ui.respose.insertPlainText(
                            dns_server + " : " + i + '\n')

    @QtCore.Slot()
    def openFile(self):
        open_file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open", "", "*.txt;;ALL Files(*)")
        self.ui.filepath.setText(open_file_name)
        file_name = self.ui.filepath.text()
        with open(file_name, "r") as f:
            self.ui.domain.clear()
            a = f.readlines()
            for i in a:
                v = i.replace('\n', ',')
                self.ui.domain.insertPlainText(v)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
