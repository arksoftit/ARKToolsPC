# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arktoolspcg2-bk2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

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
        icon.addFile(u"C:/Users/juanep/.designer/backup/imagen/fi-sr-rectangle-list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon1.addFile(u"assets/icons/fi-sr-arrow-down-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon2.addFile(u"assets/icons/fi-sr-expand.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon3.addFile(u"assets/icons/fi-sr-expand-arrows.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon4.addFile(u"assets/icons/fi-sr-cross-small.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cerrar.setIcon(icon4)
        self.btn_cerrar.setIconSize(QSize(35, 35))

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
        icon5 = QIcon()
        icon5.addFile(u"assets/icons/PC01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_hardware.setIcon(icon5)
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
        icon6 = QIcon()
        icon6.addFile(u"assets/icons/Red01.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_red.setIcon(icon6)
        self.btn_info_red.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_info_red)

        self.btn_info_so = QPushButton(self.frame_menu)
        self.btn_info_so.setObjectName(u"btn_info_so")
        self.btn_info_so.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon7.addFile(u"assets/icons/fi-sr-computer-classic.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_so.setIcon(icon7)
        self.btn_info_so.setIconSize(QSize(35, 36))

        self.verticalLayout_3.addWidget(self.btn_info_so)

        self.btn_info_regional = QPushButton(self.frame_menu)
        self.btn_info_regional.setObjectName(u"btn_info_regional")
        self.btn_info_regional.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon8 = QIcon()
        icon8.addFile(u"assets/icons/Regional01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_regional.setIcon(icon8)
        self.btn_info_regional.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_info_regional)

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
        icon9 = QIcon()
        icon9.addFile(u"assets/icons/Clear01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_limpiar.setIcon(icon9)
        self.btn_limpiar.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_limpiar)

        self.verticalSpacer_3 = QSpacerItem(20, 106, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.btn_operations = QPushButton(self.frame_menu)
        self.btn_operations.setObjectName(u"btn_operations")
        self.btn_operations.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon10 = QIcon()
        icon10.addFile(u"assets/icons/fi-sr-menu-dots.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_operations.setIcon(icon10)
        self.btn_operations.setIconSize(QSize(28, 29))

        self.verticalLayout_3.addWidget(self.btn_operations)

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
        icon11 = QIcon()
        icon11.addFile(u"assets/icons/fi-sr-settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_config.setIcon(icon11)
        self.btn_config.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_config)


        self.horizontalLayout.addWidget(self.frame_menu)

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
        self.btn_info_sistema = QPushButton(self.frame_sub_hardware)
        self.btn_info_sistema.setObjectName(u"btn_info_sistema")
        self.btn_info_sistema.setMinimumSize(QSize(170, 35))
        self.btn_info_sistema.setMaximumSize(QSize(170, 35))
        self.btn_info_sistema.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_info_sistema.setIcon(icon11)
        self.btn_info_sistema.setIconSize(QSize(35, 35))

        self.verticalLayout_5.addWidget(self.btn_info_sistema)

        self.btn_info_mbd = QPushButton(self.frame_sub_hardware)
        self.btn_info_mbd.setObjectName(u"btn_info_mbd")
        self.btn_info_mbd.setMinimumSize(QSize(170, 35))
        self.btn_info_mbd.setMaximumSize(QSize(170, 35))
        self.btn_info_mbd.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon12.addFile(u"assets/icons/mbd_01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_mbd.setIcon(icon12)
        self.btn_info_mbd.setIconSize(QSize(28, 29))

        self.verticalLayout_5.addWidget(self.btn_info_mbd)

        self.btn_info_cpu = QPushButton(self.frame_sub_hardware)
        self.btn_info_cpu.setObjectName(u"btn_info_cpu")
        self.btn_info_cpu.setMinimumSize(QSize(170, 35))
        self.btn_info_cpu.setMaximumSize(QSize(170, 40))
        self.btn_info_cpu.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon13.addFile(u"assets/icons/cpu01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_cpu.setIcon(icon13)
        self.btn_info_cpu.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_info_cpu)

        self.btn_info_gpu = QPushButton(self.frame_sub_hardware)
        self.btn_info_gpu.setObjectName(u"btn_info_gpu")
        self.btn_info_gpu.setMinimumSize(QSize(170, 35))
        self.btn_info_gpu.setMaximumSize(QSize(170, 35))
        self.btn_info_gpu.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon14 = QIcon()
        icon14.addFile(u"assets/icons/Grafica01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_gpu.setIcon(icon14)
        self.btn_info_gpu.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_info_gpu)

        self.btn_info_ram = QPushButton(self.frame_sub_hardware)
        self.btn_info_ram.setObjectName(u"btn_info_ram")
        self.btn_info_ram.setMinimumSize(QSize(170, 35))
        self.btn_info_ram.setMaximumSize(QSize(170, 35))
        self.btn_info_ram.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon15.addFile(u"assets/icons/RAM.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_ram.setIcon(icon15)
        self.btn_info_ram.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_info_ram)

        self.btn_info_hdd = QPushButton(self.frame_sub_hardware)
        self.btn_info_hdd.setObjectName(u"btn_info_hdd")
        self.btn_info_hdd.setMinimumSize(QSize(170, 35))
        self.btn_info_hdd.setMaximumSize(QSize(170, 35))
        self.btn_info_hdd.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon16.addFile(u"assets/icons/hdd2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_hdd.setIcon(icon16)
        self.btn_info_hdd.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_info_hdd)

        self.btn_info_nic = QPushButton(self.frame_sub_hardware)
        self.btn_info_nic.setObjectName(u"btn_info_nic")
        self.btn_info_nic.setMinimumSize(QSize(170, 35))
        self.btn_info_nic.setMaximumSize(QSize(170, 35))
        self.btn_info_nic.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon17 = QIcon()
        icon17.addFile(u"assets/icons/nic01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_nic.setIcon(icon17)
        self.btn_info_nic.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_info_nic)

        self.btn_info_audio = QPushButton(self.frame_sub_hardware)
        self.btn_info_audio.setObjectName(u"btn_info_audio")
        self.btn_info_audio.setMinimumSize(QSize(170, 35))
        self.btn_info_audio.setMaximumSize(QSize(170, 35))
        self.btn_info_audio.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon18.addFile(u"assets/icons/audio01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_audio.setIcon(icon18)
        self.btn_info_audio.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_info_audio)

        self.btn_info_com = QPushButton(self.frame_sub_hardware)
        self.btn_info_com.setObjectName(u"btn_info_com")
        self.btn_info_com.setMinimumSize(QSize(170, 35))
        self.btn_info_com.setMaximumSize(QSize(170, 35))
        self.btn_info_com.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon19.addFile(u"assets/icons/com02.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_com.setIcon(icon19)
        self.btn_info_com.setIconSize(QSize(35, 35))

        self.verticalLayout_5.addWidget(self.btn_info_com)

        self.btn_info_usb = QPushButton(self.frame_sub_hardware)
        self.btn_info_usb.setObjectName(u"btn_info_usb")
        self.btn_info_usb.setMinimumSize(QSize(170, 35))
        self.btn_info_usb.setMaximumSize(QSize(170, 35))
        self.btn_info_usb.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon20.addFile(u"assets/icons/usb1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_usb.setIcon(icon20)
        self.btn_info_usb.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_info_usb)

        self.btn_info_bth = QPushButton(self.frame_sub_hardware)
        self.btn_info_bth.setObjectName(u"btn_info_bth")
        self.btn_info_bth.setMinimumSize(QSize(170, 35))
        self.btn_info_bth.setMaximumSize(QSize(170, 35))
        self.btn_info_bth.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon21.addFile(u"assets/icons/bluetootht.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_bth.setIcon(icon21)
        self.btn_info_bth.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_info_bth)

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
        icon22 = QIcon()
        icon22.addFile(u"assets/icons/fi-sr-angle-double-small-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_regresar_menu.setIcon(icon22)
        self.btn_regresar_menu.setIconSize(QSize(35, 35))

        self.verticalLayout_5.addWidget(self.btn_regresar_menu)


        self.horizontalLayout.addWidget(self.frame_sub_hardware)

        self.frame_operations = QFrame(self.frame_inferior)
        self.frame_operations.setObjectName(u"frame_operations")
        self.frame_operations.setMinimumSize(QSize(0, 0))
        self.frame_operations.setMaximumSize(QSize(0, 16777215))
        self.frame_operations.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}")
        self.frame_operations.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_operations.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_operations)
        self.verticalLayout_16.setSpacing(4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(4, 4, 4, 4)
        self.btn_ark_company = QPushButton(self.frame_operations)
        self.btn_ark_company.setObjectName(u"btn_ark_company")
        self.btn_ark_company.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon23 = QIcon()
        icon23.addFile(u"assets/icons/fi-sr-home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_company.setIcon(icon23)
        self.btn_ark_company.setIconSize(QSize(18, 18))

        self.verticalLayout_16.addWidget(self.btn_ark_company)

        self.btn_ark_clients = QPushButton(self.frame_operations)
        self.btn_ark_clients.setObjectName(u"btn_ark_clients")
        icon24 = QIcon()
        icon24.addFile(u"assets/icons/fi-sr-person-shelter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_clients.setIcon(icon24)
        self.btn_ark_clients.setIconSize(QSize(18, 18))

        self.verticalLayout_16.addWidget(self.btn_ark_clients)

        self.btn_ark_ark_currencies = QPushButton(self.frame_operations)
        self.btn_ark_ark_currencies.setObjectName(u"btn_ark_ark_currencies")
        self.btn_ark_ark_currencies.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon25 = QIcon()
        icon25.addFile(u"assets/icons/fi-sr-currency.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_ark_currencies.setIcon(icon25)
        self.btn_ark_ark_currencies.setIconSize(QSize(18, 18))

        self.verticalLayout_16.addWidget(self.btn_ark_ark_currencies)

        self.btn_ark_categories = QPushButton(self.frame_operations)
        self.btn_ark_categories.setObjectName(u"btn_ark_categories")
        self.btn_ark_categories.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon26 = QIcon()
        icon26.addFile(u"assets/icons/fi-sr-category-alt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_categories.setIcon(icon26)
        self.btn_ark_categories.setIconSize(QSize(18, 18))

        self.verticalLayout_16.addWidget(self.btn_ark_categories)

        self.btn_ark_functional_units = QPushButton(self.frame_operations)
        self.btn_ark_functional_units.setObjectName(u"btn_ark_functional_units")
        self.btn_ark_functional_units.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon27 = QIcon()
        icon27.addFile(u"assets/icons/fi-sr-department-structure.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_functional_units.setIcon(icon27)
        self.btn_ark_functional_units.setIconSize(QSize(18, 18))

        self.verticalLayout_16.addWidget(self.btn_ark_functional_units)

        self.btn_ark_actions = QPushButton(self.frame_operations)
        self.btn_ark_actions.setObjectName(u"btn_ark_actions")
        self.btn_ark_actions.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon28 = QIcon()
        icon28.addFile(u"assets/icons/fi-sr-tasks.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_actions.setIcon(icon28)
        self.btn_ark_actions.setIconSize(QSize(18, 18))

        self.verticalLayout_16.addWidget(self.btn_ark_actions)

        self.btn_ark_employees = QPushButton(self.frame_operations)
        self.btn_ark_employees.setObjectName(u"btn_ark_employees")
        self.btn_ark_employees.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon29 = QIcon()
        icon29.addFile(u"assets/icons/fi-sr-employee-man-alt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_employees.setIcon(icon29)
        self.btn_ark_employees.setIconSize(QSize(18, 18))

        self.verticalLayout_16.addWidget(self.btn_ark_employees)

        self.btn_ark_device_types = QPushButton(self.frame_operations)
        self.btn_ark_device_types.setObjectName(u"btn_ark_device_types")
        self.btn_ark_device_types.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon30 = QIcon()
        icon30.addFile(u"assets/icons/fi-sr-list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_device_types.setIcon(icon30)
        self.btn_ark_device_types.setIconSize(QSize(18, 18))

        self.verticalLayout_16.addWidget(self.btn_ark_device_types)

        self.btn_ark_it_assets = QPushButton(self.frame_operations)
        self.btn_ark_it_assets.setObjectName(u"btn_ark_it_assets")
        self.btn_ark_it_assets.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon31 = QIcon()
        icon31.addFile(u"assets/icons/fi-sr-resources.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_it_assets.setIcon(icon31)
        self.btn_ark_it_assets.setIconSize(QSize(18, 18))

        self.verticalLayout_16.addWidget(self.btn_ark_it_assets)

        self.btn_ark_job_titles = QPushButton(self.frame_operations)
        self.btn_ark_job_titles.setObjectName(u"btn_ark_job_titles")
        self.btn_ark_job_titles.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon32 = QIcon()
        icon32.addFile(u"assets/icons/fi-sr-person-chalkboard.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_job_titles.setIcon(icon32)
        self.btn_ark_job_titles.setIconSize(QSize(18, 18))

        self.verticalLayout_16.addWidget(self.btn_ark_job_titles)

        self.btn_ark_users = QPushButton(self.frame_operations)
        self.btn_ark_users.setObjectName(u"btn_ark_users")
        self.btn_ark_users.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon33 = QIcon()
        icon33.addFile(u"assets/icons/fi-sr-person-simple.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_users.setIcon(icon33)
        self.btn_ark_users.setIconSize(QSize(18, 18))

        self.verticalLayout_16.addWidget(self.btn_ark_users)

        self.btn_menu_ppal = QPushButton(self.frame_operations)
        self.btn_menu_ppal.setObjectName(u"btn_menu_ppal")
        self.btn_menu_ppal.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_menu_ppal.setIcon(icon22)
        self.btn_menu_ppal.setIconSize(QSize(18, 18))

        self.verticalLayout_16.addWidget(self.btn_menu_ppal)


        self.horizontalLayout.addWidget(self.frame_operations)

        self.frame_consolas = QFrame(self.frame_inferior)
        self.frame_consolas.setObjectName(u"frame_consolas")
        self.frame_consolas.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"   \n"
"}")
        self.frame_consolas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_consolas.setFrameShadow(QFrame.Shadow.Raised)
        self.sw_consolas = QStackedWidget(self.frame_consolas)
        self.sw_consolas.setObjectName(u"sw_consolas")
        self.sw_consolas.setGeometry(QRect(10, 32, 776, 509))
        self.sw_consolas.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.sw_consolas.setStyleSheet(u"/* Estilo del marco */\n"
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
        self.verticalLayout_13 = QVBoxLayout(self.page_inicio)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_inicio_head = QFrame(self.page_inicio)
        self.frame_inicio_head.setObjectName(u"frame_inicio_head")
        self.frame_inicio_head.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_inicio_head.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_inicio_head)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.title_arktoolspc = QLabel(self.frame_inicio_head)
        self.title_arktoolspc.setObjectName(u"title_arktoolspc")
        self.title_arktoolspc.setMinimumSize(QSize(40, 60))
        self.title_arktoolspc.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.title_arktoolspc.setFont(font1)
        self.title_arktoolspc.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")
        self.title_arktoolspc.setFrameShadow(QFrame.Shadow.Sunken)
        self.title_arktoolspc.setTextFormat(Qt.TextFormat.PlainText)
        self.title_arktoolspc.setPixmap(QPixmap(u"assets/images/ArlToolsPC2.png"))
        self.title_arktoolspc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.title_arktoolspc)

        self.verticalSpacer_2 = QSpacerItem(20, 94, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_2)


        self.verticalLayout_13.addWidget(self.frame_inicio_head)

        self.frame_inicio_middle = QFrame(self.page_inicio)
        self.frame_inicio_middle.setObjectName(u"frame_inicio_middle")
        self.frame_inicio_middle.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_inicio_middle.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_inicio_middle)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(248, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_logo_tools = QLabel(self.frame_inicio_middle)
        self.label_logo_tools.setObjectName(u"label_logo_tools")
        self.label_logo_tools.setMinimumSize(QSize(120, 120))
        self.label_logo_tools.setMaximumSize(QSize(260, 260))
        self.label_logo_tools.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_logo_tools.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_logo_tools.setPixmap(QPixmap(u"assets/images/ArkToolsPC_02.png"))
        self.label_logo_tools.setScaledContents(True)
        self.label_logo_tools.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_logo_tools)

        self.horizontalSpacer_3 = QSpacerItem(248, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_13.addWidget(self.frame_inicio_middle)

        self.frame_inicio_pie = QFrame(self.page_inicio)
        self.frame_inicio_pie.setObjectName(u"frame_inicio_pie")
        self.frame_inicio_pie.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_inicio_pie.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_inicio_pie)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 9)
        self.verticalSpacer = QSpacerItem(20, 123, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.pie_arkinfo = QLabel(self.frame_inicio_pie)
        self.pie_arkinfo.setObjectName(u"pie_arkinfo")
        self.pie_arkinfo.setMinimumSize(QSize(40, 40))
        self.pie_arkinfo.setMaximumSize(QSize(16777215, 40))
        self.pie_arkinfo.setFont(font1)
        self.pie_arkinfo.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")
        self.pie_arkinfo.setFrameShadow(QFrame.Shadow.Sunken)
        self.pie_arkinfo.setTextFormat(Qt.TextFormat.PlainText)
        self.pie_arkinfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.pie_arkinfo)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 1)

        self.verticalLayout_13.addWidget(self.frame_inicio_pie)

        self.sw_consolas.addWidget(self.page_inicio)
        self.page_inf_hardware = QWidget()
        self.page_inf_hardware.setObjectName(u"page_inf_hardware")
        self.page_inf_hardware.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.page_inf_hardware)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.textEdit_info_hw = QTextEdit(self.page_inf_hardware)
        self.textEdit_info_hw.setObjectName(u"textEdit_info_hw")
        self.textEdit_info_hw.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")

        self.verticalLayout_8.addWidget(self.textEdit_info_hw)

        self.label_info_hw = QLabel(self.page_inf_hardware)
        self.label_info_hw.setObjectName(u"label_info_hw")
        self.label_info_hw.setMinimumSize(QSize(80, 80))
        self.label_info_hw.setMaximumSize(QSize(80, 80))
        self.label_info_hw.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_info_hw)

        self.sw_consolas.addWidget(self.page_inf_hardware)
        self.page_inf_config = QWidget()
        self.page_inf_config.setObjectName(u"page_inf_config")
        self.page_inf_config.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.page_inf_config)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_config = QFrame(self.page_inf_config)
        self.frame_config.setObjectName(u"frame_config")
        self.frame_config.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_config.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_config)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_btns_config = QFrame(self.frame_config)
        self.frame_btns_config.setObjectName(u"frame_btns_config")
        self.frame_btns_config.setMinimumSize(QSize(200, 0))
        self.frame_btns_config.setMaximumSize(QSize(200, 16777215))
        self.frame_btns_config.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}")
        self.frame_btns_config.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_btns_config.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_btns_config)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_cambio_regional = QPushButton(self.frame_btns_config)
        self.btn_cambio_regional.setObjectName(u"btn_cambio_regional")
        self.btn_cambio_regional.setMinimumSize(QSize(170, 90))
        self.btn_cambio_regional.setMaximumSize(QSize(170, 90))
        font2 = QFont()
        font2.setBold(True)
        self.btn_cambio_regional.setFont(font2)
        self.btn_cambio_regional.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px; /* Un padding uniforme puede ayudar a centrarlo */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center; /* Justifica el texto al centro */\n"
"}\n"
"\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.btn_cambio_regional.setIcon(icon8)
        self.btn_cambio_regional.setIconSize(QSize(35, 35))

        self.verticalLayout_12.addWidget(self.btn_cambio_regional)

        self.btn_config_sql_tools = QPushButton(self.frame_btns_config)
        self.btn_config_sql_tools.setObjectName(u"btn_config_sql_tools")
        self.btn_config_sql_tools.setMinimumSize(QSize(170, 90))
        self.btn_config_sql_tools.setMaximumSize(QSize(170, 90))
        self.btn_config_sql_tools.setFont(font2)
        self.btn_config_sql_tools.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px; /* Un padding uniforme puede ayudar a centrarlo */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center; /* Justifica el texto al centro */\n"
"}\n"
"\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon34 = QIcon()
        icon34.addFile(u"assets/icons/fi-sr-sql-server.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_config_sql_tools.setIcon(icon34)
        self.btn_config_sql_tools.setIconSize(QSize(35, 35))

        self.verticalLayout_12.addWidget(self.btn_config_sql_tools)

        self.btn_config_tools = QPushButton(self.frame_btns_config)
        self.btn_config_tools.setObjectName(u"btn_config_tools")
        self.btn_config_tools.setMinimumSize(QSize(170, 90))
        self.btn_config_tools.setMaximumSize(QSize(170, 90))
        self.btn_config_tools.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon35 = QIcon()
        icon35.addFile(u"assets/icons/filesettings_102180.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_config_tools.setIcon(icon35)
        self.btn_config_tools.setIconSize(QSize(35, 35))

        self.verticalLayout_12.addWidget(self.btn_config_tools)


        self.horizontalLayout_3.addWidget(self.frame_btns_config)

        self.textEdit_info_config = QTextEdit(self.frame_config)
        self.textEdit_info_config.setObjectName(u"textEdit_info_config")
        self.textEdit_info_config.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: rgb(170, 170, 127);")

        self.horizontalLayout_3.addWidget(self.textEdit_info_config)


        self.verticalLayout_7.addWidget(self.frame_config)

        self.frame_pie_config = QFrame(self.page_inf_config)
        self.frame_pie_config.setObjectName(u"frame_pie_config")
        self.frame_pie_config.setMinimumSize(QSize(0, 85))
        self.frame_pie_config.setMaximumSize(QSize(16777215, 85))
        self.frame_pie_config.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pie_config.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_pie_config)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_info_config = QLabel(self.frame_pie_config)
        self.label_info_config.setObjectName(u"label_info_config")
        self.label_info_config.setMinimumSize(QSize(40, 40))
        self.label_info_config.setMaximumSize(QSize(80, 80))
        self.label_info_config.setPixmap(QPixmap(u"C:/Users/juanep/.designer/backup/imagen/confi01.svg"))
        self.label_info_config.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.label_info_config)


        self.verticalLayout_7.addWidget(self.frame_pie_config)

        self.sw_consolas.addWidget(self.page_inf_config)
        self.page_inf_red = QWidget()
        self.page_inf_red.setObjectName(u"page_inf_red")
        self.page_inf_red.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.verticalLayout_9 = QVBoxLayout(self.page_inf_red)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.textEdit_info_red = QTextEdit(self.page_inf_red)
        self.textEdit_info_red.setObjectName(u"textEdit_info_red")
        self.textEdit_info_red.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")

        self.verticalLayout_9.addWidget(self.textEdit_info_red)

        self.label_info_red = QLabel(self.page_inf_red)
        self.label_info_red.setObjectName(u"label_info_red")
        self.label_info_red.setMinimumSize(QSize(40, 40))
        self.label_info_red.setMaximumSize(QSize(80, 80))
        self.label_info_red.setPixmap(QPixmap(u"C:/Users/juanep/.designer/backup/imagen/Red01.svg"))
        self.label_info_red.setScaledContents(True)
        self.label_info_red.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_info_red)

        self.sw_consolas.addWidget(self.page_inf_red)
        self.page_inf_so = QWidget()
        self.page_inf_so.setObjectName(u"page_inf_so")
        self.page_inf_so.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.page_inf_so)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.textEdit_info_so = QTextEdit(self.page_inf_so)
        self.textEdit_info_so.setObjectName(u"textEdit_info_so")
        self.textEdit_info_so.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")

        self.verticalLayout_11.addWidget(self.textEdit_info_so)

        self.label_info_so = QLabel(self.page_inf_so)
        self.label_info_so.setObjectName(u"label_info_so")
        self.label_info_so.setMinimumSize(QSize(40, 40))
        self.label_info_so.setMaximumSize(QSize(80, 80))
        self.label_info_so.setPixmap(QPixmap(u"C:/Users/juanep/.designer/backup/imagen/OS02.svg"))
        self.label_info_so.setScaledContents(True)
        self.label_info_so.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_info_so)

        self.sw_consolas.addWidget(self.page_inf_so)
        self.page_inf_regional = QWidget()
        self.page_inf_regional.setObjectName(u"page_inf_regional")
        self.page_inf_regional.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.page_inf_regional)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit_info_regional = QTextEdit(self.page_inf_regional)
        self.textEdit_info_regional.setObjectName(u"textEdit_info_regional")
        self.textEdit_info_regional.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")

        self.verticalLayout_10.addWidget(self.textEdit_info_regional)

        self.label_info_regional = QLabel(self.page_inf_regional)
        self.label_info_regional.setObjectName(u"label_info_regional")
        self.label_info_regional.setMinimumSize(QSize(80, 80))
        self.label_info_regional.setMaximumSize(QSize(80, 80))
        self.label_info_regional.setPixmap(QPixmap(u"C:/Users/juanep/.designer/backup/imagen/filesettings_102180.svg"))
        self.label_info_regional.setScaledContents(True)
        self.label_info_regional.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_info_regional)

        self.sw_consolas.addWidget(self.page_inf_regional)
        self.qsw_operaciones = QStackedWidget(self.frame_consolas)
        self.qsw_operaciones.setObjectName(u"qsw_operaciones")
        self.qsw_operaciones.setGeometry(QRect(1, 1, 750, 549))
        self.qsw_operaciones.setMinimumSize(QSize(750, 549))
        self.page_ark_company = QWidget()
        self.page_ark_company.setObjectName(u"page_ark_company")
        self.page_ark_company.setMinimumSize(QSize(790, 549))
        self.verticalLayout_20 = QVBoxLayout(self.page_ark_company)
        self.verticalLayout_20.setSpacing(1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(1, 1, 1, 1)
        self.frame_form_company = QFrame(self.page_ark_company)
        self.frame_form_company.setObjectName(u"frame_form_company")
        self.frame_form_company.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_form_company.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_form_company.setFrameShadow(QFrame.Shadow.Raised)
        self.label_titel_company = QLabel(self.frame_form_company)
        self.label_titel_company.setObjectName(u"label_titel_company")
        self.label_titel_company.setGeometry(QRect(280, 30, 141, 20))
        self.label_titel_company.setFrameShadow(QFrame.Shadow.Plain)
        self.label_titel_company.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.frame_form_company)

        self.frame_actbar_company = QFrame(self.page_ark_company)
        self.frame_actbar_company.setObjectName(u"frame_actbar_company")
        self.frame_actbar_company.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(0, 170, 255);\n"
"   \n"
"}")
        self.frame_actbar_company.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_actbar_company.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_20.addWidget(self.frame_actbar_company)

        self.verticalLayout_20.setStretch(0, 6)
        self.verticalLayout_20.setStretch(1, 1)
        self.qsw_operaciones.addWidget(self.page_ark_company)
        self.page_ark_categories = QWidget()
        self.page_ark_categories.setObjectName(u"page_ark_categories")
        self.page_ark_categories.setMinimumSize(QSize(790, 540))
        self.verticalLayout_18 = QVBoxLayout(self.page_ark_categories)
        self.verticalLayout_18.setSpacing(1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(1, 1, 1, 1)
        self.frame_form_categories = QFrame(self.page_ark_categories)
        self.frame_form_categories.setObjectName(u"frame_form_categories")
        self.frame_form_categories.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_form_categories.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_form_categories.setFrameShadow(QFrame.Shadow.Raised)
        self.label_titel_categories = QLabel(self.frame_form_categories)
        self.label_titel_categories.setObjectName(u"label_titel_categories")
        self.label_titel_categories.setGeometry(QRect(270, 30, 141, 20))
        self.label_titel_categories.setFrameShape(QFrame.Shape.Box)
        self.label_titel_categories.setFrameShadow(QFrame.Shadow.Plain)
        self.label_titel_categories.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.frame_form_categories)

        self.frame_actbar_categories = QFrame(self.page_ark_categories)
        self.frame_actbar_categories.setObjectName(u"frame_actbar_categories")
        self.frame_actbar_categories.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color:  rgb(0, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_actbar_categories.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_actbar_categories.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_18.addWidget(self.frame_actbar_categories)

        self.verticalLayout_18.setStretch(0, 6)
        self.verticalLayout_18.setStretch(1, 1)
        self.qsw_operaciones.addWidget(self.page_ark_categories)
        self.page_ark__units = QWidget()
        self.page_ark__units.setObjectName(u"page_ark__units")
        self.page_ark__units.setMinimumSize(QSize(800, 549))
        self.verticalLayout_4 = QVBoxLayout(self.page_ark__units)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.frame_form_units = QFrame(self.page_ark__units)
        self.frame_form_units.setObjectName(u"frame_form_units")
        self.frame_form_units.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_form_units.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_form_units.setFrameShadow(QFrame.Shadow.Raised)
        self.label_titel_units = QLabel(self.frame_form_units)
        self.label_titel_units.setObjectName(u"label_titel_units")
        self.label_titel_units.setGeometry(QRect(300, 30, 141, 20))
        self.label_titel_units.setFrameShadow(QFrame.Shadow.Plain)
        self.label_titel_units.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.frame_form_units)

        self.frame_actbar_units = QFrame(self.page_ark__units)
        self.frame_actbar_units.setObjectName(u"frame_actbar_units")
        self.frame_actbar_units.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(0, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_actbar_units.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_actbar_units.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_4.addWidget(self.frame_actbar_units)

        self.verticalLayout_4.setStretch(0, 6)
        self.verticalLayout_4.setStretch(1, 1)
        self.qsw_operaciones.addWidget(self.page_ark__units)
        self.page_ark_actions = QWidget()
        self.page_ark_actions.setObjectName(u"page_ark_actions")
        self.page_ark_actions.setMinimumSize(QSize(790, 549))
        self.verticalLayout_17 = QVBoxLayout(self.page_ark_actions)
        self.verticalLayout_17.setSpacing(1)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(1, 1, 1, 1)
        self.frame_form_actions = QFrame(self.page_ark_actions)
        self.frame_form_actions.setObjectName(u"frame_form_actions")
        self.frame_form_actions.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_form_actions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_form_actions.setFrameShadow(QFrame.Shadow.Raised)
        self.label_titel_actions = QLabel(self.frame_form_actions)
        self.label_titel_actions.setObjectName(u"label_titel_actions")
        self.label_titel_actions.setGeometry(QRect(360, 30, 49, 16))

        self.verticalLayout_17.addWidget(self.frame_form_actions)

        self.frame_actbar_actions = QFrame(self.page_ark_actions)
        self.frame_actbar_actions.setObjectName(u"frame_actbar_actions")
        self.frame_actbar_actions.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color:  rgb(0, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_actbar_actions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_actbar_actions.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_17.addWidget(self.frame_actbar_actions)

        self.verticalLayout_17.setStretch(0, 6)
        self.verticalLayout_17.setStretch(1, 1)
        self.qsw_operaciones.addWidget(self.page_ark_actions)
        self.page_ark_employees = QWidget()
        self.page_ark_employees.setObjectName(u"page_ark_employees")
        self.page_ark_employees.setMinimumSize(QSize(790, 549))
        self.verticalLayout_22 = QVBoxLayout(self.page_ark_employees)
        self.verticalLayout_22.setSpacing(1)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(1, 1, 1, 1)
        self.frame_form_employees = QFrame(self.page_ark_employees)
        self.frame_form_employees.setObjectName(u"frame_form_employees")
        self.frame_form_employees.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_form_employees.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_form_employees.setFrameShadow(QFrame.Shadow.Raised)
        self.label_titel_employees = QLabel(self.frame_form_employees)
        self.label_titel_employees.setObjectName(u"label_titel_employees")
        self.label_titel_employees.setGeometry(QRect(280, 40, 141, 20))
        self.label_titel_employees.setFrameShadow(QFrame.Shadow.Plain)
        self.label_titel_employees.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.frame_form_employees)

        self.frame_actbar_employees = QFrame(self.page_ark_employees)
        self.frame_actbar_employees.setObjectName(u"frame_actbar_employees")
        self.frame_actbar_employees.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(0, 170, 255);\n"
"   \n"
"}")
        self.frame_actbar_employees.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_actbar_employees.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_22.addWidget(self.frame_actbar_employees)

        self.verticalLayout_22.setStretch(0, 6)
        self.verticalLayout_22.setStretch(1, 1)
        self.qsw_operaciones.addWidget(self.page_ark_employees)
        self.page_ark_types = QWidget()
        self.page_ark_types.setObjectName(u"page_ark_types")
        self.page_ark_types.setMinimumSize(QSize(790, 549))
        self.verticalLayout_26 = QVBoxLayout(self.page_ark_types)
        self.verticalLayout_26.setSpacing(1)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(1, 1, 1, 1)
        self.frame_form_types = QFrame(self.page_ark_types)
        self.frame_form_types.setObjectName(u"frame_form_types")
        self.frame_form_types.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_form_types.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_form_types.setFrameShadow(QFrame.Shadow.Raised)
        self.label_titel_types = QLabel(self.frame_form_types)
        self.label_titel_types.setObjectName(u"label_titel_types")
        self.label_titel_types.setGeometry(QRect(280, 30, 141, 20))
        self.label_titel_types.setFrameShadow(QFrame.Shadow.Plain)
        self.label_titel_types.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.frame_form_types)

        self.frame_actbar_types = QFrame(self.page_ark_types)
        self.frame_actbar_types.setObjectName(u"frame_actbar_types")
        self.frame_actbar_types.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(0, 170, 255);\n"
"   \n"
"}")
        self.frame_actbar_types.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_actbar_types.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_26.addWidget(self.frame_actbar_types)

        self.verticalLayout_26.setStretch(0, 6)
        self.verticalLayout_26.setStretch(1, 1)
        self.qsw_operaciones.addWidget(self.page_ark_types)
        self.page_ark_it_assets = QWidget()
        self.page_ark_it_assets.setObjectName(u"page_ark_it_assets")
        self.page_ark_it_assets.setMinimumSize(QSize(790, 549))
        self.verticalLayout_23 = QVBoxLayout(self.page_ark_it_assets)
        self.verticalLayout_23.setSpacing(1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(1, 1, -1, 1)
        self.frame_form_it_assets = QFrame(self.page_ark_it_assets)
        self.frame_form_it_assets.setObjectName(u"frame_form_it_assets")
        self.frame_form_it_assets.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_form_it_assets.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_form_it_assets.setFrameShadow(QFrame.Shadow.Raised)
        self.label_titel_assets = QLabel(self.frame_form_it_assets)
        self.label_titel_assets.setObjectName(u"label_titel_assets")
        self.label_titel_assets.setGeometry(QRect(300, 30, 141, 20))
        self.label_titel_assets.setFrameShadow(QFrame.Shadow.Plain)
        self.label_titel_assets.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.frame_form_it_assets)

        self.frame_actbar_it_assets = QFrame(self.page_ark_it_assets)
        self.frame_actbar_it_assets.setObjectName(u"frame_actbar_it_assets")
        self.frame_actbar_it_assets.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(0, 170, 255);\n"
"   \n"
"}")
        self.frame_actbar_it_assets.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_actbar_it_assets.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_23.addWidget(self.frame_actbar_it_assets)

        self.verticalLayout_23.setStretch(0, 6)
        self.verticalLayout_23.setStretch(1, 1)
        self.qsw_operaciones.addWidget(self.page_ark_it_assets)
        self.page_ark_job_titles = QWidget()
        self.page_ark_job_titles.setObjectName(u"page_ark_job_titles")
        self.page_ark_job_titles.setMinimumSize(QSize(790, 549))
        self.verticalLayout_24 = QVBoxLayout(self.page_ark_job_titles)
        self.verticalLayout_24.setSpacing(1)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(1, 1, 1, 1)
        self.frame_form_job_titles = QFrame(self.page_ark_job_titles)
        self.frame_form_job_titles.setObjectName(u"frame_form_job_titles")
        self.frame_form_job_titles.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_form_job_titles.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_form_job_titles.setFrameShadow(QFrame.Shadow.Raised)
        self.label_titel_job_titles = QLabel(self.frame_form_job_titles)
        self.label_titel_job_titles.setObjectName(u"label_titel_job_titles")
        self.label_titel_job_titles.setGeometry(QRect(290, 30, 141, 20))
        self.label_titel_job_titles.setFrameShadow(QFrame.Shadow.Plain)
        self.label_titel_job_titles.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.frame_form_job_titles)

        self.frame_actbar_job_titles = QFrame(self.page_ark_job_titles)
        self.frame_actbar_job_titles.setObjectName(u"frame_actbar_job_titles")
        self.frame_actbar_job_titles.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(0, 170, 255);\n"
