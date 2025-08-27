# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arktoolspcg2icaDEG.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frm_principal = QFrame(self.centralwidget)
        self.frm_principal.setObjectName(u"frm_principal")
        self.frm_principal.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_principal.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frm_principal)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frm_principal)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 45))
        self.frame_superior.setMaximumSize(QSize(16777215, 45))
        self.frame_superior.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_superior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.btn_menu = QPushButton(self.frame_superior)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(200, 35))
        self.btn_menu.setMaximumSize(QSize(200, 35))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        self.btn_menu.setFont(font)
        self.btn_menu.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"imagen/fi-sr-rectangle-list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.btn_menu)

        self.horizontalSpacer = QSpacerItem(439, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_minimizar = QPushButton(self.frame_superior)
        self.btn_minimizar.setObjectName(u"btn_minimizar")
        self.btn_minimizar.setMinimumSize(QSize(35, 35))
        self.btn_minimizar.setMaximumSize(QSize(35, 35))
        self.btn_minimizar.setFont(font)
        self.btn_minimizar.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"imagen/fi-sr-arrow-down-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_minimizar.setIcon(icon1)
        self.btn_minimizar.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.btn_minimizar)

        self.btn_restaurar = QPushButton(self.frame_superior)
        self.btn_restaurar.setObjectName(u"btn_restaurar")
        self.btn_restaurar.setMinimumSize(QSize(35, 35))
        self.btn_restaurar.setMaximumSize(QSize(35, 35))
        self.btn_restaurar.setFont(font)
        self.btn_restaurar.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"imagen/fi-sr-expand.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_restaurar.setIcon(icon2)
        self.btn_restaurar.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.btn_restaurar)

        self.btn_maximizar = QPushButton(self.frame_superior)
        self.btn_maximizar.setObjectName(u"btn_maximizar")
        self.btn_maximizar.setMinimumSize(QSize(35, 35))
        self.btn_maximizar.setMaximumSize(QSize(35, 35))
        self.btn_maximizar.setFont(font)
        self.btn_maximizar.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"imagen/fi-sr-expand-arrows.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_maximizar.setIcon(icon3)
        self.btn_maximizar.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.btn_maximizar)

        self.btn_cerrar = QPushButton(self.frame_superior)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setMinimumSize(QSize(35, 35))
        self.btn_cerrar.setMaximumSize(QSize(35, 35))
        self.btn_cerrar.setFont(font)
        self.btn_cerrar.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"imagen/fi-sr-cross-small.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cerrar.setIcon(icon4)
        self.btn_cerrar.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.btn_cerrar)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.frm_principal)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setMinimumSize(QSize(200, 0))
        self.frame_inferior.setMaximumSize(QSize(16777215, 16777215))
        self.frame_inferior.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"   \n"
