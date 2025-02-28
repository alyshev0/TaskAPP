# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainpGZuRy.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QHeaderView, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTextEdit, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_TASKMANAGERAPP(object):
    def setupUi(self, TASKMANAGERAPP):
        if not TASKMANAGERAPP.objectName():
            TASKMANAGERAPP.setObjectName(u"TASKMANAGERAPP")
        TASKMANAGERAPP.resize(800, 600)
        self.centralwidget = QWidget(TASKMANAGERAPP)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nametitle = QLineEdit(self.centralwidget)
        self.nametitle.setObjectName(u"nametitle")

        self.verticalLayout.addWidget(self.nametitle)

        self.nameopisanie = QTextEdit(self.centralwidget)
        self.nameopisanie.setObjectName(u"nameopisanie")

        self.verticalLayout.addWidget(self.nameopisanie)
        x = "Alyshev"
        self.calendarik = QCalendarWidget(self.centralwidget)
        self.calendarik.setObjectName(u"calendarik")
        self.calendarik.setStyleSheet(u"font: italic 9pt \"Times New Roman\";\n"
"\n"
"\n"
"selection-background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")

        self.verticalLayout.addWidget(self.calendarik)

        self.TimeEdit = QTimeEdit(self.centralwidget)
        self.TimeEdit.setObjectName(u"TimeEdit")
        self.TimeEdit.setEnabled(True)

        self.verticalLayout.addWidget(self.TimeEdit)

        self.prioritet = QLineEdit(self.centralwidget)
        self.prioritet.setObjectName(u"prioritet")

        self.verticalLayout.addWidget(self.prioritet)

        self.categoria = QLineEdit(self.centralwidget)
        self.categoria.setObjectName(u"categoria")

        self.verticalLayout.addWidget(self.categoria)

        self.taskTable = QTableWidget(self.centralwidget)
        if (self.taskTable.columnCount() < 7):
            self.taskTable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.taskTable.setObjectName(u"taskTable")

        self.verticalLayout.addWidget(self.taskTable)

        self.addtask = QPushButton(self.centralwidget)
        self.addtask.setObjectName(u"addtask")

        self.verticalLayout.addWidget(self.addtask)

        self.updatetask = QPushButton(self.centralwidget)
        self.updatetask.setObjectName(u"updatetask")

        self.verticalLayout.addWidget(self.updatetask)

        self.deletetask = QPushButton(self.centralwidget)
        self.deletetask.setObjectName(u"deletetask")

        self.verticalLayout.addWidget(self.deletetask)

        TASKMANAGERAPP.setCentralWidget(self.centralwidget)

        self.retranslateUi(TASKMANAGERAPP)

        QMetaObject.connectSlotsByName(TASKMANAGERAPP)
    # setupUi

    def retranslateUi(self, TASKMANAGERAPP):
        TASKMANAGERAPP.setWindowTitle(QCoreApplication.translate("TASKMANAGERAPP", u"TaskManager - Alyshev", None))
        self.nametitle.setPlaceholderText(QCoreApplication.translate("TASKMANAGERAPP", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.nameopisanie.setPlaceholderText(QCoreApplication.translate("TASKMANAGERAPP", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.prioritet.setPlaceholderText(QCoreApplication.translate("TASKMANAGERAPP", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442 (\u043d\u0438\u0437\u043a\u0438\u0439, \u0441\u0440\u0435\u0434\u043d\u0438\u0439, \u0432\u044b\u0441\u043e\u043a\u0438\u0439)", None))
        self.categoria.setPlaceholderText(QCoreApplication.translate("TASKMANAGERAPP", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f (\u0440\u0430\u0431\u043e\u0442\u0430, \u0443\u0447\u0435\u0431\u0430, \u043b\u0438\u0447\u043d\u043e\u0435)", None))
        ___qtablewidgetitem = self.taskTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TASKMANAGERAPP", u"ID", None));
        ___qtablewidgetitem1 = self.taskTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TASKMANAGERAPP", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.taskTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TASKMANAGERAPP", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem3 = self.taskTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TASKMANAGERAPP", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem4 = self.taskTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TASKMANAGERAPP", u"\u0414\u0435\u0430\u0434\u043b\u0430\u0439\u043d", None));
        ___qtablewidgetitem5 = self.taskTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TASKMANAGERAPP", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None));
        ___qtablewidgetitem6 = self.taskTable.horizontalHeaderItem(6) # Alyshev
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TASKMANAGERAPP", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None));
        self.addtask.setText(QCoreApplication.translate("TASKMANAGERAPP", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.updatetask.setText(QCoreApplication.translate("TASKMANAGERAPP", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.deletetask.setText(QCoreApplication.translate("TASKMANAGERAPP", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
    # retranslateUi