"   \n"
"}")
        self.frame_actbar_job_titles.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_actbar_job_titles.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_24.addWidget(self.frame_actbar_job_titles)

        self.verticalLayout_24.setStretch(0, 6)
        self.verticalLayout_24.setStretch(1, 1)
        self.qsw_operaciones.addWidget(self.page_ark_job_titles)
        self.page_ark_users = QWidget()
        self.page_ark_users.setObjectName(u"page_ark_users")
        self.page_ark_users.setMinimumSize(QSize(790, 549))
        self.verticalLayout_27 = QVBoxLayout(self.page_ark_users)
        self.verticalLayout_27.setSpacing(1)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(1, 1, 1, 1)
        self.frame_form_users = QFrame(self.page_ark_users)
        self.frame_form_users.setObjectName(u"frame_form_users")
        self.frame_form_users.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_form_users.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_form_users.setFrameShadow(QFrame.Shadow.Raised)
        self.label_titel_users = QLabel(self.frame_form_users)
        self.label_titel_users.setObjectName(u"label_titel_users")
        self.label_titel_users.setGeometry(QRect(290, 30, 141, 20))
        self.label_titel_users.setFrameShadow(QFrame.Shadow.Plain)
        self.label_titel_users.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.frame_form_users)

        self.frame_actbar_users = QFrame(self.page_ark_users)
        self.frame_actbar_users.setObjectName(u"frame_actbar_users")
        self.frame_actbar_users.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(0, 170, 255);\n"