"}\n"
"")
        self.frame_inferior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_sub_hardware = QFrame(self.frame_inferior)
        self.frame_sub_hardware.setObjectName(u"frame_sub_hardware")
        self.frame_sub_hardware.setMinimumSize(QSize(0, 0))
        self.frame_sub_hardware.setMaximumSize(QSize(0, 16777215))
        self.frame_sub_hardware.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.frame_sub_hardware.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}")
        self.frame_sub_hardware.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sub_hardware.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_sub_hardware)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_inf_sistema = QPushButton(self.frame_sub_hardware)
        self.btn_inf_sistema.setObjectName(u"btn_inf_sistema")
        self.btn_inf_sistema.setMinimumSize(QSize(170, 35))
        self.btn_inf_sistema.setMaximumSize(QSize(170, 35))
        self.btn_inf_sistema.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color:qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"imagen/fi-sr-settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inf_sistema.setIcon(icon5)
        self.btn_inf_sistema.setIconSize(QSize(35, 35))

        self.verticalLayout_5.addWidget(self.btn_inf_sistema)

        self.btn_inf_mbd = QPushButton(self.frame_sub_hardware)
        self.btn_inf_mbd.setObjectName(u"btn_inf_mbd")
        self.btn_inf_mbd.setMinimumSize(QSize(170, 35))
        self.btn_inf_mbd.setMaximumSize(QSize(170, 35))
        self.btn_inf_mbd.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"imagen/Motherboard01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inf_mbd.setIcon(icon6)
        self.btn_inf_mbd.setIconSize(QSize(28, 29))

        self.verticalLayout_5.addWidget(self.btn_inf_mbd)

        self.btn_inf_cpu = QPushButton(self.frame_sub_hardware)
        self.btn_inf_cpu.setObjectName(u"btn_inf_cpu")
        self.btn_inf_cpu.setMinimumSize(QSize(170, 35))
        self.btn_inf_cpu.setMaximumSize(QSize(170, 40))
        self.btn_inf_cpu.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"imagen/fi-sr-cpu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inf_cpu.setIcon(icon7)
        self.btn_inf_cpu.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_inf_cpu)

        self.btn_inf_gpu = QPushButton(self.frame_sub_hardware)
        self.btn_inf_gpu.setObjectName(u"btn_inf_gpu")
        self.btn_inf_gpu.setMinimumSize(QSize(170, 35))
        self.btn_inf_gpu.setMaximumSize(QSize(170, 35))
        self.btn_inf_gpu.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color:qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"imagen/Grafica01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inf_gpu.setIcon(icon8)
        self.btn_inf_gpu.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_inf_gpu)

        self.btn_inf_ram = QPushButton(self.frame_sub_hardware)
        self.btn_inf_ram.setObjectName(u"btn_inf_ram")
        self.btn_inf_ram.setMinimumSize(QSize(170, 35))
        self.btn_inf_ram.setMaximumSize(QSize(170, 35))
        self.btn_inf_ram.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"imagen/RAM.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inf_ram.setIcon(icon9)
        self.btn_inf_ram.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_inf_ram)

        self.btn_inf_hdd = QPushButton(self.frame_sub_hardware)
        self.btn_inf_hdd.setObjectName(u"btn_inf_hdd")
        self.btn_inf_hdd.setMinimumSize(QSize(170, 35))
        self.btn_inf_hdd.setMaximumSize(QSize(170, 35))
        self.btn_inf_hdd.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color:qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"imagen/hdd2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inf_hdd.setIcon(icon10)
        self.btn_inf_hdd.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_inf_hdd)

        self.btn_inf_nic = QPushButton(self.frame_sub_hardware)
        self.btn_inf_nic.setObjectName(u"btn_inf_nic")
        self.btn_inf_nic.setMinimumSize(QSize(170, 35))
        self.btn_inf_nic.setMaximumSize(QSize(170, 35))
        self.btn_inf_nic.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"imagen/Red01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inf_nic.setIcon(icon11)
        self.btn_inf_nic.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_inf_nic)

        self.btn_inf_audio = QPushButton(self.frame_sub_hardware)
        self.btn_inf_audio.setObjectName(u"btn_inf_audio")
        self.btn_inf_audio.setMinimumSize(QSize(170, 35))
        self.btn_inf_audio.setMaximumSize(QSize(170, 35))
        self.btn_inf_audio.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"imagen/fi-sr-foreign-language-audio.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inf_audio.setIcon(icon12)
        self.btn_inf_audio.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_inf_audio)

        self.btn_inf_com = QPushButton(self.frame_sub_hardware)
        self.btn_inf_com.setObjectName(u"btn_inf_com")
        self.btn_inf_com.setMinimumSize(QSize(170, 35))
        self.btn_inf_com.setMaximumSize(QSize(170, 35))
        self.btn_inf_com.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"imagen/hdd.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inf_com.setIcon(icon13)
        self.btn_inf_com.setIconSize(QSize(35, 35))

        self.verticalLayout_5.addWidget(self.btn_inf_com)

        self.btn_inf_usb = QPushButton(self.frame_sub_hardware)
        self.btn_inf_usb.setObjectName(u"btn_inf_usb")
        self.btn_inf_usb.setMinimumSize(QSize(170, 35))
        self.btn_inf_usb.setMaximumSize(QSize(170, 35))
        self.btn_inf_usb.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"imagen/usb1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inf_usb.setIcon(icon14)
        self.btn_inf_usb.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_inf_usb)

        self.btn_inf_bth = QPushButton(self.frame_sub_hardware)
        self.btn_inf_bth.setObjectName(u"btn_inf_bth")
        self.btn_inf_bth.setMinimumSize(QSize(170, 35))
        self.btn_inf_bth.setMaximumSize(QSize(170, 35))
        self.btn_inf_bth.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"imagen/fi-sr-bluetooth-alt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inf_bth.setIcon(icon15)
        self.btn_inf_bth.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_inf_bth)

        self.btn_regresar_menu = QPushButton(self.frame_sub_hardware)
        self.btn_regresar_menu.setObjectName(u"btn_regresar_menu")
        self.btn_regresar_menu.setMinimumSize(QSize(170, 35))
        self.btn_regresar_menu.setMaximumSize(QSize(170, 35))
        self.btn_regresar_menu.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color:qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u"imagen/fi-sr-angle-double-small-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_regresar_menu.setIcon(icon16)
        self.btn_regresar_menu.setIconSize(QSize(35, 35))

        self.verticalLayout_5.addWidget(self.btn_regresar_menu)


        self.horizontalLayout.addWidget(self.frame_sub_hardware)

        self.frame_menu = QFrame(self.frame_inferior)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(0, 0))
        self.frame_menu.setMaximumSize(QSize(0, 16777215))
        self.frame_menu.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}")
        self.frame_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_info_hardware = QPushButton(self.frame_menu)
        self.btn_info_hardware.setObjectName(u"btn_info_hardware")
        self.btn_info_hardware.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color:qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u"imagen/PC02.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_hardware.setIcon(icon17)
        self.btn_info_hardware.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_info_hardware)

        self.btn_info_red = QPushButton(self.frame_menu)
        self.btn_info_red.setObjectName(u"btn_info_red")
        self.btn_info_red.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u"imagen/netword01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_red.setIcon(icon18)
        self.btn_info_red.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_info_red)

        self.btn_info_hardware_2 = QPushButton(self.frame_menu)
        self.btn_info_hardware_2.setObjectName(u"btn_info_hardware_2")
        self.btn_info_hardware_2.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color:qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.btn_info_hardware_2.setIcon(icon17)
        self.btn_info_hardware_2.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_info_hardware_2)

        self.btn_inf_so = QPushButton(self.frame_menu)
        self.btn_inf_so.setObjectName(u"btn_inf_so")
        self.btn_inf_so.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u"imagen/fi-sr-computer-classic.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inf_so.setIcon(icon19)
        self.btn_inf_so.setIconSize(QSize(35, 36))

        self.verticalLayout_3.addWidget(self.btn_inf_so)

        self.btn_inf_regional = QPushButton(self.frame_menu)
        self.btn_inf_regional.setObjectName(u"btn_inf_regional")
        self.btn_inf_regional.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u"imagen/Regional01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inf_regional.setIcon(icon20)
        self.btn_inf_regional.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_inf_regional)

        self.btn_limpiar = QPushButton(self.frame_menu)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u"imagen/Clear01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_limpiar.setIcon(icon21)
        self.btn_limpiar.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_limpiar)

        self.btn_config = QPushButton(self.frame_menu)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color:qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.btn_config.setIcon(icon5)
        self.btn_config.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_config)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.frame_consolas = QFrame(self.frame_inferior)
        self.frame_consolas.setObjectName(u"frame_consolas")
        self.frame_consolas.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"   \n"