"   \n"
"}")
        self.frame_actbar_users.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_actbar_users.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_27.addWidget(self.frame_actbar_users)

        self.verticalLayout_27.setStretch(0, 6)
        self.verticalLayout_27.setStretch(1, 1)
        self.qsw_operaciones.addWidget(self.page_ark_users)
        self.page_ark_sessions = QWidget()
        self.page_ark_sessions.setObjectName(u"page_ark_sessions")
        self.page_ark_sessions.setMinimumSize(QSize(790, 549))
        self.verticalLayout_25 = QVBoxLayout(self.page_ark_sessions)
        self.verticalLayout_25.setSpacing(1)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(1, 1, 1, 1)
        self.frame_form_sessions = QFrame(self.page_ark_sessions)
        self.frame_form_sessions.setObjectName(u"frame_form_sessions")
        self.frame_form_sessions.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_form_sessions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_form_sessions.setFrameShadow(QFrame.Shadow.Raised)
        self.label_titel_sessions = QLabel(self.frame_form_sessions)
        self.label_titel_sessions.setObjectName(u"label_titel_sessions")
        self.label_titel_sessions.setGeometry(QRect(280, 30, 141, 20))
        self.label_titel_sessions.setFrameShadow(QFrame.Shadow.Plain)
        self.label_titel_sessions.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.frame_form_sessions)

        self.frame_actbar_sessions = QFrame(self.page_ark_sessions)
        self.frame_actbar_sessions.setObjectName(u"frame_actbar_sessions")
        self.frame_actbar_sessions.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(0, 170, 255);\n"
"   \n"
"}")
        self.frame_actbar_sessions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_actbar_sessions.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_25.addWidget(self.frame_actbar_sessions)

        self.verticalLayout_25.setStretch(0, 6)
        self.verticalLayout_25.setStretch(1, 1)
        self.qsw_operaciones.addWidget(self.page_ark_sessions)
        self.page_ark_currencies = QWidget()
        self.page_ark_currencies.setObjectName(u"page_ark_currencies")
        self.page_ark_currencies.setMinimumSize(QSize(790, 549))
        self.verticalLayout_21 = QVBoxLayout(self.page_ark_currencies)
        self.verticalLayout_21.setSpacing(1)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(1, 1, 1, 1)
        self.frame_form_currencies = QFrame(self.page_ark_currencies)
        self.frame_form_currencies.setObjectName(u"frame_form_currencies")
        self.frame_form_currencies.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_form_currencies.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_form_currencies.setFrameShadow(QFrame.Shadow.Raised)
        self.label_titel_currencies = QLabel(self.frame_form_currencies)
        self.label_titel_currencies.setObjectName(u"label_titel_currencies")
        self.label_titel_currencies.setGeometry(QRect(280, 30, 141, 20))
        self.label_titel_currencies.setFrameShadow(QFrame.Shadow.Plain)
        self.label_titel_currencies.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.frame_form_currencies)

        self.frame_actbar_currencies = QFrame(self.page_ark_currencies)
        self.frame_actbar_currencies.setObjectName(u"frame_actbar_currencies")
        self.frame_actbar_currencies.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(0, 170, 255);\n"