"}")
        self.frame_consolas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_consolas.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_consolas)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_consolas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stackedWidget.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.page_inicio.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.page_inicio)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Layout_logo_inicio = QVBoxLayout()
        self.Layout_logo_inicio.setObjectName(u"Layout_logo_inicio")
        self.label_logo_tools = QLabel(self.page_inicio)
        self.label_logo_tools.setObjectName(u"label_logo_tools")
        self.label_logo_tools.setMinimumSize(QSize(120, 120))
        self.label_logo_tools.setMaximumSize(QSize(260, 260))
        self.label_logo_tools.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_logo_tools.setPixmap(QPixmap(u"imagen/ArkToolsPC_02.png"))
        self.label_logo_tools.setScaledContents(True)
        self.label_logo_tools.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Layout_logo_inicio.addWidget(self.label_logo_tools)
        self.verticalLayout_6.addLayout(self.Layout_logo_inicio)
        self.stackedWidget.addWidget(self.page_inicio)
        self.verticalLayout_6.addWidget(self.label_logo_tools, 0, Qt.AlignmentFlag.AlignCenter)
        
        self.page_inf_hardware = QWidget()
        self.page_inf_hardware.setObjectName(u"page_inf_hardware")
        self.page_inf_hardware.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.label_inf_hw1 = QLabel(self.page_inf_hardware)
        self.label_inf_hw1.setObjectName(u"label_inf_hw1")
        self.label_inf_hw1.setGeometry(QRect(700, 470, 71, 61))
        self.label_inf_hw1.setMinimumSize(QSize(40, 40))
        self.label_inf_hw1.setMaximumSize(QSize(80, 80))
        self.label_inf_hw1.setPixmap(QPixmap(u"imagen/PC02.svg"))
        self.label_inf_hw1.setScaledContents(True)
        self.stackedWidget.addWidget(self.page_inf_hardware)
        self.page_inf_hardware_2 = QWidget()
        self.page_inf_hardware_2.setObjectName(u"page_inf_hardware_2")
        self.page_inf_hardware_2.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.label_inf_hw2 = QLabel(self.page_inf_hardware_2)
        self.label_inf_hw2.setObjectName(u"label_inf_hw2")
        self.label_inf_hw2.setGeometry(QRect(670, 460, 71, 61))
        self.label_inf_hw2.setMinimumSize(QSize(40, 40))
        self.label_inf_hw2.setMaximumSize(QSize(80, 80))
        self.label_inf_hw2.setPixmap(QPixmap(u"imagen/PC01.svg"))
        self.label_inf_hw2.setScaledContents(True)
        self.stackedWidget.addWidget(self.page_inf_hardware_2)
        self.page_inf_red = QWidget()
        self.page_inf_red.setObjectName(u"page_inf_red")
        self.page_inf_red.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.label_inf_red = QLabel(self.page_inf_red)
        self.label_inf_red.setObjectName(u"label_inf_red")
        self.label_inf_red.setGeometry(QRect(660, 460, 71, 61))
        self.label_inf_red.setMinimumSize(QSize(40, 40))
        self.label_inf_red.setMaximumSize(QSize(80, 80))
        self.label_inf_red.setPixmap(QPixmap(u"imagen/pcnetwork_102250.svg"))
        self.label_inf_red.setScaledContents(True)
        self.stackedWidget.addWidget(self.page_inf_red)
        self.page_inf_so = QWidget()
        self.page_inf_so.setObjectName(u"page_inf_so")
        self.page_inf_so.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.label_inf_so = QLabel(self.page_inf_so)
        self.label_inf_so.setObjectName(u"label_inf_so")
        self.label_inf_so.setGeometry(QRect(670, 430, 71, 61))
        self.label_inf_so.setMinimumSize(QSize(40, 40))
        self.label_inf_so.setMaximumSize(QSize(80, 80))
        self.label_inf_so.setPixmap(QPixmap(u"imagen/OS02.svg"))
        self.label_inf_so.setScaledContents(True)
        self.stackedWidget.addWidget(self.page_inf_so)
        self.page_inf_regional = QWidget()
        self.page_inf_regional.setObjectName(u"page_inf_regional")
        self.page_inf_regional.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.label_inf_regional = QLabel(self.page_inf_regional)
        self.label_inf_regional.setObjectName(u"label_inf_regional")
        self.label_inf_regional.setGeometry(QRect(650, 450, 71, 61))
        self.label_inf_regional.setMinimumSize(QSize(40, 40))
        self.label_inf_regional.setMaximumSize(QSize(80, 80))
        self.label_inf_regional.setPixmap(QPixmap(u"imagen/Regional01.svg"))
        self.label_inf_regional.setScaledContents(True)
        self.stackedWidget.addWidget(self.page_inf_regional)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_consolas)


        self.verticalLayout_2.addWidget(self.frame_inferior)


        self.verticalLayout.addWidget(self.frm_principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"     Men\u00fa", None))
        self.btn_minimizar.setText("")
        self.btn_restaurar.setText("")
        self.btn_maximizar.setText("")
        self.btn_cerrar.setText("")