"   \n"
"}")
        self.frame_actbar_currencies.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_actbar_currencies.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_21.addWidget(self.frame_actbar_currencies)

        self.verticalLayout_21.setStretch(0, 6)
        self.verticalLayout_21.setStretch(1, 1)
        self.qsw_operaciones.addWidget(self.page_ark_currencies)
        self.page_ark_clients = QWidget()
        self.page_ark_clients.setObjectName(u"page_ark_clients")
        self.page_ark_clients.setMinimumSize(QSize(790, 549))
        self.verticalLayout_19 = QVBoxLayout(self.page_ark_clients)
        self.verticalLayout_19.setSpacing(1)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(1, 1, 1, 1)
        self.frame_form_clients = QFrame(self.page_ark_clients)
        self.frame_form_clients.setObjectName(u"frame_form_clients")
        self.frame_form_clients.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_form_clients.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_form_clients.setFrameShadow(QFrame.Shadow.Raised)
        self.label_title_clients = QLabel(self.frame_form_clients)
        self.label_title_clients.setObjectName(u"label_title_clients")
        self.label_title_clients.setGeometry(QRect(280, 30, 141, 20))
        self.label_title_clients.setFrameShadow(QFrame.Shadow.Plain)
        self.label_title_clients.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.frame_form_clients)

        self.frame_actbar_clients = QFrame(self.page_ark_clients)
        self.frame_actbar_clients.setObjectName(u"frame_actbar_clients")
        self.frame_actbar_clients.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(0, 170, 255);\n"
"   \n"
"}")
        self.frame_actbar_clients.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_actbar_clients.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_19.addWidget(self.frame_actbar_clients)

        self.verticalLayout_19.setStretch(0, 6)
        self.verticalLayout_19.setStretch(1, 1)
        self.qsw_operaciones.addWidget(self.page_ark_clients)

        self.horizontalLayout.addWidget(self.frame_consolas)


        self.verticalLayout_2.addWidget(self.frame_inferior)


        self.verticalLayout.addWidget(self.frm_principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.sw_consolas.setCurrentIndex(0)
        self.qsw_operaciones.setCurrentIndex(8)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"     Men\u00fa", None))
        self.btn_minimizar.setText("")
        self.btn_restaurar.setText("")
        self.btn_maximizar.setText("")
        self.btn_cerrar.setText("")
        self.btn_info_hardware.setText(QCoreApplication.translate("MainWindow", u"      Hardware", None))
        self.btn_info_red.setText(QCoreApplication.translate("MainWindow", u"      Red", None))
        self.btn_info_so.setText(QCoreApplication.translate("MainWindow", u"      Sistema", None))
        self.btn_info_regional.setText(QCoreApplication.translate("MainWindow", u"      Regional", None))
#if QT_CONFIG(shortcut)
        self.btn_info_regional.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_limpiar.setText(QCoreApplication.translate("MainWindow", u"      Limpiar", None))
        self.btn_operations.setText(QCoreApplication.translate("MainWindow", u"  Operaciones", None))
        self.btn_config.setText(QCoreApplication.translate("MainWindow", u"  Configuraci\u00f3n", None))