#if QT_CONFIG(accessibility)
        self.frame_sub_hardware.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.btn_inf_sistema.setText(QCoreApplication.translate("MainWindow", u"Sistema", None))
        self.btn_inf_mbd.setText(QCoreApplication.translate("MainWindow", u"      Motherboard", None))
        self.btn_inf_cpu.setText(QCoreApplication.translate("MainWindow", u"      CPU", None))
#if QT_CONFIG(shortcut)
        self.btn_inf_cpu.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_inf_gpu.setText(QCoreApplication.translate("MainWindow", u"      GPU", None))
        self.btn_inf_ram.setText(QCoreApplication.translate("MainWindow", u"      RAM", None))
        self.btn_inf_hdd.setText(QCoreApplication.translate("MainWindow", u"      HDD-SSD", None))
        self.btn_inf_nic.setText(QCoreApplication.translate("MainWindow", u"Tarjetas de Red", None))
        self.btn_inf_audio.setText(QCoreApplication.translate("MainWindow", u"      Audio", None))
        self.btn_inf_com.setText(QCoreApplication.translate("MainWindow", u"  Puertos COM", None))
        self.btn_inf_usb.setText(QCoreApplication.translate("MainWindow", u"      USB", None))
        self.btn_inf_bth.setText(QCoreApplication.translate("MainWindow", u"      Bluetooth", None))
        self.btn_regresar_menu.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa Principal", None))
        self.btn_info_hardware.setText(QCoreApplication.translate("MainWindow", u"      Hardware", None))
        self.btn_info_red.setText(QCoreApplication.translate("MainWindow", u"      Red", None))
        self.btn_info_hardware_2.setText(QCoreApplication.translate("MainWindow", u"      Hardware", None))
        self.btn_inf_so.setText(QCoreApplication.translate("MainWindow", u"      Sistema", None))
        self.btn_inf_regional.setText(QCoreApplication.translate("MainWindow", u"      Regional", None))
#if QT_CONFIG(shortcut)
        self.btn_inf_regional.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_limpiar.setText(QCoreApplication.translate("MainWindow", u"      Limpiar", None))
        self.btn_config.setText(QCoreApplication.translate("MainWindow", u"  Configuraci\u00f3n", None))
        self.label_logo_tools.setText("")
        self.label_inf_hw1.setText("")
        self.label_inf_hw2.setText("")
        self.label_inf_red.setText("")
        self.label_inf_so.setText("")
        self.label_inf_regional.setText("")
    # retranslateUi