#if QT_CONFIG(accessibility)
        self.frame_sub_hardware.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.btn_info_sistema.setText(QCoreApplication.translate("MainWindow", u"  Sistema", None))
        self.btn_info_mbd.setText(QCoreApplication.translate("MainWindow", u"      Motherboard", None))
        self.btn_info_cpu.setText(QCoreApplication.translate("MainWindow", u"      CPU", None))
#if QT_CONFIG(shortcut)
        self.btn_info_cpu.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_info_gpu.setText(QCoreApplication.translate("MainWindow", u"      GPU", None))
        self.btn_info_ram.setText(QCoreApplication.translate("MainWindow", u"      RAM", None))
        self.btn_info_hdd.setText(QCoreApplication.translate("MainWindow", u"      HDD-SSD", None))
        self.btn_info_nic.setText(QCoreApplication.translate("MainWindow", u"Tarjetas de Red", None))
        self.btn_info_audio.setText(QCoreApplication.translate("MainWindow", u"      Audio", None))
        self.btn_info_com.setText(QCoreApplication.translate("MainWindow", u"  Puertos COM", None))
        self.btn_info_usb.setText(QCoreApplication.translate("MainWindow", u"      USB", None))
        self.btn_info_bth.setText(QCoreApplication.translate("MainWindow", u"      Bluetooth", None))
        self.btn_regresar_menu.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa Principal", None))
        self.btn_ark_company.setText(QCoreApplication.translate("MainWindow", u"      Empresa", None))
        self.btn_ark_clients.setText(QCoreApplication.translate("MainWindow", u"      Clientes", None))
        self.btn_ark_ark_currencies.setText(QCoreApplication.translate("MainWindow", u"      Monedas", None))
        self.btn_ark_categories.setText(QCoreApplication.translate("MainWindow", u"    Categor\u00edas", None))
        self.btn_ark_functional_units.setText(QCoreApplication.translate("MainWindow", u" Unidades", None))
        self.btn_ark_actions.setText(QCoreApplication.translate("MainWindow", u"      Acciones", None))
        self.btn_ark_employees.setText(QCoreApplication.translate("MainWindow", u"      Empleados", None))
        self.btn_ark_device_types.setText(QCoreApplication.translate("MainWindow", u"      Tipos", None))
        self.btn_ark_it_assets.setText(QCoreApplication.translate("MainWindow", u"    Recursos", None))
        self.btn_ark_job_titles.setText(QCoreApplication.translate("MainWindow", u"   Profesiones", None))
        self.btn_ark_users.setText(QCoreApplication.translate("MainWindow", u"    Usuarios", None))
        self.btn_menu_ppal.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa Principal", None))
        self.title_arktoolspc.setText("")
        self.label_logo_tools.setText("")
        self.pie_arkinfo.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2025 Arksoft Integradores de Sistemas, C.A. RIF: J310994692 - Todos los derechos reservados\n"
"            Contacto: +58 424-3672111 | arksoft.sistemas@gmail.com", None))
        self.label_info_hw.setText("")
        self.btn_cambio_regional.setText(QCoreApplication.translate("MainWindow", u"  Cambiar \n"
"  Configuraci\u00f3n \n"
"  Regional", None))
        self.btn_config_sql_tools.setText(QCoreApplication.translate("MainWindow", u"  Consultar\n"
"  Conexi\u00f3n\n"
"  SQLite", None))
        self.btn_config_tools.setText(QCoreApplication.translate("MainWindow", u"  Consultar\n"
"  Configuraci\u00f3n\n"
"  Actual", None))
        self.label_info_config.setText("")
        self.label_info_red.setText("")
        self.label_info_so.setText("")
        self.label_info_regional.setText("")
        self.label_titel_company.setText(QCoreApplication.translate("MainWindow", u"EMPRESA", None))
        self.label_titel_categories.setText(QCoreApplication.translate("MainWindow", u"CATEGORIAS", None))
        self.label_titel_units.setText(QCoreApplication.translate("MainWindow", u"UNIDADES FUNCIONALES", None))
        self.label_titel_actions.setText(QCoreApplication.translate("MainWindow", u"ACCIONES", None))
        self.label_titel_employees.setText(QCoreApplication.translate("MainWindow", u"EMPLEADOS", None))
        self.label_titel_types.setText(QCoreApplication.translate("MainWindow", u"TIPOS", None))
        self.label_titel_assets.setText(QCoreApplication.translate("MainWindow", u"RECURSOS", None))
        self.label_titel_job_titles.setText(QCoreApplication.translate("MainWindow", u"PROFESIONES", None))
        self.label_titel_users.setText(QCoreApplication.translate("MainWindow", u"USUARIOS", None))
        self.label_titel_sessions.setText(QCoreApplication.translate("MainWindow", u"SESIONES", None))
        self.label_titel_currencies.setText(QCoreApplication.translate("MainWindow", u"MONEDAS", None))
        self.label_title_clients.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
    # retranslateUi

