# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arktoolspcg2iEJCiw.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QTimeEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindow.resize(825, 613)
        MainWindow.setMinimumSize(QSize(825, 544))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(825, 544))
        self.centralwidget.setMaximumSize(QSize(1980, 1080))
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frm_principal = QFrame(self.centralwidget)
        self.frm_principal.setObjectName(u"frm_principal")
        self.frm_principal.setMaximumSize(QSize(1980, 1080))
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
        self.hly_frame_superior = QHBoxLayout(self.frame_superior)
        self.hly_frame_superior.setSpacing(2)
        self.hly_frame_superior.setObjectName(u"hly_frame_superior")
        self.hly_frame_superior.setContentsMargins(2, 2, 2, 2)
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
        icon.addFile(u":/rec/assets/icons/fi-sr-rectangle-list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(28, 28))

        self.hly_frame_superior.addWidget(self.btn_menu)

        self.horizontalSpacer = QSpacerItem(439, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hly_frame_superior.addItem(self.horizontalSpacer)

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
        icon1.addFile(u":/rec/assets/icons/fi-sr-arrow-down-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_minimizar.setIcon(icon1)
        self.btn_minimizar.setIconSize(QSize(24, 24))

        self.hly_frame_superior.addWidget(self.btn_minimizar)

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
        icon2.addFile(u":/rec/assets/icons/fi-sr-expand.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_restaurar.setIcon(icon2)
        self.btn_restaurar.setIconSize(QSize(24, 24))

        self.hly_frame_superior.addWidget(self.btn_restaurar)

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
        icon3.addFile(u":/rec/assets/icons/fi-sr-expand-arrows.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_maximizar.setIcon(icon3)
        self.btn_maximizar.setIconSize(QSize(24, 24))

        self.hly_frame_superior.addWidget(self.btn_maximizar)

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
        icon4.addFile(u":/rec/assets/icons/fi-sr-cross-small.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cerrar.setIcon(icon4)
        self.btn_cerrar.setIconSize(QSize(35, 35))

        self.hly_frame_superior.addWidget(self.btn_cerrar)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.frm_principal)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setMinimumSize(QSize(825, 544))
        self.frame_inferior.setMaximumSize(QSize(1980, 1080))
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
        self.frame_menu.setEnabled(True)
        self.frame_menu.setMinimumSize(QSize(0, 0))
        self.frame_menu.setMaximumSize(QSize(0, 16777215))
        self.frame_menu.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}")
        self.frame_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frame_menu = QVBoxLayout(self.frame_menu)
        self.vly_frame_menu.setObjectName(u"vly_frame_menu")
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
        icon5.addFile(u":/rec/assets/icons/PC01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_hardware.setIcon(icon5)
        self.btn_info_hardware.setIconSize(QSize(35, 35))

        self.vly_frame_menu.addWidget(self.btn_info_hardware)

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
        icon6.addFile(u":/rec/assets/icons/Red01.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_red.setIcon(icon6)
        self.btn_info_red.setIconSize(QSize(35, 35))

        self.vly_frame_menu.addWidget(self.btn_info_red)

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
        icon7.addFile(u":/rec/assets/icons/fi-sr-computer-classic.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_so.setIcon(icon7)
        self.btn_info_so.setIconSize(QSize(35, 36))

        self.vly_frame_menu.addWidget(self.btn_info_so)

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
        icon8.addFile(u":/rec/assets/icons/Regional01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_regional.setIcon(icon8)
        self.btn_info_regional.setIconSize(QSize(35, 35))

        self.vly_frame_menu.addWidget(self.btn_info_regional)

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
        icon9.addFile(u":/rec/assets/icons/Clear01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_limpiar.setIcon(icon9)
        self.btn_limpiar.setIconSize(QSize(35, 35))

        self.vly_frame_menu.addWidget(self.btn_limpiar)

        self.verticalSpacer_3 = QSpacerItem(20, 106, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vly_frame_menu.addItem(self.verticalSpacer_3)

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
        icon10.addFile(u":/rec/assets/icons/filesettings_102180.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_operations.setIcon(icon10)
        self.btn_operations.setIconSize(QSize(28, 29))

        self.vly_frame_menu.addWidget(self.btn_operations)

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
        icon11.addFile(u":/rec/assets/icons/fi-sr-settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_config.setIcon(icon11)
        self.btn_config.setIconSize(QSize(35, 35))

        self.vly_frame_menu.addWidget(self.btn_config)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.frame_sub_hardware = QFrame(self.frame_inferior)
        self.frame_sub_hardware.setObjectName(u"frame_sub_hardware")
        self.frame_sub_hardware.setEnabled(True)
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
        self.vly_frame_sub_hardware = QVBoxLayout(self.frame_sub_hardware)
        self.vly_frame_sub_hardware.setObjectName(u"vly_frame_sub_hardware")
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
        icon12 = QIcon()
        icon12.addFile(u":/rec/assets/icons/sys01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_sistema.setIcon(icon12)
        self.btn_info_sistema.setIconSize(QSize(35, 35))

        self.vly_frame_sub_hardware.addWidget(self.btn_info_sistema)

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
        icon13 = QIcon()
        icon13.addFile(u":/rec/assets/icons/mbd_01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_mbd.setIcon(icon13)
        self.btn_info_mbd.setIconSize(QSize(28, 29))

        self.vly_frame_sub_hardware.addWidget(self.btn_info_mbd)

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
        icon14 = QIcon()
        icon14.addFile(u":/rec/assets/icons/cpu01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_cpu.setIcon(icon14)
        self.btn_info_cpu.setIconSize(QSize(28, 28))

        self.vly_frame_sub_hardware.addWidget(self.btn_info_cpu)

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
        icon15 = QIcon()
        icon15.addFile(u":/rec/assets/icons/Grafica01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_gpu.setIcon(icon15)
        self.btn_info_gpu.setIconSize(QSize(28, 28))

        self.vly_frame_sub_hardware.addWidget(self.btn_info_gpu)

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
        icon16 = QIcon()
        icon16.addFile(u":/rec/assets/icons/RAM.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_ram.setIcon(icon16)
        self.btn_info_ram.setIconSize(QSize(28, 28))

        self.vly_frame_sub_hardware.addWidget(self.btn_info_ram)

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
        icon17 = QIcon()
        icon17.addFile(u":/rec/assets/icons/hdd2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_hdd.setIcon(icon17)
        self.btn_info_hdd.setIconSize(QSize(28, 28))

        self.vly_frame_sub_hardware.addWidget(self.btn_info_hdd)

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
        icon18 = QIcon()
        icon18.addFile(u":/rec/assets/icons/nic01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_nic.setIcon(icon18)
        self.btn_info_nic.setIconSize(QSize(28, 28))

        self.vly_frame_sub_hardware.addWidget(self.btn_info_nic)

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
        icon19 = QIcon()
        icon19.addFile(u":/rec/assets/icons/audio01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_audio.setIcon(icon19)
        self.btn_info_audio.setIconSize(QSize(28, 28))

        self.vly_frame_sub_hardware.addWidget(self.btn_info_audio)

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
        icon20 = QIcon()
        icon20.addFile(u":/rec/assets/icons/com02.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_com.setIcon(icon20)
        self.btn_info_com.setIconSize(QSize(35, 35))

        self.vly_frame_sub_hardware.addWidget(self.btn_info_com)

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
        icon21 = QIcon()
        icon21.addFile(u":/rec/assets/icons/usb1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_usb.setIcon(icon21)
        self.btn_info_usb.setIconSize(QSize(28, 28))

        self.vly_frame_sub_hardware.addWidget(self.btn_info_usb)

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
        icon22 = QIcon()
        icon22.addFile(u":/rec/assets/icons/bluetooth02.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_bth.setIcon(icon22)
        self.btn_info_bth.setIconSize(QSize(28, 28))

        self.vly_frame_sub_hardware.addWidget(self.btn_info_bth)

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
        icon23 = QIcon()
        icon23.addFile(u":/rec/assets/icons/fi-sr-angle-double-small-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_regresar_menu.setIcon(icon23)
        self.btn_regresar_menu.setIconSize(QSize(35, 35))

        self.vly_frame_sub_hardware.addWidget(self.btn_regresar_menu)


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
        self.frame_operations.setFrameShadow(QFrame.Shadow.Sunken)
        self.vly_frame_operations = QVBoxLayout(self.frame_operations)
        self.vly_frame_operations.setObjectName(u"vly_frame_operations")
        self.btn_ark_company = QPushButton(self.frame_operations)
        self.btn_ark_company.setObjectName(u"btn_ark_company")
        self.btn_ark_company.setMinimumSize(QSize(0, 32))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setBold(True)
        font1.setKerning(False)
        self.btn_ark_company.setFont(font1)
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
"    font-size: 12px;\n"
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
        icon24 = QIcon()
        icon24.addFile(u":/rec/assets/icons/fi-sr-home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_company.setIcon(icon24)
        self.btn_ark_company.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_ark_company)

        self.btn_ark_clients = QPushButton(self.frame_operations)
        self.btn_ark_clients.setObjectName(u"btn_ark_clients")
        self.btn_ark_clients.setMinimumSize(QSize(0, 32))
        self.btn_ark_clients.setFont(font1)
        self.btn_ark_clients.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
"    font-size: 12px;\n"
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
        icon25.addFile(u":/rec/assets/icons/fi-sr-person-shelter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_clients.setIcon(icon25)
        self.btn_ark_clients.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_ark_clients)

        self.btn_ark_currencies = QPushButton(self.frame_operations)
        self.btn_ark_currencies.setObjectName(u"btn_ark_currencies")
        self.btn_ark_currencies.setMinimumSize(QSize(0, 32))
        self.btn_ark_currencies.setFont(font1)
        self.btn_ark_currencies.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
"    font-size: 12px;\n"
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
        icon26.addFile(u":/rec/assets/icons/fi-sr-currency.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_currencies.setIcon(icon26)
        self.btn_ark_currencies.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_ark_currencies)

        self.btn_ark_categories = QPushButton(self.frame_operations)
        self.btn_ark_categories.setObjectName(u"btn_ark_categories")
        self.btn_ark_categories.setMinimumSize(QSize(0, 32))
        self.btn_ark_categories.setFont(font1)
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
"    font-size: 12px;\n"
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
        icon27.addFile(u":/rec/assets/icons/fi-sr-category-alt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_categories.setIcon(icon27)
        self.btn_ark_categories.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_ark_categories)

        self.btn_ark_functional_units = QPushButton(self.frame_operations)
        self.btn_ark_functional_units.setObjectName(u"btn_ark_functional_units")
        self.btn_ark_functional_units.setMinimumSize(QSize(0, 32))
        self.btn_ark_functional_units.setFont(font1)
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
"    font-size: 12px;\n"
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
        icon28.addFile(u":/rec/assets/icons/fi-sr-department-structure.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_functional_units.setIcon(icon28)
        self.btn_ark_functional_units.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_ark_functional_units)

        self.btn_ark_actions = QPushButton(self.frame_operations)
        self.btn_ark_actions.setObjectName(u"btn_ark_actions")
        self.btn_ark_actions.setMinimumSize(QSize(0, 32))
        self.btn_ark_actions.setFont(font1)
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
"    font-size: 12px;\n"
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
        icon29.addFile(u":/rec/assets/icons/fi-sr-tasks.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_actions.setIcon(icon29)
        self.btn_ark_actions.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_ark_actions)

        self.btn_ark_employees = QPushButton(self.frame_operations)
        self.btn_ark_employees.setObjectName(u"btn_ark_employees")
        self.btn_ark_employees.setMinimumSize(QSize(0, 32))
        self.btn_ark_employees.setFont(font1)
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
"    font-size: 12px;\n"
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
        icon30.addFile(u":/rec/assets/icons/fi-sr-employee-man-alt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_employees.setIcon(icon30)
        self.btn_ark_employees.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_ark_employees)

        self.btn_ark_device_types = QPushButton(self.frame_operations)
        self.btn_ark_device_types.setObjectName(u"btn_ark_device_types")
        self.btn_ark_device_types.setMinimumSize(QSize(0, 32))
        self.btn_ark_device_types.setFont(font1)
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
"    font-size: 12px;\n"
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
        icon31.addFile(u":/rec/assets/icons/fi-sr-list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_device_types.setIcon(icon31)
        self.btn_ark_device_types.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_ark_device_types)

        self.btn_ark_it_assets = QPushButton(self.frame_operations)
        self.btn_ark_it_assets.setObjectName(u"btn_ark_it_assets")
        self.btn_ark_it_assets.setMinimumSize(QSize(0, 32))
        self.btn_ark_it_assets.setFont(font1)
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
"    font-size: 12px;\n"
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
        icon32.addFile(u":/rec/assets/icons/fi-sr-resources.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_it_assets.setIcon(icon32)
        self.btn_ark_it_assets.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_ark_it_assets)

        self.btn_ark_job_titles = QPushButton(self.frame_operations)
        self.btn_ark_job_titles.setObjectName(u"btn_ark_job_titles")
        self.btn_ark_job_titles.setMinimumSize(QSize(0, 32))
        self.btn_ark_job_titles.setFont(font1)
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
"    font-size: 12px;\n"
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
        icon33.addFile(u":/rec/assets/icons/fi-sr-person-chalkboard.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_job_titles.setIcon(icon33)
        self.btn_ark_job_titles.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_ark_job_titles)

        self.btn_ark_requests = QPushButton(self.frame_operations)
        self.btn_ark_requests.setObjectName(u"btn_ark_requests")
        self.btn_ark_requests.setMinimumSize(QSize(0, 32))
        self.btn_ark_requests.setFont(font1)
        self.btn_ark_requests.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
"    font-size: 12px;\n"
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
        icon34 = QIcon()
        icon34.addFile(u":/rec/assets/icons/fi-sr-code-pull-request.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_requests.setIcon(icon34)
        self.btn_ark_requests.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_ark_requests)

        self.btn_ark_sessions = QPushButton(self.frame_operations)
        self.btn_ark_sessions.setObjectName(u"btn_ark_sessions")
        self.btn_ark_sessions.setMinimumSize(QSize(0, 32))
        self.btn_ark_sessions.setFont(font1)
        self.btn_ark_sessions.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
"    font-size: 12px;\n"
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
        self.btn_ark_sessions.setIcon(icon29)
        self.btn_ark_sessions.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_ark_sessions)

        self.btn_ark_users = QPushButton(self.frame_operations)
        self.btn_ark_users.setObjectName(u"btn_ark_users")
        self.btn_ark_users.setMinimumSize(QSize(0, 32))
        self.btn_ark_users.setFont(font1)
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
"    font-size: 12px;\n"
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
        icon35 = QIcon()
        icon35.addFile(u":/rec/assets/icons/fi-sr-person-simple.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_users.setIcon(icon35)
        self.btn_ark_users.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_ark_users)

        self.btn_menu_ppal = QPushButton(self.frame_operations)
        self.btn_menu_ppal.setObjectName(u"btn_menu_ppal")
        self.btn_menu_ppal.setMinimumSize(QSize(0, 32))
        self.btn_menu_ppal.setFont(font1)
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
"    font-size: 12px;\n"
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
        self.btn_menu_ppal.setIcon(icon23)
        self.btn_menu_ppal.setIconSize(QSize(18, 18))

        self.vly_frame_operations.addWidget(self.btn_menu_ppal)


        self.horizontalLayout.addWidget(self.frame_operations)

        self.frame_consolas = QFrame(self.frame_inferior)
        self.frame_consolas.setObjectName(u"frame_consolas")
        self.frame_consolas.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_consolas.sizePolicy().hasHeightForWidth())
        self.frame_consolas.setSizePolicy(sizePolicy)
        self.frame_consolas.setMinimumSize(QSize(825, 544))
        self.frame_consolas.setMaximumSize(QSize(1920, 1080))
        self.frame_consolas.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"   \n"
"}")
        self.frame_consolas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_consolas.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frame_consolas = QVBoxLayout(self.frame_consolas)
        self.vly_frame_consolas.setSpacing(0)
        self.vly_frame_consolas.setObjectName(u"vly_frame_consolas")
        self.vly_frame_consolas.setContentsMargins(0, 0, 0, 0)
        self.sw_consolas = QStackedWidget(self.frame_consolas)
        self.sw_consolas.setObjectName(u"sw_consolas")
        self.sw_consolas.setEnabled(True)
        sizePolicy.setHeightForWidth(self.sw_consolas.sizePolicy().hasHeightForWidth())
        self.sw_consolas.setSizePolicy(sizePolicy)
        self.sw_consolas.setMinimumSize(QSize(825, 544))
        self.sw_consolas.setMaximumSize(QSize(1920, 1080))
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
        self.vly_page_inicio = QVBoxLayout(self.page_inicio)
        self.vly_page_inicio.setSpacing(0)
        self.vly_page_inicio.setObjectName(u"vly_page_inicio")
        self.vly_page_inicio.setContentsMargins(0, 0, 0, 0)
        self.frame_inicio_head = QFrame(self.page_inicio)
        self.frame_inicio_head.setObjectName(u"frame_inicio_head")
        self.frame_inicio_head.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_inicio_head.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frame_inicio_head = QVBoxLayout(self.frame_inicio_head)
        self.vly_frame_inicio_head.setObjectName(u"vly_frame_inicio_head")
        self.title_arktoolspc = QLabel(self.frame_inicio_head)
        self.title_arktoolspc.setObjectName(u"title_arktoolspc")
        self.title_arktoolspc.setEnabled(True)
        self.title_arktoolspc.setMinimumSize(QSize(40, 60))
        self.title_arktoolspc.setMaximumSize(QSize(1980, 40))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        self.title_arktoolspc.setFont(font2)
        self.title_arktoolspc.setStyleSheet(u"")
        self.title_arktoolspc.setFrameShadow(QFrame.Shadow.Sunken)
        self.title_arktoolspc.setTextFormat(Qt.TextFormat.PlainText)
        self.title_arktoolspc.setPixmap(QPixmap(u":/rec/assets/images/ArlToolsPC2.png"))
        self.title_arktoolspc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vly_frame_inicio_head.addWidget(self.title_arktoolspc)

        self.verticalSpacer_2 = QSpacerItem(20, 94, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vly_frame_inicio_head.addItem(self.verticalSpacer_2)


        self.vly_page_inicio.addWidget(self.frame_inicio_head)

        self.frame_inicio_middle = QFrame(self.page_inicio)
        self.frame_inicio_middle.setObjectName(u"frame_inicio_middle")
        self.frame_inicio_middle.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_inicio_middle.setFrameShadow(QFrame.Shadow.Plain)
        self.hly_frame_inicio_middle = QHBoxLayout(self.frame_inicio_middle)
        self.hly_frame_inicio_middle.setSpacing(1)
        self.hly_frame_inicio_middle.setObjectName(u"hly_frame_inicio_middle")
        self.hly_frame_inicio_middle.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(248, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hly_frame_inicio_middle.addItem(self.horizontalSpacer_2)

        self.label_logo_tools = QLabel(self.frame_inicio_middle)
        self.label_logo_tools.setObjectName(u"label_logo_tools")
        self.label_logo_tools.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_logo_tools.sizePolicy().hasHeightForWidth())
        self.label_logo_tools.setSizePolicy(sizePolicy1)
        self.label_logo_tools.setMinimumSize(QSize(164, 164))
        self.label_logo_tools.setMaximumSize(QSize(200, 200))
        self.label_logo_tools.setAutoFillBackground(False)
        self.label_logo_tools.setStyleSheet(u"")
        self.label_logo_tools.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_logo_tools.setPixmap(QPixmap(u":/rec/assets/images/ArkToolsPC_02.png"))
        self.label_logo_tools.setScaledContents(True)
        self.label_logo_tools.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hly_frame_inicio_middle.addWidget(self.label_logo_tools)

        self.horizontalSpacer_3 = QSpacerItem(248, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hly_frame_inicio_middle.addItem(self.horizontalSpacer_3)


        self.vly_page_inicio.addWidget(self.frame_inicio_middle)

        self.frame_inicio_pie = QFrame(self.page_inicio)
        self.frame_inicio_pie.setObjectName(u"frame_inicio_pie")
        self.frame_inicio_pie.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_inicio_pie.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frame_inicio_pie = QVBoxLayout(self.frame_inicio_pie)
        self.vly_frame_inicio_pie.setSpacing(6)
        self.vly_frame_inicio_pie.setObjectName(u"vly_frame_inicio_pie")
        self.vly_frame_inicio_pie.setContentsMargins(0, 0, 0, 9)
        self.verticalSpacer = QSpacerItem(20, 123, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vly_frame_inicio_pie.addItem(self.verticalSpacer)

        self.pie_arkinfo = QLabel(self.frame_inicio_pie)
        self.pie_arkinfo.setObjectName(u"pie_arkinfo")
        self.pie_arkinfo.setMinimumSize(QSize(40, 40))
        self.pie_arkinfo.setMaximumSize(QSize(16777215, 40))
        self.pie_arkinfo.setFont(font2)
        self.pie_arkinfo.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")
        self.pie_arkinfo.setFrameShadow(QFrame.Shadow.Sunken)
        self.pie_arkinfo.setTextFormat(Qt.TextFormat.PlainText)
        self.pie_arkinfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vly_frame_inicio_pie.addWidget(self.pie_arkinfo)

        self.vly_frame_inicio_pie.setStretch(0, 1)
        self.vly_frame_inicio_pie.setStretch(1, 1)

        self.vly_page_inicio.addWidget(self.frame_inicio_pie)

        self.vly_page_inicio.setStretch(0, 1)
        self.vly_page_inicio.setStretch(1, 1)
        self.vly_page_inicio.setStretch(2, 1)
        self.sw_consolas.addWidget(self.page_inicio)
        self.page_inf_hardware = QWidget()
        self.page_inf_hardware.setObjectName(u"page_inf_hardware")
        self.page_inf_hardware.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.vly_page_inf_hardware = QVBoxLayout(self.page_inf_hardware)
        self.vly_page_inf_hardware.setObjectName(u"vly_page_inf_hardware")
        self.textEdit_info_hw = QTextEdit(self.page_inf_hardware)
        self.textEdit_info_hw.setObjectName(u"textEdit_info_hw")
        self.textEdit_info_hw.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")

        self.vly_page_inf_hardware.addWidget(self.textEdit_info_hw)

        self.label_info_hw = QLabel(self.page_inf_hardware)
        self.label_info_hw.setObjectName(u"label_info_hw")
        self.label_info_hw.setMinimumSize(QSize(80, 80))
        self.label_info_hw.setMaximumSize(QSize(80, 80))
        self.label_info_hw.setPixmap(QPixmap(u":/rec/assets/icons/sys01.svg"))
        self.label_info_hw.setScaledContents(True)

        self.vly_page_inf_hardware.addWidget(self.label_info_hw)

        self.sw_consolas.addWidget(self.page_inf_hardware)
        self.page_inf_config = QWidget()
        self.page_inf_config.setObjectName(u"page_inf_config")
        self.page_inf_config.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.vly_page_inf_config = QVBoxLayout(self.page_inf_config)
        self.vly_page_inf_config.setObjectName(u"vly_page_inf_config")
        self.frame_config = QFrame(self.page_inf_config)
        self.frame_config.setObjectName(u"frame_config")
        self.frame_config.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_config.setFrameShadow(QFrame.Shadow.Raised)
        self.hly_frame_config = QHBoxLayout(self.frame_config)
        self.hly_frame_config.setSpacing(0)
        self.hly_frame_config.setObjectName(u"hly_frame_config")
        self.hly_frame_config.setContentsMargins(0, 0, 0, 0)
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
        self.vly_frame_btns_config = QVBoxLayout(self.frame_btns_config)
        self.vly_frame_btns_config.setObjectName(u"vly_frame_btns_config")
        self.btn_cambio_regional = QPushButton(self.frame_btns_config)
        self.btn_cambio_regional.setObjectName(u"btn_cambio_regional")
        self.btn_cambio_regional.setMinimumSize(QSize(170, 90))
        self.btn_cambio_regional.setMaximumSize(QSize(170, 90))
        font3 = QFont()
        font3.setBold(True)
        self.btn_cambio_regional.setFont(font3)
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

        self.vly_frame_btns_config.addWidget(self.btn_cambio_regional)

        self.btn_config_sql_tools = QPushButton(self.frame_btns_config)
        self.btn_config_sql_tools.setObjectName(u"btn_config_sql_tools")
        self.btn_config_sql_tools.setMinimumSize(QSize(170, 90))
        self.btn_config_sql_tools.setMaximumSize(QSize(170, 90))
        self.btn_config_sql_tools.setFont(font3)
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
        icon36 = QIcon()
        icon36.addFile(u":/rec/assets/icons/fi-sr-sql-server.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_config_sql_tools.setIcon(icon36)
        self.btn_config_sql_tools.setIconSize(QSize(35, 35))

        self.vly_frame_btns_config.addWidget(self.btn_config_sql_tools)

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
        self.btn_config_tools.setIcon(icon10)
        self.btn_config_tools.setIconSize(QSize(35, 35))

        self.vly_frame_btns_config.addWidget(self.btn_config_tools)


        self.hly_frame_config.addWidget(self.frame_btns_config)

        self.textEdit_info_config = QTextEdit(self.frame_config)
        self.textEdit_info_config.setObjectName(u"textEdit_info_config")
        self.textEdit_info_config.setEnabled(False)
        self.textEdit_info_config.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.textEdit_info_config.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: rgb(170, 170, 127);")

        self.hly_frame_config.addWidget(self.textEdit_info_config)


        self.vly_page_inf_config.addWidget(self.frame_config)

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
        self.label_info_config.setPixmap(QPixmap(u":/rec/assets/icons/confi01.svg"))
        self.label_info_config.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.label_info_config)


        self.vly_page_inf_config.addWidget(self.frame_pie_config)

        self.sw_consolas.addWidget(self.page_inf_config)
        self.page_forms = QWidget()
        self.page_forms.setObjectName(u"page_forms")
        sizePolicy.setHeightForWidth(self.page_forms.sizePolicy().hasHeightForWidth())
        self.page_forms.setSizePolicy(sizePolicy)
        self.page_forms.setMinimumSize(QSize(825, 544))
        self.page_forms.setMaximumSize(QSize(1920, 1080))
        self.page_forms.setStyleSheet(u"")
        self.hly_page_forms = QHBoxLayout(self.page_forms)
        self.hly_page_forms.setSpacing(4)
        self.hly_page_forms.setObjectName(u"hly_page_forms")
        self.hly_page_forms.setContentsMargins(0, 0, 0, 0)
        self.qsw_forms = QStackedWidget(self.page_forms)
        self.qsw_forms.setObjectName(u"qsw_forms")
        sizePolicy.setHeightForWidth(self.qsw_forms.sizePolicy().hasHeightForWidth())
        self.qsw_forms.setSizePolicy(sizePolicy)
        self.qsw_forms.setMinimumSize(QSize(825, 544))
        self.qsw_forms.setMaximumSize(QSize(1920, 1080))
        self.qsw_forms.setStyleSheet(u"   font: 9pt \"Consolas\";\n"
"  color: #000000; \n"
"   background-color: rgb(19, 255, 168)\n"
"")
        self.page_frm_currencies = QWidget()
        self.page_frm_currencies.setObjectName(u"page_frm_currencies")
        sizePolicy.setHeightForWidth(self.page_frm_currencies.sizePolicy().hasHeightForWidth())
        self.page_frm_currencies.setSizePolicy(sizePolicy)
        self.page_frm_currencies.setMinimumSize(QSize(825, 544))
        self.page_frm_currencies.setMaximumSize(QSize(1920, 1080))
        self.page_frm_currencies.setStyleSheet(u"")
        self.hly_frm_currencies = QHBoxLayout(self.page_frm_currencies)
        self.hly_frm_currencies.setSpacing(0)
        self.hly_frm_currencies.setObjectName(u"hly_frm_currencies")
        self.hly_frm_currencies.setContentsMargins(0, 0, 0, 0)
        self.frm_form_currencies = QFrame(self.page_frm_currencies)
        self.frm_form_currencies.setObjectName(u"frm_form_currencies")
        sizePolicy.setHeightForWidth(self.frm_form_currencies.sizePolicy().hasHeightForWidth())
        self.frm_form_currencies.setSizePolicy(sizePolicy)
        self.frm_form_currencies.setMinimumSize(QSize(625, 0))
        self.frm_form_currencies.setMaximumSize(QSize(1920, 1080))
        self.frm_form_currencies.setFont(font2)
        self.frm_form_currencies.setStyleSheet(u"")
        self.frm_form_currencies.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_currencies.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frm_form_currencies)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.frm_currencies = QFrame(self.frm_form_currencies)
        self.frm_currencies.setObjectName(u"frm_currencies")
        sizePolicy.setHeightForWidth(self.frm_currencies.sizePolicy().hasHeightForWidth())
        self.frm_currencies.setSizePolicy(sizePolicy)
        self.frm_currencies.setMinimumSize(QSize(625, 433))
        self.frm_currencies.setMaximumSize(QSize(625, 433))
        self.frm_currencies.setStyleSheet(u"/* Estilos para la seccion de formularios */\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del marco */\n"
"QGroupBox {\n"
"    background-color: rgb(188, 246, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    color: #000000;                  /* Color del texto */\n"
"    font: bold 24pt \"Segoe UI\";     /* Fuente m\u00e1s grande y en negrita */\n"
"    subcontrol-origin: margin;      /* Posici\u00f3n del t\u00edtulo */\n"
"    subcontrol-position: top left;  /* Alineaci\u00f3n del t\u00edtulo */\n"
"    padding: 4px;                   /* Espacio alrededor del texto */\n"
"}\n"
"\n"
"/* Estilo de las etiquetas */\n"
"QLabel {\n"
"    color: #000000;                /* Color del texto */\n"
"    background-color: rgb(188, 246, 255); /* Opcional: fondo */\n"
"    font: 10pt \"Segoe UI\";        "
                        " /* Fuente de Etiquetas */\n"
"    line-height: 12px;\n"
"}\n"
"\n"
"/* Estilo de QTextEdit */\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QLineEdit */\n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Co"
                        "lor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QComboBox */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* Estilo de QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas r"
                        "edondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
"QComboBox:disabled, \n"
"QDateEdit:disabled, \n"
"QTimeEdit:disabled {\n"
"    background-color: #e1e1e1;\n"
"    color: #808080;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"\n"
"/* Forzamos el QTextEdit */\n"
"QTextEdit:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"/* Forzamos el QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_currencies.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_currencies.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_currencies = QVBoxLayout(self.frm_currencies)
        self.vly_frm_currencies.setSpacing(2)
        self.vly_frm_currencies.setObjectName(u"vly_frm_currencies")
        self.vly_frm_currencies.setContentsMargins(4, 4, 4, 4)
        self.grb_currencies = QGroupBox(self.frm_currencies)
        self.grb_currencies.setObjectName(u"grb_currencies")
        self.grb_currencies.setMinimumSize(QSize(0, 0))
        self.grb_currencies.setMaximumSize(QSize(16777215, 544))
        self.grb_currencies.setStyleSheet(u"")
        self.cmb_mda_iso4217 = QComboBox(self.grb_currencies)
        self.cmb_mda_iso4217.addItem("")
        self.cmb_mda_iso4217.addItem("")
        self.cmb_mda_iso4217.addItem("")
        self.cmb_mda_iso4217.setObjectName(u"cmb_mda_iso4217")
        self.cmb_mda_iso4217.setGeometry(QRect(90, 90, 80, 20))
        sizePolicy1.setHeightForWidth(self.cmb_mda_iso4217.sizePolicy().hasHeightForWidth())
        self.cmb_mda_iso4217.setSizePolicy(sizePolicy1)
        self.cmb_mda_iso4217.setMinimumSize(QSize(80, 20))
        self.cmb_mda_iso4217.setMaximumSize(QSize(80, 20))
        self.cmb_mda_iso4217.setStyleSheet(u"")
        self.label_mda_simbolo = QLabel(self.grb_currencies)
        self.label_mda_simbolo.setObjectName(u"label_mda_simbolo")
        self.label_mda_simbolo.setGeometry(QRect(387, 90, 105, 20))
        self.label_mda_simbolo.setMinimumSize(QSize(105, 20))
        self.label_mda_simbolo.setMaximumSize(QSize(105, 20))
        self.label_mda_descripcion = QLabel(self.grb_currencies)
        self.label_mda_descripcion.setObjectName(u"label_mda_descripcion")
        self.label_mda_descripcion.setGeometry(QRect(15, 60, 91, 16))
        self.label_mda_descripcion.setMaximumSize(QSize(150, 20))
        self.lineEdit_mda_codigo = QLineEdit(self.grb_currencies)
        self.lineEdit_mda_codigo.setObjectName(u"lineEdit_mda_codigo")
        self.lineEdit_mda_codigo.setGeometry(QRect(90, 30, 100, 20))
        sizePolicy1.setHeightForWidth(self.lineEdit_mda_codigo.sizePolicy().hasHeightForWidth())
        self.lineEdit_mda_codigo.setSizePolicy(sizePolicy1)
        self.lineEdit_mda_codigo.setMaximumSize(QSize(100, 20))
        self.lineEdit_mda_descripcion = QLineEdit(self.grb_currencies)
        self.lineEdit_mda_descripcion.setObjectName(u"lineEdit_mda_descripcion")
        self.lineEdit_mda_descripcion.setGeometry(QRect(111, 60, 400, 20))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_mda_descripcion.sizePolicy().hasHeightForWidth())
        self.lineEdit_mda_descripcion.setSizePolicy(sizePolicy2)
        self.lineEdit_mda_descripcion.setMinimumSize(QSize(400, 20))
        self.lineEdit_mda_descripcion.setMaximumSize(QSize(400, 20))
        self.lineEdit_mda_descripcion.setStyleSheet(u"")
        self.label_mda_iso4217 = QLabel(self.grb_currencies)
        self.label_mda_iso4217.setObjectName(u"label_mda_iso4217")
        self.label_mda_iso4217.setGeometry(QRect(15, 90, 65, 20))
        self.label_mda_iso4217.setMinimumSize(QSize(65, 20))
        self.label_mda_iso4217.setMaximumSize(QSize(65, 20))
        self.label_mda_status = QLabel(self.grb_currencies)
        self.label_mda_status.setObjectName(u"label_mda_status")
        self.label_mda_status.setGeometry(QRect(440, 30, 49, 16))
        self.label_mda_status.setMaximumSize(QSize(100, 20))
        self.label_mda_codigo = QLabel(self.grb_currencies)
        self.label_mda_codigo.setObjectName(u"label_mda_codigo")
        self.label_mda_codigo.setGeometry(QRect(15, 30, 49, 16))
        self.label_mda_codigo.setMaximumSize(QSize(100, 20))
        self.label_mda_codigo.setAutoFillBackground(False)
        self.label_mda_fechacreacion = QLabel(self.grb_currencies)
        self.label_mda_fechacreacion.setObjectName(u"label_mda_fechacreacion")
        self.label_mda_fechacreacion.setGeometry(QRect(20, 120, 130, 20))
        self.label_mda_fechacreacion.setMinimumSize(QSize(130, 20))
        self.label_mda_fechacreacion.setMaximumSize(QSize(130, 20))
        self.dateEdit_mda_fechacreacion = QDateEdit(self.grb_currencies)
        self.dateEdit_mda_fechacreacion.setObjectName(u"dateEdit_mda_fechacreacion")
        self.dateEdit_mda_fechacreacion.setGeometry(QRect(150, 120, 100, 20))
        sizePolicy1.setHeightForWidth(self.dateEdit_mda_fechacreacion.sizePolicy().hasHeightForWidth())
        self.dateEdit_mda_fechacreacion.setSizePolicy(sizePolicy1)
        self.dateEdit_mda_fechacreacion.setMaximumSize(QSize(100, 20))
        self.dateEdit_mda_fechacreacion.setStyleSheet(u"")
        self.dateEdit_mda_fechacreacion.setCalendarPopup(True)
        self.cmb_mda_status = QComboBox(self.grb_currencies)
        self.cmb_mda_status.addItem("")
        self.cmb_mda_status.addItem("")
        self.cmb_mda_status.setObjectName(u"cmb_mda_status")
        self.cmb_mda_status.setGeometry(QRect(498, 30, 80, 20))
        sizePolicy1.setHeightForWidth(self.cmb_mda_status.sizePolicy().hasHeightForWidth())
        self.cmb_mda_status.setSizePolicy(sizePolicy1)
        self.cmb_mda_status.setMinimumSize(QSize(80, 20))
        self.cmb_mda_status.setMaximumSize(QSize(80, 20))
        self.cmb_mda_status.setStyleSheet(u"")
        self.cmb_mda_simbolo = QComboBox(self.grb_currencies)
        self.cmb_mda_simbolo.addItem("")
        self.cmb_mda_simbolo.addItem("")
        self.cmb_mda_simbolo.addItem("")
        self.cmb_mda_simbolo.setObjectName(u"cmb_mda_simbolo")
        self.cmb_mda_simbolo.setGeometry(QRect(498, 90, 80, 20))
        sizePolicy1.setHeightForWidth(self.cmb_mda_simbolo.sizePolicy().hasHeightForWidth())
        self.cmb_mda_simbolo.setSizePolicy(sizePolicy1)
        self.cmb_mda_simbolo.setMinimumSize(QSize(80, 20))
        self.cmb_mda_simbolo.setMaximumSize(QSize(80, 20))
        self.cmb_mda_simbolo.setStyleSheet(u"")

        self.vly_frm_currencies.addWidget(self.grb_currencies)

        self.grb_mda_gestion = QGroupBox(self.frm_currencies)
        self.grb_mda_gestion.setObjectName(u"grb_mda_gestion")
        self.grb_mda_gestion.setMinimumSize(QSize(0, 0))
        self.grb_mda_gestion.setMaximumSize(QSize(625, 210))
        self.grb_mda_gestion.setStyleSheet(u"")
        self.label_mda_fechaactualizacion = QLabel(self.grb_mda_gestion)
        self.label_mda_fechaactualizacion.setObjectName(u"label_mda_fechaactualizacion")
        self.label_mda_fechaactualizacion.setGeometry(QRect(10, 30, 140, 20))
        self.label_mda_fechaactualizacion.setMinimumSize(QSize(140, 20))
        self.label_mda_fechaactualizacion.setMaximumSize(QSize(140, 20))
        self.dateEdit_mda_fechaactualizacion = QDateEdit(self.grb_mda_gestion)
        self.dateEdit_mda_fechaactualizacion.setObjectName(u"dateEdit_mda_fechaactualizacion")
        self.dateEdit_mda_fechaactualizacion.setGeometry(QRect(160, 30, 100, 20))
        self.dateEdit_mda_fechaactualizacion.setMaximumSize(QSize(100, 20))
        self.dateEdit_mda_fechaactualizacion.setStyleSheet(u"")
        self.dateEdit_mda_fechaactualizacion.setCalendarPopup(True)
        self.lineEdit_mda_factorpasivo = QLineEdit(self.grb_mda_gestion)
        self.lineEdit_mda_factorpasivo.setObjectName(u"lineEdit_mda_factorpasivo")
        self.lineEdit_mda_factorpasivo.setGeometry(QRect(471, 70, 100, 20))
        sizePolicy1.setHeightForWidth(self.lineEdit_mda_factorpasivo.sizePolicy().hasHeightForWidth())
        self.lineEdit_mda_factorpasivo.setSizePolicy(sizePolicy1)
        self.lineEdit_mda_factorpasivo.setMaximumSize(QSize(100, 20))
        self.label_mda_factorpasivo = QLabel(self.grb_mda_gestion)
        self.label_mda_factorpasivo.setObjectName(u"label_mda_factorpasivo")
        self.label_mda_factorpasivo.setGeometry(QRect(357, 70, 105, 20))
        self.label_mda_factorpasivo.setMinimumSize(QSize(105, 20))
        self.label_mda_factorpasivo.setMaximumSize(QSize(105, 20))
        self.label_mda_factorpasivo.setAutoFillBackground(False)
        self.label_mda_factorpasivo.setTextFormat(Qt.TextFormat.AutoText)
        self.lineEdit_mda_factoractivo = QLineEdit(self.grb_mda_gestion)
        self.lineEdit_mda_factoractivo.setObjectName(u"lineEdit_mda_factoractivo")
        self.lineEdit_mda_factoractivo.setGeometry(QRect(130, 70, 100, 20))
        sizePolicy1.setHeightForWidth(self.lineEdit_mda_factoractivo.sizePolicy().hasHeightForWidth())
        self.lineEdit_mda_factoractivo.setSizePolicy(sizePolicy1)
        self.lineEdit_mda_factoractivo.setMaximumSize(QSize(100, 20))
        self.label_mda_factoractivo = QLabel(self.grb_mda_gestion)
        self.label_mda_factoractivo.setObjectName(u"label_mda_factoractivo")
        self.label_mda_factoractivo.setGeometry(QRect(20, 70, 105, 20))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(10)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_mda_factoractivo.sizePolicy().hasHeightForWidth())
        self.label_mda_factoractivo.setSizePolicy(sizePolicy3)
        self.label_mda_factoractivo.setMinimumSize(QSize(105, 20))
        self.label_mda_factoractivo.setMaximumSize(QSize(105, 20))
        self.label_mda_factoractivo.setAutoFillBackground(False)
        self.dateEdit_mda_label_mda_fechaultima = QDateEdit(self.grb_mda_gestion)
        self.dateEdit_mda_label_mda_fechaultima.setObjectName(u"dateEdit_mda_label_mda_fechaultima")
        self.dateEdit_mda_label_mda_fechaultima.setGeometry(QRect(470, 30, 100, 20))
        self.dateEdit_mda_label_mda_fechaultima.setMaximumSize(QSize(100, 20))
        self.dateEdit_mda_label_mda_fechaultima.setStyleSheet(u"")
        self.dateEdit_mda_label_mda_fechaultima.setCalendarPopup(True)
        self.label_mda_fechaultima = QLabel(self.grb_mda_gestion)
        self.label_mda_fechaultima.setObjectName(u"label_mda_fechaultima")
        self.label_mda_fechaultima.setGeometry(QRect(320, 30, 145, 20))
        self.label_mda_fechaultima.setMinimumSize(QSize(145, 20))
        self.label_mda_fechaultima.setMaximumSize(QSize(145, 20))

        self.vly_frm_currencies.addWidget(self.grb_mda_gestion)

        self.vly_frm_currencies.setStretch(0, 1)
        self.vly_frm_currencies.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frm_currencies)

        self.frm_bar_currencies = QFrame(self.frm_form_currencies)
        self.frm_bar_currencies.setObjectName(u"frm_bar_currencies")
        sizePolicy1.setHeightForWidth(self.frm_bar_currencies.sizePolicy().hasHeightForWidth())
        self.frm_bar_currencies.setSizePolicy(sizePolicy1)
        self.frm_bar_currencies.setMinimumSize(QSize(629, 64))
        self.frm_bar_currencies.setMaximumSize(QSize(629, 64))
        self.frm_bar_currencies.setStyleSheet(u"/*Estilos para la barra de acciones*/\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(79, 179, 255);\n"
"    border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    min-width: 625px;\n"
"    max-width: 625px;\n"
"    min-height: 60px;\n"
"    max-height: 60px;\n"
"   \n"
"}\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"   border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    padding: 10px;\n"
"    font: 10pt ;\n"
"	font: 9pt \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    margin: 2px;               /* Espaciado uniforme alrededor */\n"
"}\n"
"\n"
"/* Estado hover */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estado p"
                        "resionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.frm_bar_currencies.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bar_currencies.setFrameShadow(QFrame.Shadow.Sunken)
        self.hly_frm_bar_currencies = QHBoxLayout(self.frm_bar_currencies)
        self.hly_frm_bar_currencies.setSpacing(2)
        self.hly_frm_bar_currencies.setObjectName(u"hly_frm_bar_currencies")
        self.hly_frm_bar_currencies.setContentsMargins(4, 4, 4, 4)
        self.btn_add_currencies = QPushButton(self.frm_bar_currencies)
        self.btn_add_currencies.setObjectName(u"btn_add_currencies")
        sizePolicy1.setHeightForWidth(self.btn_add_currencies.sizePolicy().hasHeightForWidth())
        self.btn_add_currencies.setSizePolicy(sizePolicy1)
        self.btn_add_currencies.setMinimumSize(QSize(118, 48))
        self.btn_add_currencies.setMaximumSize(QSize(118, 48))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(True)
        font4.setItalic(False)
        self.btn_add_currencies.setFont(font4)
        self.btn_add_currencies.setStyleSheet(u"")
        icon37 = QIcon()
        icon37.addFile(u":/rec/assets/icons/fi-sr-add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_add_currencies.setIcon(icon37)
        self.btn_add_currencies.setIconSize(QSize(22, 22))

        self.hly_frm_bar_currencies.addWidget(self.btn_add_currencies)

        self.btn_save_currencies = QPushButton(self.frm_bar_currencies)
        self.btn_save_currencies.setObjectName(u"btn_save_currencies")
        self.btn_save_currencies.setMinimumSize(QSize(118, 48))
        self.btn_save_currencies.setMaximumSize(QSize(118, 48))
        self.btn_save_currencies.setFont(font4)
        self.btn_save_currencies.setStyleSheet(u"")
        icon38 = QIcon()
        icon38.addFile(u":/rec/assets/icons/fi-sr-disk.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save_currencies.setIcon(icon38)
        self.btn_save_currencies.setIconSize(QSize(22, 22))

        self.hly_frm_bar_currencies.addWidget(self.btn_save_currencies)

        self.btn_edit_currencies = QPushButton(self.frm_bar_currencies)
        self.btn_edit_currencies.setObjectName(u"btn_edit_currencies")
        sizePolicy1.setHeightForWidth(self.btn_edit_currencies.sizePolicy().hasHeightForWidth())
        self.btn_edit_currencies.setSizePolicy(sizePolicy1)
        self.btn_edit_currencies.setMinimumSize(QSize(118, 48))
        self.btn_edit_currencies.setMaximumSize(QSize(118, 48))
        self.btn_edit_currencies.setFont(font4)
        self.btn_edit_currencies.setStyleSheet(u"")
        icon39 = QIcon()
        icon39.addFile(u":/rec/assets/icons/fi-sr-file-edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_edit_currencies.setIcon(icon39)
        self.btn_edit_currencies.setIconSize(QSize(22, 22))

        self.hly_frm_bar_currencies.addWidget(self.btn_edit_currencies)

        self.btn_cancel_currencies = QPushButton(self.frm_bar_currencies)
        self.btn_cancel_currencies.setObjectName(u"btn_cancel_currencies")
        self.btn_cancel_currencies.setMinimumSize(QSize(118, 48))
        self.btn_cancel_currencies.setMaximumSize(QSize(118, 48))
        self.btn_cancel_currencies.setFont(font4)
        self.btn_cancel_currencies.setStyleSheet(u"")
        icon40 = QIcon()
        icon40.addFile(u":/rec/assets/icons/fi-sr-circle-xmark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cancel_currencies.setIcon(icon40)
        self.btn_cancel_currencies.setIconSize(QSize(22, 22))

        self.hly_frm_bar_currencies.addWidget(self.btn_cancel_currencies)

        self.btn_delete_currencies = QPushButton(self.frm_bar_currencies)
        self.btn_delete_currencies.setObjectName(u"btn_delete_currencies")
        sizePolicy1.setHeightForWidth(self.btn_delete_currencies.sizePolicy().hasHeightForWidth())
        self.btn_delete_currencies.setSizePolicy(sizePolicy1)
        self.btn_delete_currencies.setMinimumSize(QSize(118, 48))
        self.btn_delete_currencies.setMaximumSize(QSize(118, 48))
        self.btn_delete_currencies.setStyleSheet(u"")
        icon41 = QIcon()
        icon41.addFile(u":/rec/assets/icons/fi-sr-delete-document.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_currencies.setIcon(icon41)
        self.btn_delete_currencies.setIconSize(QSize(22, 22))

        self.hly_frm_bar_currencies.addWidget(self.btn_delete_currencies)


        self.verticalLayout.addWidget(self.frm_bar_currencies)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)

        self.hly_frm_currencies.addWidget(self.frm_form_currencies)

        self.qsw_forms.addWidget(self.page_frm_currencies)
        self.page_frm_employees = QWidget()
        self.page_frm_employees.setObjectName(u"page_frm_employees")
        sizePolicy.setHeightForWidth(self.page_frm_employees.sizePolicy().hasHeightForWidth())
        self.page_frm_employees.setSizePolicy(sizePolicy)
        self.page_frm_employees.setMinimumSize(QSize(825, 544))
        self.page_frm_employees.setMaximumSize(QSize(1920, 1080))
        self.page_frm_employees.setStyleSheet(u"")
        self.hly_page_frm_employees = QHBoxLayout(self.page_frm_employees)
        self.hly_page_frm_employees.setSpacing(0)
        self.hly_page_frm_employees.setObjectName(u"hly_page_frm_employees")
        self.hly_page_frm_employees.setContentsMargins(0, 0, 0, 0)
        self.frm_form_employees = QFrame(self.page_frm_employees)
        self.frm_form_employees.setObjectName(u"frm_form_employees")
        sizePolicy.setHeightForWidth(self.frm_form_employees.sizePolicy().hasHeightForWidth())
        self.frm_form_employees.setSizePolicy(sizePolicy)
        self.frm_form_employees.setMinimumSize(QSize(625, 0))
        self.frm_form_employees.setMaximumSize(QSize(1920, 1080))
        self.frm_form_employees.setStyleSheet(u"")
        self.frm_form_employees.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_employees.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_employees = QVBoxLayout(self.frm_form_employees)
        self.vly_frm_form_employees.setSpacing(3)
        self.vly_frm_form_employees.setObjectName(u"vly_frm_form_employees")
        self.vly_frm_form_employees.setContentsMargins(4, 4, 4, 4)
        self.frm_employees = QFrame(self.frm_form_employees)
        self.frm_employees.setObjectName(u"frm_employees")
        sizePolicy.setHeightForWidth(self.frm_employees.sizePolicy().hasHeightForWidth())
        self.frm_employees.setSizePolicy(sizePolicy)
        self.frm_employees.setMinimumSize(QSize(625, 433))
        self.frm_employees.setMaximumSize(QSize(625, 433))
        self.frm_employees.setStyleSheet(u"/* Estilos para la seccion de formularios */\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del marco */\n"
"QGroupBox {\n"
"    background-color: rgb(188, 246, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    color: #000000;                  /* Color del texto */\n"
"    font: bold 24pt \"Segoe UI\";     /* Fuente m\u00e1s grande y en negrita */\n"
"    subcontrol-origin: margin;      /* Posici\u00f3n del t\u00edtulo */\n"
"    subcontrol-position: top left;  /* Alineaci\u00f3n del t\u00edtulo */\n"
"    padding: 4px;                   /* Espacio alrededor del texto */\n"
"}\n"
"\n"
"/* Estilo de las etiquetas */\n"
"QLabel {\n"
"    color: #000000;                /* Color del texto */\n"
"    background-color: rgb(188, 246, 255); /* Opcional: fondo */\n"
"    font: 10pt \"Segoe UI\";        "
                        " /* Fuente de Etiquetas */\n"
"    line-height: 12px;\n"
"}\n"
"\n"
"/* Estilo de QTextEdit */\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QLineEdit */\n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Co"
                        "lor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QComboBox */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* Estilo de QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas r"
                        "edondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
"QComboBox:disabled, \n"
"QDateEdit:disabled, \n"
"QTimeEdit:disabled {\n"
"    background-color: #e1e1e1;\n"
"    color: #808080;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"\n"
"/* Forzamos el QTextEdit */\n"
"QTextEdit:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"/* Forzamos el QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_employees.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_employees.setFrameShadow(QFrame.Shadow.Raised)
        self.vly__employees = QVBoxLayout(self.frm_employees)
        self.vly__employees.setSpacing(3)
        self.vly__employees.setObjectName(u"vly__employees")
        self.vly__employees.setContentsMargins(4, 4, 4, 4)
        self.grb_employees = QGroupBox(self.frm_employees)
        self.grb_employees.setObjectName(u"grb_employees")
        self.grb_employees.setMinimumSize(QSize(0, 0))
        self.grb_employees.setMaximumSize(QSize(16777215, 544))
        self.grb_employees.setStyleSheet(u"")
        self.label_emy_codigo = QLabel(self.grb_employees)
        self.label_emy_codigo.setObjectName(u"label_emy_codigo")
        self.label_emy_codigo.setGeometry(QRect(10, 30, 61, 20))
        self.label_emy_codigo.setMaximumSize(QSize(100, 20))
        self.label_emy_codigo.setAutoFillBackground(False)
        self.lineEdit_emy_codigo = QLineEdit(self.grb_employees)
        self.lineEdit_emy_codigo.setObjectName(u"lineEdit_emy_codigo")
        self.lineEdit_emy_codigo.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_emy_codigo.setMaximumSize(QSize(100, 20))
        self.label_emy_descripcion = QLabel(self.grb_employees)
        self.label_emy_descripcion.setObjectName(u"label_emy_descripcion")
        self.label_emy_descripcion.setGeometry(QRect(10, 60, 101, 20))
        self.label_emy_descripcion.setMaximumSize(QSize(101, 20))
        self.lineEdit_emy_descripcion = QLineEdit(self.grb_employees)
        self.lineEdit_emy_descripcion.setObjectName(u"lineEdit_emy_descripcion")
        self.lineEdit_emy_descripcion.setGeometry(QRect(120, 60, 400, 20))
        self.lineEdit_emy_descripcion.setMinimumSize(QSize(400, 20))
        self.lineEdit_emy_descripcion.setMaximumSize(QSize(400, 20))
        self.lineEdit_emy_descripcion.setStyleSheet(u"")
        self.label_emy_idemployees = QLabel(self.grb_employees)
        self.label_emy_idemployees.setObjectName(u"label_emy_idemployees")
        self.label_emy_idemployees.setGeometry(QRect(10, 90, 101, 20))
        self.label_emy_idemployees.setMinimumSize(QSize(101, 0))
        self.label_emy_idemployees.setMaximumSize(QSize(101, 20))
        self.label_emy_status = QLabel(self.grb_employees)
        self.label_emy_status.setObjectName(u"label_emy_status")
        self.label_emy_status.setGeometry(QRect(428, 30, 61, 20))
        self.label_emy_status.setMaximumSize(QSize(100, 20))
        self.lineEdit_emy_idemployees = QLineEdit(self.grb_employees)
        self.lineEdit_emy_idemployees.setObjectName(u"lineEdit_emy_idemployees")
        self.lineEdit_emy_idemployees.setGeometry(QRect(120, 90, 100, 20))
        self.lineEdit_emy_idemployees.setMaximumSize(QSize(100, 20))
        self.cmb_emy_status = QComboBox(self.grb_employees)
        self.cmb_emy_status.addItem("")
        self.cmb_emy_status.addItem("")
        self.cmb_emy_status.setObjectName(u"cmb_emy_status")
        self.cmb_emy_status.setGeometry(QRect(498, 30, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_emy_status.sizePolicy().hasHeightForWidth())
        self.cmb_emy_status.setSizePolicy(sizePolicy)
        self.cmb_emy_status.setMinimumSize(QSize(80, 20))
        self.cmb_emy_status.setMaximumSize(QSize(80, 20))
        self.cmb_emy_status.setStyleSheet(u"")

        self.vly__employees.addWidget(self.grb_employees)

        self.grb_direccion_telefonos_employees = QGroupBox(self.frm_employees)
        self.grb_direccion_telefonos_employees.setObjectName(u"grb_direccion_telefonos_employees")
        self.grb_direccion_telefonos_employees.setMinimumSize(QSize(0, 0))
        self.grb_direccion_telefonos_employees.setStyleSheet(u"")
        self.label_emy_telefono1 = QLabel(self.grb_direccion_telefonos_employees)
        self.label_emy_telefono1.setObjectName(u"label_emy_telefono1")
        self.label_emy_telefono1.setGeometry(QRect(11, 30, 101, 20))
        self.label_emy_telefono1.setMaximumSize(QSize(150, 20))
        self.label_emy_rol = QLabel(self.grb_direccion_telefonos_employees)
        self.label_emy_rol.setObjectName(u"label_emy_rol")
        self.label_emy_rol.setGeometry(QRect(370, 30, 40, 20))
        self.label_emy_rol.setMaximumSize(QSize(150, 20))
        self.lineEdit_emy_telefono1 = QLineEdit(self.grb_direccion_telefonos_employees)
        self.lineEdit_emy_telefono1.setObjectName(u"lineEdit_emy_telefono1")
        self.lineEdit_emy_telefono1.setGeometry(QRect(120, 30, 165, 20))
        self.lineEdit_emy_telefono1.setMinimumSize(QSize(165, 0))
        self.lineEdit_emy_telefono1.setMaximumSize(QSize(165, 20))
        self.lineEdit_emy_rol = QLineEdit(self.grb_direccion_telefonos_employees)
        self.lineEdit_emy_rol.setObjectName(u"lineEdit_emy_rol")
        self.lineEdit_emy_rol.setGeometry(QRect(419, 30, 165, 20))
        self.lineEdit_emy_rol.setMinimumSize(QSize(165, 0))
        self.lineEdit_emy_rol.setMaximumSize(QSize(165, 20))
        self.label_emy_emailusuario = QLabel(self.grb_direccion_telefonos_employees)
        self.label_emy_emailusuario.setObjectName(u"label_emy_emailusuario")
        self.label_emy_emailusuario.setGeometry(QRect(11, 60, 101, 20))
        self.label_emy_emailusuario.setMaximumSize(QSize(150, 20))
        self.lineEdit_emy_emailusuario = QLineEdit(self.grb_direccion_telefonos_employees)
        self.lineEdit_emy_emailusuario.setObjectName(u"lineEdit_emy_emailusuario")
        self.lineEdit_emy_emailusuario.setGeometry(QRect(120, 60, 260, 20))
        self.lineEdit_emy_emailusuario.setMinimumSize(QSize(260, 0))
        self.lineEdit_emy_emailusuario.setMaximumSize(QSize(260, 20))

        self.vly__employees.addWidget(self.grb_direccion_telefonos_employees)

        self.grb_sontactos__employees = QGroupBox(self.frm_employees)
        self.grb_sontactos__employees.setObjectName(u"grb_sontactos__employees")
        self.grb_sontactos__employees.setMinimumSize(QSize(0, 0))
        self.grb_sontactos__employees.setStyleSheet(u"")
        self.label_emy_cliente = QLabel(self.grb_sontactos__employees)
        self.label_emy_cliente.setObjectName(u"label_emy_cliente")
        self.label_emy_cliente.setGeometry(QRect(10, 30, 110, 20))
        self.label_emy_cliente.setMinimumSize(QSize(110, 20))
        self.label_emy_cliente.setMaximumSize(QSize(110, 20))
        self.lineEdit_emy_cliente = QLineEdit(self.grb_sontactos__employees)
        self.lineEdit_emy_cliente.setObjectName(u"lineEdit_emy_cliente")
        self.lineEdit_emy_cliente.setGeometry(QRect(120, 30, 400, 20))
        self.lineEdit_emy_cliente.setMinimumSize(QSize(400, 0))
        self.lineEdit_emy_cliente.setMaximumSize(QSize(400, 20))
        self.lineEdit_emy_cliente.setStyleSheet(u"")
        self.label_emy_password = QLabel(self.grb_sontactos__employees)
        self.label_emy_password.setObjectName(u"label_emy_password")
        self.label_emy_password.setGeometry(QRect(386, 60, 80, 20))
        self.label_emy_password.setMinimumSize(QSize(80, 0))
        self.label_emy_password.setMaximumSize(QSize(80, 20))
        self.lineEdit_emy_password = QLineEdit(self.grb_sontactos__employees)
        self.lineEdit_emy_password.setObjectName(u"lineEdit_emy_password")
        self.lineEdit_emy_password.setGeometry(QRect(470, 60, 100, 20))
        self.lineEdit_emy_password.setMaximumSize(QSize(100, 20))
        self.lineEdit_emy_cargo = QLineEdit(self.grb_sontactos__employees)
        self.lineEdit_emy_cargo.setObjectName(u"lineEdit_emy_cargo")
        self.lineEdit_emy_cargo.setGeometry(QRect(120, 60, 165, 20))
        self.lineEdit_emy_cargo.setMinimumSize(QSize(165, 0))
        self.lineEdit_emy_cargo.setMaximumSize(QSize(165, 20))
        self.label_emy_cargo = QLabel(self.grb_sontactos__employees)
        self.label_emy_cargo.setObjectName(u"label_emy_cargo")
        self.label_emy_cargo.setGeometry(QRect(10, 60, 110, 20))
        self.label_emy_cargo.setMinimumSize(QSize(110, 0))
        self.label_emy_cargo.setMaximumSize(QSize(110, 20))
        self.dateEdit_emy_fechacreacion = QDateEdit(self.grb_sontactos__employees)
        self.dateEdit_emy_fechacreacion.setObjectName(u"dateEdit_emy_fechacreacion")
        self.dateEdit_emy_fechacreacion.setGeometry(QRect(142, 90, 100, 20))
        self.dateEdit_emy_fechacreacion.setMaximumSize(QSize(100, 20))
        self.dateEdit_emy_fechacreacion.setStyleSheet(u"")
        self.dateEdit_emy_fechacreacion.setCalendarPopup(True)
        self.label_emy_fechacreacion = QLabel(self.grb_sontactos__employees)
        self.label_emy_fechacreacion.setObjectName(u"label_emy_fechacreacion")
        self.label_emy_fechacreacion.setGeometry(QRect(10, 90, 130, 20))
        self.label_emy_fechacreacion.setMaximumSize(QSize(130, 20))

        self.vly__employees.addWidget(self.grb_sontactos__employees)


        self.vly_frm_form_employees.addWidget(self.frm_employees)

        self.frm_bar_employees = QFrame(self.frm_form_employees)
        self.frm_bar_employees.setObjectName(u"frm_bar_employees")
        sizePolicy1.setHeightForWidth(self.frm_bar_employees.sizePolicy().hasHeightForWidth())
        self.frm_bar_employees.setSizePolicy(sizePolicy1)
        self.frm_bar_employees.setMinimumSize(QSize(629, 64))
        self.frm_bar_employees.setMaximumSize(QSize(629, 64))
        self.frm_bar_employees.setStyleSheet(u"/*Estilos para la barra de acciones*/\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(79, 179, 255);\n"
"    border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    min-width: 625px;\n"
"    max-width: 625px;\n"
"    min-height: 60px;\n"
"    max-height: 60px;\n"
"   \n"
"}\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"   border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    padding: 10px;\n"
"    font: 10pt ;\n"
"	font: 9pt \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    margin: 2px;               /* Espaciado uniforme alrededor */\n"
"}\n"
"\n"
"/* Estado hover */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estado p"
                        "resionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.frm_bar_employees.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bar_employees.setFrameShadow(QFrame.Shadow.Sunken)
        self.hly_frm_bar_employees = QHBoxLayout(self.frm_bar_employees)
        self.hly_frm_bar_employees.setSpacing(2)
        self.hly_frm_bar_employees.setObjectName(u"hly_frm_bar_employees")
        self.hly_frm_bar_employees.setContentsMargins(4, 4, 4, 4)
        self.btn_add_employees = QPushButton(self.frm_bar_employees)
        self.btn_add_employees.setObjectName(u"btn_add_employees")
        sizePolicy1.setHeightForWidth(self.btn_add_employees.sizePolicy().hasHeightForWidth())
        self.btn_add_employees.setSizePolicy(sizePolicy1)
        self.btn_add_employees.setMinimumSize(QSize(118, 48))
        self.btn_add_employees.setMaximumSize(QSize(118, 48))
        self.btn_add_employees.setFont(font4)
        self.btn_add_employees.setStyleSheet(u"")
        self.btn_add_employees.setIcon(icon37)
        self.btn_add_employees.setIconSize(QSize(22, 22))

        self.hly_frm_bar_employees.addWidget(self.btn_add_employees)

        self.btn_save_employees = QPushButton(self.frm_bar_employees)
        self.btn_save_employees.setObjectName(u"btn_save_employees")
        self.btn_save_employees.setMinimumSize(QSize(118, 48))
        self.btn_save_employees.setMaximumSize(QSize(118, 48))
        self.btn_save_employees.setFont(font4)
        self.btn_save_employees.setStyleSheet(u"")
        self.btn_save_employees.setIcon(icon38)
        self.btn_save_employees.setIconSize(QSize(22, 22))

        self.hly_frm_bar_employees.addWidget(self.btn_save_employees)

        self.btn_edit_employees = QPushButton(self.frm_bar_employees)
        self.btn_edit_employees.setObjectName(u"btn_edit_employees")
        sizePolicy1.setHeightForWidth(self.btn_edit_employees.sizePolicy().hasHeightForWidth())
        self.btn_edit_employees.setSizePolicy(sizePolicy1)
        self.btn_edit_employees.setMinimumSize(QSize(118, 48))
        self.btn_edit_employees.setMaximumSize(QSize(118, 48))
        self.btn_edit_employees.setFont(font4)
        self.btn_edit_employees.setStyleSheet(u"")
        self.btn_edit_employees.setIcon(icon39)
        self.btn_edit_employees.setIconSize(QSize(22, 22))

        self.hly_frm_bar_employees.addWidget(self.btn_edit_employees)

        self.btn_cancel_employees = QPushButton(self.frm_bar_employees)
        self.btn_cancel_employees.setObjectName(u"btn_cancel_employees")
        self.btn_cancel_employees.setMinimumSize(QSize(118, 48))
        self.btn_cancel_employees.setMaximumSize(QSize(118, 48))
        self.btn_cancel_employees.setFont(font4)
        self.btn_cancel_employees.setStyleSheet(u"")
        self.btn_cancel_employees.setIcon(icon40)
        self.btn_cancel_employees.setIconSize(QSize(22, 22))

        self.hly_frm_bar_employees.addWidget(self.btn_cancel_employees)

        self.btn_delete_employees = QPushButton(self.frm_bar_employees)
        self.btn_delete_employees.setObjectName(u"btn_delete_employees")
        sizePolicy1.setHeightForWidth(self.btn_delete_employees.sizePolicy().hasHeightForWidth())
        self.btn_delete_employees.setSizePolicy(sizePolicy1)
        self.btn_delete_employees.setMinimumSize(QSize(118, 48))
        self.btn_delete_employees.setMaximumSize(QSize(118, 48))
        self.btn_delete_employees.setStyleSheet(u"")
        self.btn_delete_employees.setIcon(icon41)
        self.btn_delete_employees.setIconSize(QSize(22, 22))

        self.hly_frm_bar_employees.addWidget(self.btn_delete_employees)


        self.vly_frm_form_employees.addWidget(self.frm_bar_employees)

        self.vly_frm_form_employees.setStretch(0, 4)

        self.hly_page_frm_employees.addWidget(self.frm_form_employees)

        self.qsw_forms.addWidget(self.page_frm_employees)
        self.page_frm_device_types = QWidget()
        self.page_frm_device_types.setObjectName(u"page_frm_device_types")
        sizePolicy.setHeightForWidth(self.page_frm_device_types.sizePolicy().hasHeightForWidth())
        self.page_frm_device_types.setSizePolicy(sizePolicy)
        self.page_frm_device_types.setMinimumSize(QSize(825, 544))
        self.page_frm_device_types.setMaximumSize(QSize(1920, 1080))
        self.page_frm_device_types.setStyleSheet(u"")
        self.hly_page_frm_device_types = QHBoxLayout(self.page_frm_device_types)
        self.hly_page_frm_device_types.setSpacing(0)
        self.hly_page_frm_device_types.setObjectName(u"hly_page_frm_device_types")
        self.hly_page_frm_device_types.setContentsMargins(0, 0, 0, 0)
        self.frm_form_device_types = QFrame(self.page_frm_device_types)
        self.frm_form_device_types.setObjectName(u"frm_form_device_types")
        sizePolicy.setHeightForWidth(self.frm_form_device_types.sizePolicy().hasHeightForWidth())
        self.frm_form_device_types.setSizePolicy(sizePolicy)
        self.frm_form_device_types.setMinimumSize(QSize(625, 0))
        self.frm_form_device_types.setMaximumSize(QSize(1920, 1080))
        self.frm_form_device_types.setFont(font2)
        self.frm_form_device_types.setStyleSheet(u"")
        self.frm_form_device_types.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_device_types.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_device_types = QVBoxLayout(self.frm_form_device_types)
        self.vly_frm_form_device_types.setSpacing(2)
        self.vly_frm_form_device_types.setObjectName(u"vly_frm_form_device_types")
        self.vly_frm_form_device_types.setContentsMargins(4, 4, 4, 4)
        self.frm_device_types = QFrame(self.frm_form_device_types)
        self.frm_device_types.setObjectName(u"frm_device_types")
        sizePolicy.setHeightForWidth(self.frm_device_types.sizePolicy().hasHeightForWidth())
        self.frm_device_types.setSizePolicy(sizePolicy)
        self.frm_device_types.setMinimumSize(QSize(625, 433))
        self.frm_device_types.setMaximumSize(QSize(625, 433))
        self.frm_device_types.setStyleSheet(u"/* Estilos para la seccion de formularios */\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del marco */\n"
"QGroupBox {\n"
"    background-color: rgb(188, 246, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    color: #000000;                  /* Color del texto */\n"
"    font: bold 24pt \"Segoe UI\";     /* Fuente m\u00e1s grande y en negrita */\n"
"    subcontrol-origin: margin;      /* Posici\u00f3n del t\u00edtulo */\n"
"    subcontrol-position: top left;  /* Alineaci\u00f3n del t\u00edtulo */\n"
"    padding: 4px;                   /* Espacio alrededor del texto */\n"
"}\n"
"\n"
"/* Estilo de las etiquetas */\n"
"QLabel {\n"
"    color: #000000;                /* Color del texto */\n"
"    background-color: rgb(188, 246, 255); /* Opcional: fondo */\n"
"    font: 10pt \"Segoe UI\";        "
                        " /* Fuente de Etiquetas */\n"
"    line-height: 12px;\n"
"}\n"
"\n"
"/* Estilo de QTextEdit */\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QLineEdit */\n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Co"
                        "lor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QComboBox */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* Estilo de QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas r"
                        "edondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
"QComboBox:disabled, \n"
"QDateEdit:disabled, \n"
"QTimeEdit:disabled {\n"
"    background-color: #e1e1e1;\n"
"    color: #808080;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"\n"
"/* Forzamos el QTextEdit */\n"
"QTextEdit:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"/* Forzamos el QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_device_types.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_device_types.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_device_types = QVBoxLayout(self.frm_device_types)
        self.vly_device_types.setSpacing(3)
        self.vly_device_types.setObjectName(u"vly_device_types")
        self.vly_device_types.setContentsMargins(4, 4, 4, 4)
        self.grb_device_types = QGroupBox(self.frm_device_types)
        self.grb_device_types.setObjectName(u"grb_device_types")
        self.grb_device_types.setMinimumSize(QSize(0, 0))
        self.grb_device_types.setMaximumSize(QSize(16777215, 544))
        self.grb_device_types.setStyleSheet(u"")
        self.label_dty_vodigo = QLabel(self.grb_device_types)
        self.label_dty_vodigo.setObjectName(u"label_dty_vodigo")
        self.label_dty_vodigo.setGeometry(QRect(10, 30, 61, 20))
        self.label_dty_vodigo.setMaximumSize(QSize(100, 20))
        self.label_dty_vodigo.setAutoFillBackground(False)
        self.lineEdit_dty_vodigo = QLineEdit(self.grb_device_types)
        self.lineEdit_dty_vodigo.setObjectName(u"lineEdit_dty_vodigo")
        self.lineEdit_dty_vodigo.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_dty_vodigo.setMaximumSize(QSize(100, 20))
        self.label_dty_descripcion = QLabel(self.grb_device_types)
        self.label_dty_descripcion.setObjectName(u"label_dty_descripcion")
        self.label_dty_descripcion.setGeometry(QRect(10, 60, 101, 20))
        self.label_dty_descripcion.setMaximumSize(QSize(150, 20))
        self.lineEdit_dty_Descripcion = QLineEdit(self.grb_device_types)
        self.lineEdit_dty_Descripcion.setObjectName(u"lineEdit_dty_Descripcion")
        self.lineEdit_dty_Descripcion.setGeometry(QRect(120, 60, 400, 20))
        self.lineEdit_dty_Descripcion.setMinimumSize(QSize(400, 20))
        self.lineEdit_dty_Descripcion.setMaximumSize(QSize(400, 20))
        self.lineEdit_dty_Descripcion.setStyleSheet(u"")
        self.label_dty_status = QLabel(self.grb_device_types)
        self.label_dty_status.setObjectName(u"label_dty_status")
        self.label_dty_status.setGeometry(QRect(433, 30, 61, 20))
        self.label_dty_status.setMaximumSize(QSize(100, 20))
        self.cmb_dty_status = QComboBox(self.grb_device_types)
        self.cmb_dty_status.addItem("")
        self.cmb_dty_status.addItem("")
        self.cmb_dty_status.setObjectName(u"cmb_dty_status")
        self.cmb_dty_status.setGeometry(QRect(498, 30, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_dty_status.sizePolicy().hasHeightForWidth())
        self.cmb_dty_status.setSizePolicy(sizePolicy)
        self.cmb_dty_status.setMinimumSize(QSize(80, 20))
        self.cmb_dty_status.setMaximumSize(QSize(80, 24))
        self.cmb_dty_status.setStyleSheet(u"")
        self.label_dty_fechacreacion = QLabel(self.grb_device_types)
        self.label_dty_fechacreacion.setObjectName(u"label_dty_fechacreacion")
        self.label_dty_fechacreacion.setGeometry(QRect(10, 160, 130, 20))
        self.label_dty_fechacreacion.setMaximumSize(QSize(130, 20))
        self.dateEdit_dty_fechacreacion = QDateEdit(self.grb_device_types)
        self.dateEdit_dty_fechacreacion.setObjectName(u"dateEdit_dty_fechacreacion")
        self.dateEdit_dty_fechacreacion.setGeometry(QRect(145, 160, 100, 20))
        self.dateEdit_dty_fechacreacion.setMaximumSize(QSize(100, 20))
        self.dateEdit_dty_fechacreacion.setStyleSheet(u"")
        self.dateEdit_dty_fechacreacion.setCalendarPopup(True)
        self.label_dty_DescripcionTec = QLabel(self.grb_device_types)
        self.label_dty_DescripcionTec.setObjectName(u"label_dty_DescripcionTec")
        self.label_dty_DescripcionTec.setGeometry(QRect(10, 90, 100, 41))
        self.label_dty_DescripcionTec.setMinimumSize(QSize(100, 0))
        self.label_dty_DescripcionTec.setMaximumSize(QSize(100, 60))
        self.label_dty_DescripcionTec.setScaledContents(False)
        self.textEdit_dty_DescripcionTec = QTextEdit(self.grb_device_types)
        self.textEdit_dty_DescripcionTec.setObjectName(u"textEdit_dty_DescripcionTec")
        self.textEdit_dty_DescripcionTec.setGeometry(QRect(120, 90, 400, 60))
        self.textEdit_dty_DescripcionTec.setMinimumSize(QSize(400, 60))
        self.textEdit_dty_DescripcionTec.setMaximumSize(QSize(400, 60))
        self.textEdit_dty_DescripcionTec.setStyleSheet(u"")

        self.vly_device_types.addWidget(self.grb_device_types)


        self.vly_frm_form_device_types.addWidget(self.frm_device_types)

        self.frm_bar_device_types = QFrame(self.frm_form_device_types)
        self.frm_bar_device_types.setObjectName(u"frm_bar_device_types")
        sizePolicy1.setHeightForWidth(self.frm_bar_device_types.sizePolicy().hasHeightForWidth())
        self.frm_bar_device_types.setSizePolicy(sizePolicy1)
        self.frm_bar_device_types.setMinimumSize(QSize(629, 64))
        self.frm_bar_device_types.setMaximumSize(QSize(629, 64))
        self.frm_bar_device_types.setStyleSheet(u"/*Estilos para la barra de acciones*/\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(79, 179, 255);\n"
"    border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    min-width: 625px;\n"
"    max-width: 625px;\n"
"    min-height: 60px;\n"
"    max-height: 60px;\n"
"   \n"
"}\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"   border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    padding: 10px;\n"
"    font: 10pt ;\n"
"	font: 9pt \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    margin: 2px;               /* Espaciado uniforme alrededor */\n"
"}\n"
"\n"
"/* Estado hover */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estado p"
                        "resionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.frm_bar_device_types.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bar_device_types.setFrameShadow(QFrame.Shadow.Sunken)
        self.hly_frm_bar_device_types = QHBoxLayout(self.frm_bar_device_types)
        self.hly_frm_bar_device_types.setSpacing(2)
        self.hly_frm_bar_device_types.setObjectName(u"hly_frm_bar_device_types")
        self.hly_frm_bar_device_types.setContentsMargins(4, 4, 4, 4)
        self.btn_add_device_types = QPushButton(self.frm_bar_device_types)
        self.btn_add_device_types.setObjectName(u"btn_add_device_types")
        sizePolicy1.setHeightForWidth(self.btn_add_device_types.sizePolicy().hasHeightForWidth())
        self.btn_add_device_types.setSizePolicy(sizePolicy1)
        self.btn_add_device_types.setMinimumSize(QSize(118, 48))
        self.btn_add_device_types.setMaximumSize(QSize(118, 48))
        self.btn_add_device_types.setFont(font4)
        self.btn_add_device_types.setStyleSheet(u"")
        self.btn_add_device_types.setIcon(icon37)
        self.btn_add_device_types.setIconSize(QSize(22, 22))

        self.hly_frm_bar_device_types.addWidget(self.btn_add_device_types)

        self.btn_save_device_types = QPushButton(self.frm_bar_device_types)
        self.btn_save_device_types.setObjectName(u"btn_save_device_types")
        self.btn_save_device_types.setMinimumSize(QSize(118, 48))
        self.btn_save_device_types.setMaximumSize(QSize(118, 48))
        self.btn_save_device_types.setFont(font4)
        self.btn_save_device_types.setStyleSheet(u"")
        self.btn_save_device_types.setIcon(icon38)
        self.btn_save_device_types.setIconSize(QSize(22, 22))

        self.hly_frm_bar_device_types.addWidget(self.btn_save_device_types)

        self.btn_edit_device_types = QPushButton(self.frm_bar_device_types)
        self.btn_edit_device_types.setObjectName(u"btn_edit_device_types")
        sizePolicy1.setHeightForWidth(self.btn_edit_device_types.sizePolicy().hasHeightForWidth())
        self.btn_edit_device_types.setSizePolicy(sizePolicy1)
        self.btn_edit_device_types.setMinimumSize(QSize(118, 48))
        self.btn_edit_device_types.setMaximumSize(QSize(118, 48))
        self.btn_edit_device_types.setFont(font4)
        self.btn_edit_device_types.setStyleSheet(u"")
        self.btn_edit_device_types.setIcon(icon39)
        self.btn_edit_device_types.setIconSize(QSize(22, 22))

        self.hly_frm_bar_device_types.addWidget(self.btn_edit_device_types)

        self.btn_cancel_device_types = QPushButton(self.frm_bar_device_types)
        self.btn_cancel_device_types.setObjectName(u"btn_cancel_device_types")
        self.btn_cancel_device_types.setMinimumSize(QSize(118, 48))
        self.btn_cancel_device_types.setMaximumSize(QSize(118, 48))
        self.btn_cancel_device_types.setFont(font4)
        self.btn_cancel_device_types.setStyleSheet(u"")
        self.btn_cancel_device_types.setIcon(icon40)
        self.btn_cancel_device_types.setIconSize(QSize(22, 22))

        self.hly_frm_bar_device_types.addWidget(self.btn_cancel_device_types)

        self.btn_delete_device_types = QPushButton(self.frm_bar_device_types)
        self.btn_delete_device_types.setObjectName(u"btn_delete_device_types")
        sizePolicy1.setHeightForWidth(self.btn_delete_device_types.sizePolicy().hasHeightForWidth())
        self.btn_delete_device_types.setSizePolicy(sizePolicy1)
        self.btn_delete_device_types.setMinimumSize(QSize(118, 48))
        self.btn_delete_device_types.setMaximumSize(QSize(118, 48))
        self.btn_delete_device_types.setStyleSheet(u"")
        self.btn_delete_device_types.setIcon(icon41)
        self.btn_delete_device_types.setIconSize(QSize(22, 22))

        self.hly_frm_bar_device_types.addWidget(self.btn_delete_device_types)


        self.vly_frm_form_device_types.addWidget(self.frm_bar_device_types)

        self.vly_frm_form_device_types.setStretch(0, 4)

        self.hly_page_frm_device_types.addWidget(self.frm_form_device_types)

        self.qsw_forms.addWidget(self.page_frm_device_types)
        self.page_frm_actions_categories = QWidget()
        self.page_frm_actions_categories.setObjectName(u"page_frm_actions_categories")
        sizePolicy.setHeightForWidth(self.page_frm_actions_categories.sizePolicy().hasHeightForWidth())
        self.page_frm_actions_categories.setSizePolicy(sizePolicy)
        self.page_frm_actions_categories.setMinimumSize(QSize(625, 544))
        self.page_frm_actions_categories.setMaximumSize(QSize(1920, 1080))
        self.page_frm_actions_categories.setStyleSheet(u"")
        self.hly_frm_action_categories = QHBoxLayout(self.page_frm_actions_categories)
        self.hly_frm_action_categories.setSpacing(0)
        self.hly_frm_action_categories.setObjectName(u"hly_frm_action_categories")
        self.hly_frm_action_categories.setContentsMargins(0, 0, 0, 0)
        self.frm_form_actions_categories = QFrame(self.page_frm_actions_categories)
        self.frm_form_actions_categories.setObjectName(u"frm_form_actions_categories")
        sizePolicy.setHeightForWidth(self.frm_form_actions_categories.sizePolicy().hasHeightForWidth())
        self.frm_form_actions_categories.setSizePolicy(sizePolicy)
        self.frm_form_actions_categories.setMinimumSize(QSize(825, 0))
        self.frm_form_actions_categories.setMaximumSize(QSize(1920, 1080))
        self.frm_form_actions_categories.setFont(font2)
        self.frm_form_actions_categories.setStyleSheet(u"")
        self.frm_form_actions_categories.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_actions_categories.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_action_categories = QVBoxLayout(self.frm_form_actions_categories)
        self.vly_frm_form_action_categories.setSpacing(3)
        self.vly_frm_form_action_categories.setObjectName(u"vly_frm_form_action_categories")
        self.vly_frm_form_action_categories.setContentsMargins(4, 4, 4, 4)
        self.frm_actions_categories = QFrame(self.frm_form_actions_categories)
        self.frm_actions_categories.setObjectName(u"frm_actions_categories")
        sizePolicy.setHeightForWidth(self.frm_actions_categories.sizePolicy().hasHeightForWidth())
        self.frm_actions_categories.setSizePolicy(sizePolicy)
        self.frm_actions_categories.setMinimumSize(QSize(625, 433))
        self.frm_actions_categories.setMaximumSize(QSize(625, 433))
        self.frm_actions_categories.setStyleSheet(u"/* Estilos para la seccion de formularios */\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del marco */\n"
"QGroupBox {\n"
"    background-color: rgb(188, 246, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    color: #000000;                  /* Color del texto */\n"
"    font: bold 24pt \"Segoe UI\";     /* Fuente m\u00e1s grande y en negrita */\n"
"    subcontrol-origin: margin;      /* Posici\u00f3n del t\u00edtulo */\n"
"    subcontrol-position: top left;  /* Alineaci\u00f3n del t\u00edtulo */\n"
"    padding: 4px;                   /* Espacio alrededor del texto */\n"
"}\n"
"\n"
"/* Estilo de las etiquetas */\n"
"QLabel {\n"
"    color: #000000;                /* Color del texto */\n"
"    background-color: rgb(188, 246, 255); /* Opcional: fondo */\n"
"    font: 10pt \"Segoe UI\";        "
                        " /* Fuente de Etiquetas */\n"
"    line-height: 12px;\n"
"}\n"
"\n"
"/* Estilo de QTextEdit */\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QLineEdit */\n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Co"
                        "lor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QComboBox */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* Estilo de QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas r"
                        "edondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
"QComboBox:disabled, \n"
"QDateEdit:disabled, \n"
"QTimeEdit:disabled {\n"
"    background-color: #e1e1e1;\n"
"    color: #808080;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"\n"
"/* Forzamos el QTextEdit */\n"
"QTextEdit:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"/* Forzamos el QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_actions_categories.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_actions_categories.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_action_categories = QVBoxLayout(self.frm_actions_categories)
        self.vly_action_categories.setSpacing(3)
        self.vly_action_categories.setObjectName(u"vly_action_categories")
        self.vly_action_categories.setContentsMargins(4, 4, 4, 4)
        self.grb_actions_categories = QGroupBox(self.frm_actions_categories)
        self.grb_actions_categories.setObjectName(u"grb_actions_categories")
        self.grb_actions_categories.setMinimumSize(QSize(0, 0))
        self.grb_actions_categories.setMaximumSize(QSize(16777215, 544))
        self.grb_actions_categories.setStyleSheet(u"")
        self.label_cat_codigo = QLabel(self.grb_actions_categories)
        self.label_cat_codigo.setObjectName(u"label_cat_codigo")
        self.label_cat_codigo.setGeometry(QRect(10, 30, 61, 20))
        self.label_cat_codigo.setMaximumSize(QSize(100, 20))
        self.label_cat_codigo.setAutoFillBackground(False)
        self.lineEdit_cat_codigo = QLineEdit(self.grb_actions_categories)
        self.lineEdit_cat_codigo.setObjectName(u"lineEdit_cat_codigo")
        self.lineEdit_cat_codigo.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_cat_codigo.setMaximumSize(QSize(100, 20))
        self.label_cat_descripcion = QLabel(self.grb_actions_categories)
        self.label_cat_descripcion.setObjectName(u"label_cat_descripcion")
        self.label_cat_descripcion.setGeometry(QRect(10, 60, 101, 20))
        self.label_cat_descripcion.setMaximumSize(QSize(150, 20))
        self.lineEdit_cat_descripcion = QLineEdit(self.grb_actions_categories)
        self.lineEdit_cat_descripcion.setObjectName(u"lineEdit_cat_descripcion")
        self.lineEdit_cat_descripcion.setGeometry(QRect(120, 60, 400, 20))
        self.lineEdit_cat_descripcion.setMinimumSize(QSize(400, 20))
        self.lineEdit_cat_descripcion.setMaximumSize(QSize(400, 20))
        self.lineEdit_cat_descripcion.setStyleSheet(u"")
        self.label_cat_status = QLabel(self.grb_actions_categories)
        self.label_cat_status.setObjectName(u"label_cat_status")
        self.label_cat_status.setGeometry(QRect(368, 30, 61, 20))
        self.label_cat_status.setMaximumSize(QSize(100, 20))
        self.cmb_cat_ststus = QComboBox(self.grb_actions_categories)
        self.cmb_cat_ststus.addItem("")
        self.cmb_cat_ststus.addItem("")
        self.cmb_cat_ststus.setObjectName(u"cmb_cat_ststus")
        self.cmb_cat_ststus.setGeometry(QRect(436, 30, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_cat_ststus.sizePolicy().hasHeightForWidth())
        self.cmb_cat_ststus.setSizePolicy(sizePolicy)
        self.cmb_cat_ststus.setMinimumSize(QSize(80, 20))
        self.cmb_cat_ststus.setMaximumSize(QSize(80, 20))
        self.cmb_cat_ststus.setStyleSheet(u"")
        self.label_cat_fechacreacion = QLabel(self.grb_actions_categories)
        self.label_cat_fechacreacion.setObjectName(u"label_cat_fechacreacion")
        self.label_cat_fechacreacion.setGeometry(QRect(10, 160, 130, 20))
        self.label_cat_fechacreacion.setMaximumSize(QSize(130, 20))
        self.dateEdit_cat_fechacreacion = QDateEdit(self.grb_actions_categories)
        self.dateEdit_cat_fechacreacion.setObjectName(u"dateEdit_cat_fechacreacion")
        self.dateEdit_cat_fechacreacion.setGeometry(QRect(128, 160, 100, 20))
        self.dateEdit_cat_fechacreacion.setMaximumSize(QSize(100, 20))
        self.dateEdit_cat_fechacreacion.setStyleSheet(u"")
        self.dateEdit_cat_fechacreacion.setCalendarPopup(True)
        self.textEdit_cat_descripciontec = QTextEdit(self.grb_actions_categories)
        self.textEdit_cat_descripciontec.setObjectName(u"textEdit_cat_descripciontec")
        self.textEdit_cat_descripciontec.setGeometry(QRect(120, 90, 400, 60))
        self.textEdit_cat_descripciontec.setMinimumSize(QSize(400, 60))
        self.textEdit_cat_descripciontec.setMaximumSize(QSize(400, 60))
        self.textEdit_cat_descripciontec.setStyleSheet(u"")
        self.label_cat_descripciontec = QLabel(self.grb_actions_categories)
        self.label_cat_descripciontec.setObjectName(u"label_cat_descripciontec")
        self.label_cat_descripciontec.setGeometry(QRect(10, 90, 100, 41))
        self.label_cat_descripciontec.setMinimumSize(QSize(100, 0))
        self.label_cat_descripciontec.setMaximumSize(QSize(100, 60))
        self.label_cat_descripciontec.setScaledContents(False)

        self.vly_action_categories.addWidget(self.grb_actions_categories)


        self.vly_frm_form_action_categories.addWidget(self.frm_actions_categories)

        self.frm_bar_action_categories = QFrame(self.frm_form_actions_categories)
        self.frm_bar_action_categories.setObjectName(u"frm_bar_action_categories")
        sizePolicy1.setHeightForWidth(self.frm_bar_action_categories.sizePolicy().hasHeightForWidth())
        self.frm_bar_action_categories.setSizePolicy(sizePolicy1)
        self.frm_bar_action_categories.setMinimumSize(QSize(629, 64))
        self.frm_bar_action_categories.setMaximumSize(QSize(629, 64))
        self.frm_bar_action_categories.setStyleSheet(u"/*Estilos para la barra de acciones*/\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(79, 179, 255);\n"
"    border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    min-width: 625px;\n"
"    max-width: 625px;\n"
"    min-height: 60px;\n"
"    max-height: 60px;\n"
"   \n"
"}\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"   border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    padding: 10px;\n"
"    font: 10pt ;\n"
"	font: 9pt \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    margin: 2px;               /* Espaciado uniforme alrededor */\n"
"}\n"
"\n"
"/* Estado hover */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estado p"
                        "resionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.frm_bar_action_categories.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bar_action_categories.setFrameShadow(QFrame.Shadow.Sunken)
        self.hyl_frm_bar_action_categories = QHBoxLayout(self.frm_bar_action_categories)
        self.hyl_frm_bar_action_categories.setSpacing(2)
        self.hyl_frm_bar_action_categories.setObjectName(u"hyl_frm_bar_action_categories")
        self.hyl_frm_bar_action_categories.setContentsMargins(4, 4, 4, 4)
        self.btn_add_actions_categories = QPushButton(self.frm_bar_action_categories)
        self.btn_add_actions_categories.setObjectName(u"btn_add_actions_categories")
        self.btn_add_actions_categories.setMinimumSize(QSize(118, 48))
        self.btn_add_actions_categories.setMaximumSize(QSize(118, 48))
        self.btn_add_actions_categories.setFont(font4)
        self.btn_add_actions_categories.setStyleSheet(u"")
        self.btn_add_actions_categories.setIcon(icon37)
        self.btn_add_actions_categories.setIconSize(QSize(22, 22))

        self.hyl_frm_bar_action_categories.addWidget(self.btn_add_actions_categories)

        self.btn_save_actions_categories = QPushButton(self.frm_bar_action_categories)
        self.btn_save_actions_categories.setObjectName(u"btn_save_actions_categories")
        self.btn_save_actions_categories.setMinimumSize(QSize(118, 48))
        self.btn_save_actions_categories.setMaximumSize(QSize(118, 48))
        self.btn_save_actions_categories.setFont(font4)
        self.btn_save_actions_categories.setStyleSheet(u"")
        self.btn_save_actions_categories.setIcon(icon38)
        self.btn_save_actions_categories.setIconSize(QSize(22, 22))

        self.hyl_frm_bar_action_categories.addWidget(self.btn_save_actions_categories)

        self.btn_edit_actions_categories = QPushButton(self.frm_bar_action_categories)
        self.btn_edit_actions_categories.setObjectName(u"btn_edit_actions_categories")
        self.btn_edit_actions_categories.setMinimumSize(QSize(118, 48))
        self.btn_edit_actions_categories.setMaximumSize(QSize(118, 48))
        self.btn_edit_actions_categories.setFont(font4)
        self.btn_edit_actions_categories.setStyleSheet(u"")
        self.btn_edit_actions_categories.setIcon(icon39)
        self.btn_edit_actions_categories.setIconSize(QSize(22, 22))

        self.hyl_frm_bar_action_categories.addWidget(self.btn_edit_actions_categories)

        self.btn_cancel_actions_categories = QPushButton(self.frm_bar_action_categories)
        self.btn_cancel_actions_categories.setObjectName(u"btn_cancel_actions_categories")
        self.btn_cancel_actions_categories.setMinimumSize(QSize(118, 48))
        self.btn_cancel_actions_categories.setMaximumSize(QSize(118, 48))
        self.btn_cancel_actions_categories.setFont(font4)
        self.btn_cancel_actions_categories.setStyleSheet(u"")
        self.btn_cancel_actions_categories.setIcon(icon40)
        self.btn_cancel_actions_categories.setIconSize(QSize(22, 22))

        self.hyl_frm_bar_action_categories.addWidget(self.btn_cancel_actions_categories)

        self.btn_delete_actions_categories = QPushButton(self.frm_bar_action_categories)
        self.btn_delete_actions_categories.setObjectName(u"btn_delete_actions_categories")
        self.btn_delete_actions_categories.setMinimumSize(QSize(118, 48))
        self.btn_delete_actions_categories.setMaximumSize(QSize(118, 48))
        self.btn_delete_actions_categories.setFont(font4)
        self.btn_delete_actions_categories.setStyleSheet(u"")
        self.btn_delete_actions_categories.setIcon(icon41)
        self.btn_delete_actions_categories.setIconSize(QSize(22, 22))

        self.hyl_frm_bar_action_categories.addWidget(self.btn_delete_actions_categories)


        self.vly_frm_form_action_categories.addWidget(self.frm_bar_action_categories)

        self.vly_frm_form_action_categories.setStretch(0, 4)
        self.vly_frm_form_action_categories.setStretch(1, 1)

        self.hly_frm_action_categories.addWidget(self.frm_form_actions_categories, 0, Qt.AlignmentFlag.AlignLeft)

        self.qsw_forms.addWidget(self.page_frm_actions_categories)
        self.page_frm_it_assets = QWidget()
        self.page_frm_it_assets.setObjectName(u"page_frm_it_assets")
        sizePolicy.setHeightForWidth(self.page_frm_it_assets.sizePolicy().hasHeightForWidth())
        self.page_frm_it_assets.setSizePolicy(sizePolicy)
        self.page_frm_it_assets.setMinimumSize(QSize(825, 544))
        self.page_frm_it_assets.setMaximumSize(QSize(1920, 1080))
        self.page_frm_it_assets.setStyleSheet(u"")
        self.hly_page_frm_it_assets = QHBoxLayout(self.page_frm_it_assets)
        self.hly_page_frm_it_assets.setSpacing(0)
        self.hly_page_frm_it_assets.setObjectName(u"hly_page_frm_it_assets")
        self.hly_page_frm_it_assets.setContentsMargins(0, 0, 0, 0)
        self.frm_form_it_assets = QFrame(self.page_frm_it_assets)
        self.frm_form_it_assets.setObjectName(u"frm_form_it_assets")
        sizePolicy.setHeightForWidth(self.frm_form_it_assets.sizePolicy().hasHeightForWidth())
        self.frm_form_it_assets.setSizePolicy(sizePolicy)
        self.frm_form_it_assets.setMinimumSize(QSize(625, 0))
        self.frm_form_it_assets.setMaximumSize(QSize(1920, 1080))
        self.frm_form_it_assets.setStyleSheet(u"")
        self.frm_form_it_assets.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_it_assets.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frm_form_it_assets)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.frm_it_assets = QFrame(self.frm_form_it_assets)
        self.frm_it_assets.setObjectName(u"frm_it_assets")
        sizePolicy.setHeightForWidth(self.frm_it_assets.sizePolicy().hasHeightForWidth())
        self.frm_it_assets.setSizePolicy(sizePolicy)
        self.frm_it_assets.setMinimumSize(QSize(625, 433))
        self.frm_it_assets.setMaximumSize(QSize(625, 433))
        self.frm_it_assets.setStyleSheet(u"/* Estilos para la seccion de formularios */\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del marco */\n"
"QGroupBox {\n"
"    background-color: rgb(188, 246, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    color: #000000;                  /* Color del texto */\n"
"    font: bold 24pt \"Segoe UI\";     /* Fuente m\u00e1s grande y en negrita */\n"
"    subcontrol-origin: margin;      /* Posici\u00f3n del t\u00edtulo */\n"
"    subcontrol-position: top left;  /* Alineaci\u00f3n del t\u00edtulo */\n"
"    padding: 4px;                   /* Espacio alrededor del texto */\n"
"}\n"
"\n"
"/* Estilo de las etiquetas */\n"
"QLabel {\n"
"    color: #000000;                /* Color del texto */\n"
"    background-color: rgb(188, 246, 255); /* Opcional: fondo */\n"
"    font: 10pt \"Segoe UI\";        "
                        " /* Fuente de Etiquetas */\n"
"    line-height: 12px;\n"
"}\n"
"\n"
"/* Estilo de QTextEdit */\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QLineEdit */\n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Co"
                        "lor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QComboBox */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* Estilo de QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas r"
                        "edondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
"QComboBox:disabled, \n"
"QDateEdit:disabled, \n"
"QTimeEdit:disabled {\n"
"    background-color: #e1e1e1;\n"
"    color: #808080;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"\n"
"/* Forzamos el QTextEdit */\n"
"QTextEdit:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"/* Forzamos el QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_it_assets.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_it_assets.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_it_assets = QVBoxLayout(self.frm_it_assets)
        self.vly_it_assets.setSpacing(3)
        self.vly_it_assets.setObjectName(u"vly_it_assets")
        self.vly_it_assets.setContentsMargins(4, 4, 4, 4)
        self.grb_it_assets = QGroupBox(self.frm_it_assets)
        self.grb_it_assets.setObjectName(u"grb_it_assets")
        self.grb_it_assets.setMinimumSize(QSize(0, 0))
        self.grb_it_assets.setMaximumSize(QSize(16777215, 544))
        self.grb_it_assets.setStyleSheet(u"")
        self.label_ita_codigo = QLabel(self.grb_it_assets)
        self.label_ita_codigo.setObjectName(u"label_ita_codigo")
        self.label_ita_codigo.setGeometry(QRect(10, 30, 61, 20))
        self.label_ita_codigo.setMaximumSize(QSize(100, 20))
        self.label_ita_codigo.setAutoFillBackground(False)
        self.lineEdit_ita_codigo = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_codigo.setObjectName(u"lineEdit_ita_codigo")
        self.lineEdit_ita_codigo.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_ita_codigo.setMaximumSize(QSize(100, 20))
        self.label_ita_descripcion = QLabel(self.grb_it_assets)
        self.label_ita_descripcion.setObjectName(u"label_ita_descripcion")
        self.label_ita_descripcion.setGeometry(QRect(10, 60, 101, 20))
        self.label_ita_descripcion.setMaximumSize(QSize(150, 20))
        self.lineEdit_ita_descripcion = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_descripcion.setObjectName(u"lineEdit_ita_descripcion")
        self.lineEdit_ita_descripcion.setGeometry(QRect(102, 60, 400, 20))
        self.lineEdit_ita_descripcion.setMinimumSize(QSize(400, 20))
        self.lineEdit_ita_descripcion.setMaximumSize(QSize(400, 20))
        self.lineEdit_ita_descripcion.setStyleSheet(u"")
        self.label_ita_marca = QLabel(self.grb_it_assets)
        self.label_ita_marca.setObjectName(u"label_ita_marca")
        self.label_ita_marca.setGeometry(QRect(10, 90, 61, 20))
        self.label_ita_marca.setMinimumSize(QSize(61, 0))
        self.label_ita_marca.setMaximumSize(QSize(61, 20))
        self.label_ita_status = QLabel(self.grb_it_assets)
        self.label_ita_status.setObjectName(u"label_ita_status")
        self.label_ita_status.setGeometry(QRect(433, 30, 61, 20))
        self.label_ita_status.setMaximumSize(QSize(100, 20))
        self.lineEdit_ita_marca = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_marca.setObjectName(u"lineEdit_ita_marca")
        self.lineEdit_ita_marca.setGeometry(QRect(78, 90, 100, 20))
        self.lineEdit_ita_marca.setMaximumSize(QSize(100, 20))
        self.cmb_ita_status = QComboBox(self.grb_it_assets)
        self.cmb_ita_status.addItem("")
        self.cmb_ita_status.addItem("")
        self.cmb_ita_status.setObjectName(u"cmb_ita_status")
        self.cmb_ita_status.setGeometry(QRect(498, 30, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_ita_status.sizePolicy().hasHeightForWidth())
        self.cmb_ita_status.setSizePolicy(sizePolicy)
        self.cmb_ita_status.setMinimumSize(QSize(80, 20))
        self.cmb_ita_status.setMaximumSize(QSize(80, 20))
        self.cmb_ita_status.setStyleSheet(u"")
        self.cmb_ita_Clasificacion = QComboBox(self.grb_it_assets)
        self.cmb_ita_Clasificacion.addItem("")
        self.cmb_ita_Clasificacion.addItem("")
        self.cmb_ita_Clasificacion.addItem("")
        self.cmb_ita_Clasificacion.addItem("")
        self.cmb_ita_Clasificacion.addItem("")
        self.cmb_ita_Clasificacion.addItem("")
        self.cmb_ita_Clasificacion.addItem("")
        self.cmb_ita_Clasificacion.setObjectName(u"cmb_ita_Clasificacion")
        self.cmb_ita_Clasificacion.setGeometry(QRect(325, 90, 240, 20))
        sizePolicy.setHeightForWidth(self.cmb_ita_Clasificacion.sizePolicy().hasHeightForWidth())
        self.cmb_ita_Clasificacion.setSizePolicy(sizePolicy)
        self.cmb_ita_Clasificacion.setMinimumSize(QSize(240, 20))
        self.cmb_ita_Clasificacion.setMaximumSize(QSize(200, 20))
        self.cmb_ita_Clasificacion.setStyleSheet(u"")
        self.label_ita_clasificacion = QLabel(self.grb_it_assets)
        self.label_ita_clasificacion.setObjectName(u"label_ita_clasificacion")
        self.label_ita_clasificacion.setGeometry(QRect(217, 90, 100, 20))
        self.label_ita_clasificacion.setMinimumSize(QSize(100, 20))
        self.label_ita_clasificacion.setMaximumSize(QSize(100, 20))
        self.label_ita_fechavreacion = QLabel(self.grb_it_assets)
        self.label_ita_fechavreacion.setObjectName(u"label_ita_fechavreacion")
        self.label_ita_fechavreacion.setGeometry(QRect(10, 310, 130, 20))
        self.label_ita_fechavreacion.setMinimumSize(QSize(130, 20))
        self.label_ita_fechavreacion.setMaximumSize(QSize(130, 20))
        self.dateEdit_ita_fechavreacion = QDateEdit(self.grb_it_assets)
        self.dateEdit_ita_fechavreacion.setObjectName(u"dateEdit_ita_fechavreacion")
        self.dateEdit_ita_fechavreacion.setGeometry(QRect(143, 310, 100, 20))
        self.dateEdit_ita_fechavreacion.setMaximumSize(QSize(100, 20))
        self.dateEdit_ita_fechavreacion.setStyleSheet(u"")
        self.dateEdit_ita_fechavreacion.setCalendarPopup(True)
        self.textEdit_ita_descripciontec = QTextEdit(self.grb_it_assets)
        self.textEdit_ita_descripciontec.setObjectName(u"textEdit_ita_descripciontec")
        self.textEdit_ita_descripciontec.setGeometry(QRect(102, 120, 440, 60))
        self.textEdit_ita_descripciontec.setMinimumSize(QSize(440, 60))
        self.textEdit_ita_descripciontec.setMaximumSize(QSize(440, 60))
        self.textEdit_ita_descripciontec.setStyleSheet(u"")
        self.label_ita_descripciontec = QLabel(self.grb_it_assets)
        self.label_ita_descripciontec.setObjectName(u"label_ita_descripciontec")
        self.label_ita_descripciontec.setGeometry(QRect(10, 120, 80, 40))
        self.label_ita_descripciontec.setMinimumSize(QSize(80, 40))
        self.label_ita_descripciontec.setMaximumSize(QSize(80, 40))
        self.label_ita_descripciontec.setScaledContents(False)
        self.label_ita_rol = QLabel(self.grb_it_assets)
        self.label_ita_rol.setObjectName(u"label_ita_rol")
        self.label_ita_rol.setGeometry(QRect(360, 190, 40, 20))
        self.label_ita_rol.setMinimumSize(QSize(40, 20))
        self.label_ita_rol.setMaximumSize(QSize(40, 20))
        self.lineEdit_ita_rol = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_rol.setObjectName(u"lineEdit_ita_rol")
        self.lineEdit_ita_rol.setGeometry(QRect(400, 190, 160, 20))
        self.lineEdit_ita_rol.setMinimumSize(QSize(160, 20))
        self.lineEdit_ita_rol.setMaximumSize(QSize(160, 20))
        self.label_ita_functional_units = QLabel(self.grb_it_assets)
        self.label_ita_functional_units.setObjectName(u"label_ita_functional_units")
        self.label_ita_functional_units.setGeometry(QRect(10, 190, 120, 20))
        self.label_ita_functional_units.setMinimumSize(QSize(120, 0))
        self.label_ita_functional_units.setMaximumSize(QSize(120, 20))
        self.label_ita_macadrees = QLabel(self.grb_it_assets)
        self.label_ita_macadrees.setObjectName(u"label_ita_macadrees")
        self.label_ita_macadrees.setGeometry(QRect(10, 220, 80, 20))
        self.label_ita_macadrees.setMinimumSize(QSize(80, 20))
        self.label_ita_macadrees.setMaximumSize(QSize(80, 20))
        self.lineEdit_ita_macadrees = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_macadrees.setObjectName(u"lineEdit_ita_macadrees")
        self.lineEdit_ita_macadrees.setGeometry(QRect(92, 220, 140, 20))
        self.lineEdit_ita_macadrees.setMinimumSize(QSize(140, 20))
        self.lineEdit_ita_macadrees.setMaximumSize(QSize(140, 20))
        self.lineEdit_ita_ipadrees = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_ipadrees.setObjectName(u"lineEdit_ita_ipadrees")
        self.lineEdit_ita_ipadrees.setGeometry(QRect(422, 220, 140, 20))
        self.lineEdit_ita_ipadrees.setMinimumSize(QSize(140, 20))
        self.lineEdit_ita_ipadrees.setMaximumSize(QSize(140, 20))
        self.label_ita_ipadrees = QLabel(self.grb_it_assets)
        self.label_ita_ipadrees.setObjectName(u"label_ita_ipadrees")
        self.label_ita_ipadrees.setGeometry(QRect(329, 220, 90, 20))
        self.label_ita_ipadrees.setMinimumSize(QSize(90, 20))
        self.label_ita_ipadrees.setMaximumSize(QSize(90, 20))
        self.lineEdit_ita_idRDP2 = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_idRDP2.setObjectName(u"lineEdit_ita_idRDP2")
        self.lineEdit_ita_idRDP2.setGeometry(QRect(422, 250, 140, 20))
        self.lineEdit_ita_idRDP2.setMinimumSize(QSize(140, 20))
        self.lineEdit_ita_idRDP2.setMaximumSize(QSize(140, 20))
        self.lineEdit_ita_idRDP1 = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_idRDP1.setObjectName(u"lineEdit_ita_idRDP1")
        self.lineEdit_ita_idRDP1.setGeometry(QRect(93, 250, 140, 20))
        self.lineEdit_ita_idRDP1.setMinimumSize(QSize(140, 20))
        self.lineEdit_ita_idRDP1.setMaximumSize(QSize(140, 20))
        self.label_ita_idRDP1 = QLabel(self.grb_it_assets)
        self.label_ita_idRDP1.setObjectName(u"label_ita_idRDP1")
        self.label_ita_idRDP1.setGeometry(QRect(11, 250, 80, 20))
        self.label_ita_idRDP1.setMinimumSize(QSize(80, 20))
        self.label_ita_idRDP1.setMaximumSize(QSize(80, 20))
        self.label_ita_idRDP2 = QLabel(self.grb_it_assets)
        self.label_ita_idRDP2.setObjectName(u"label_ita_idRDP2")
        self.label_ita_idRDP2.setGeometry(QRect(358, 250, 60, 20))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(60)
        sizePolicy4.setVerticalStretch(20)
        sizePolicy4.setHeightForWidth(self.label_ita_idRDP2.sizePolicy().hasHeightForWidth())
        self.label_ita_idRDP2.setSizePolicy(sizePolicy4)
        self.label_ita_idRDP2.setMinimumSize(QSize(60, 20))
        self.label_ita_idRDP2.setMaximumSize(QSize(100, 20))
        self.label_ita_idemployees = QLabel(self.grb_it_assets)
        self.label_ita_idemployees.setObjectName(u"label_ita_idemployees")
        self.label_ita_idemployees.setGeometry(QRect(10, 280, 120, 20))
        self.label_ita_idemployees.setMinimumSize(QSize(120, 0))
        self.label_ita_idemployees.setMaximumSize(QSize(120, 20))
        self.lineEdit_ita_iprdp = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_iprdp.setObjectName(u"lineEdit_ita_iprdp")
        self.lineEdit_ita_iprdp.setGeometry(QRect(422, 280, 140, 20))
        self.lineEdit_ita_iprdp.setMinimumSize(QSize(140, 20))
        self.lineEdit_ita_iprdp.setMaximumSize(QSize(140, 20))
        self.label_ita_iprdp = QLabel(self.grb_it_assets)
        self.label_ita_iprdp.setObjectName(u"label_ita_iprdp")
        self.label_ita_iprdp.setGeometry(QRect(369, 280, 50, 20))
        self.label_ita_iprdp.setMinimumSize(QSize(50, 20))
        self.label_ita_iprdp.setMaximumSize(QSize(50, 20))
        self.cmb_ita_functional_units = QComboBox(self.grb_it_assets)
        self.cmb_ita_functional_units.setObjectName(u"cmb_ita_functional_units")
        self.cmb_ita_functional_units.setGeometry(QRect(130, 190, 200, 20))
        self.cmb_ita_functional_units.setMinimumSize(QSize(200, 20))
        self.cmb_ita_functional_units.setMaximumSize(QSize(200, 20))
        self.cmb_ita_functional_units.setStyleSheet(u"")
        self.cmb_ita_idemployees = QComboBox(self.grb_it_assets)
        self.cmb_ita_idemployees.setObjectName(u"cmb_ita_idemployees")
        self.cmb_ita_idemployees.setGeometry(QRect(130, 280, 200, 20))
        self.cmb_ita_idemployees.setMinimumSize(QSize(200, 20))
        self.cmb_ita_idemployees.setMaximumSize(QSize(200, 20))
        self.cmb_ita_idemployees.setStyleSheet(u"")
        self.textEdit_ita_NotasTech = QTextEdit(self.grb_it_assets)
        self.textEdit_ita_NotasTech.setObjectName(u"textEdit_ita_NotasTech")
        self.textEdit_ita_NotasTech.setGeometry(QRect(102, 350, 440, 60))
        self.textEdit_ita_NotasTech.setMinimumSize(QSize(440, 60))
        self.textEdit_ita_NotasTech.setMaximumSize(QSize(440, 60))
        self.textEdit_ita_NotasTech.setStyleSheet(u"")
        self.label_ita_NotasTech = QLabel(self.grb_it_assets)
        self.label_ita_NotasTech.setObjectName(u"label_ita_NotasTech")
        self.label_ita_NotasTech.setGeometry(QRect(10, 350, 80, 40))
        self.label_ita_NotasTech.setMinimumSize(QSize(80, 40))
        self.label_ita_NotasTech.setMaximumSize(QSize(80, 40))
        self.label_ita_NotasTech.setScaledContents(False)

        self.vly_it_assets.addWidget(self.grb_it_assets)


        self.verticalLayout_5.addWidget(self.frm_it_assets)

        self.frm_bar_it_assets = QFrame(self.frm_form_it_assets)
        self.frm_bar_it_assets.setObjectName(u"frm_bar_it_assets")
        sizePolicy1.setHeightForWidth(self.frm_bar_it_assets.sizePolicy().hasHeightForWidth())
        self.frm_bar_it_assets.setSizePolicy(sizePolicy1)
        self.frm_bar_it_assets.setMinimumSize(QSize(629, 64))
        self.frm_bar_it_assets.setMaximumSize(QSize(629, 64))
        self.frm_bar_it_assets.setStyleSheet(u"/*Estilos para la barra de acciones*/\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(79, 179, 255);\n"
"    border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    min-width: 625px;\n"
"    max-width: 625px;\n"
"    min-height: 60px;\n"
"    max-height: 60px;\n"
"   \n"
"}\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"   border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    padding: 10px;\n"
"    font: 10pt ;\n"
"	font: 9pt \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    margin: 2px;               /* Espaciado uniforme alrededor */\n"
"}\n"
"\n"
"/* Estado hover */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estado p"
                        "resionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.frm_bar_it_assets.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bar_it_assets.setFrameShadow(QFrame.Shadow.Sunken)
        self.hly_frm_bar_it_assets = QHBoxLayout(self.frm_bar_it_assets)
        self.hly_frm_bar_it_assets.setSpacing(2)
        self.hly_frm_bar_it_assets.setObjectName(u"hly_frm_bar_it_assets")
        self.hly_frm_bar_it_assets.setContentsMargins(4, 4, 4, 4)
        self.btn_add_it_assets = QPushButton(self.frm_bar_it_assets)
        self.btn_add_it_assets.setObjectName(u"btn_add_it_assets")
        sizePolicy1.setHeightForWidth(self.btn_add_it_assets.sizePolicy().hasHeightForWidth())
        self.btn_add_it_assets.setSizePolicy(sizePolicy1)
        self.btn_add_it_assets.setMinimumSize(QSize(118, 48))
        self.btn_add_it_assets.setMaximumSize(QSize(118, 48))
        self.btn_add_it_assets.setFont(font4)
        self.btn_add_it_assets.setStyleSheet(u"")
        self.btn_add_it_assets.setIcon(icon37)
        self.btn_add_it_assets.setIconSize(QSize(22, 22))

        self.hly_frm_bar_it_assets.addWidget(self.btn_add_it_assets)

        self.btn_save_it_assets = QPushButton(self.frm_bar_it_assets)
        self.btn_save_it_assets.setObjectName(u"btn_save_it_assets")
        self.btn_save_it_assets.setMinimumSize(QSize(118, 48))
        self.btn_save_it_assets.setMaximumSize(QSize(118, 48))
        self.btn_save_it_assets.setFont(font4)
        self.btn_save_it_assets.setStyleSheet(u"")
        self.btn_save_it_assets.setIcon(icon38)
        self.btn_save_it_assets.setIconSize(QSize(22, 22))

        self.hly_frm_bar_it_assets.addWidget(self.btn_save_it_assets)

        self.btn_edit_it_assets = QPushButton(self.frm_bar_it_assets)
        self.btn_edit_it_assets.setObjectName(u"btn_edit_it_assets")
        sizePolicy1.setHeightForWidth(self.btn_edit_it_assets.sizePolicy().hasHeightForWidth())
        self.btn_edit_it_assets.setSizePolicy(sizePolicy1)
        self.btn_edit_it_assets.setMinimumSize(QSize(118, 48))
        self.btn_edit_it_assets.setMaximumSize(QSize(118, 48))
        self.btn_edit_it_assets.setFont(font4)
        self.btn_edit_it_assets.setStyleSheet(u"")
        self.btn_edit_it_assets.setIcon(icon39)
        self.btn_edit_it_assets.setIconSize(QSize(22, 22))

        self.hly_frm_bar_it_assets.addWidget(self.btn_edit_it_assets)

        self.btn_cancel_it_assets = QPushButton(self.frm_bar_it_assets)
        self.btn_cancel_it_assets.setObjectName(u"btn_cancel_it_assets")
        self.btn_cancel_it_assets.setMinimumSize(QSize(118, 48))
        self.btn_cancel_it_assets.setMaximumSize(QSize(118, 48))
        self.btn_cancel_it_assets.setFont(font4)
        self.btn_cancel_it_assets.setStyleSheet(u"")
        self.btn_cancel_it_assets.setIcon(icon40)
        self.btn_cancel_it_assets.setIconSize(QSize(22, 22))

        self.hly_frm_bar_it_assets.addWidget(self.btn_cancel_it_assets)

        self.btn_delete_it_assets = QPushButton(self.frm_bar_it_assets)
        self.btn_delete_it_assets.setObjectName(u"btn_delete_it_assets")
        sizePolicy1.setHeightForWidth(self.btn_delete_it_assets.sizePolicy().hasHeightForWidth())
        self.btn_delete_it_assets.setSizePolicy(sizePolicy1)
        self.btn_delete_it_assets.setMinimumSize(QSize(118, 48))
        self.btn_delete_it_assets.setMaximumSize(QSize(118, 48))
        self.btn_delete_it_assets.setStyleSheet(u"")
        self.btn_delete_it_assets.setIcon(icon41)
        self.btn_delete_it_assets.setIconSize(QSize(22, 22))

        self.hly_frm_bar_it_assets.addWidget(self.btn_delete_it_assets)


        self.verticalLayout_5.addWidget(self.frm_bar_it_assets)

        self.verticalLayout_5.setStretch(0, 4)
        self.verticalLayout_5.setStretch(1, 1)

        self.hly_page_frm_it_assets.addWidget(self.frm_form_it_assets)

        self.qsw_forms.addWidget(self.page_frm_it_assets)
        self.page_frm_users = QWidget()
        self.page_frm_users.setObjectName(u"page_frm_users")
        sizePolicy.setHeightForWidth(self.page_frm_users.sizePolicy().hasHeightForWidth())
        self.page_frm_users.setSizePolicy(sizePolicy)
        self.page_frm_users.setMinimumSize(QSize(825, 544))
        self.page_frm_users.setMaximumSize(QSize(1920, 1080))
        self.page_frm_users.setStyleSheet(u"")
        self.hly_page_frm_users = QHBoxLayout(self.page_frm_users)
        self.hly_page_frm_users.setSpacing(0)
        self.hly_page_frm_users.setObjectName(u"hly_page_frm_users")
        self.hly_page_frm_users.setContentsMargins(0, 0, 0, 0)
        self.frm_form_users = QFrame(self.page_frm_users)
        self.frm_form_users.setObjectName(u"frm_form_users")
        sizePolicy.setHeightForWidth(self.frm_form_users.sizePolicy().hasHeightForWidth())
        self.frm_form_users.setSizePolicy(sizePolicy)
        self.frm_form_users.setMinimumSize(QSize(625, 0))
        self.frm_form_users.setMaximumSize(QSize(1920, 1080))
        self.frm_form_users.setStyleSheet(u"")
        self.frm_form_users.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_users.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_users = QVBoxLayout(self.frm_form_users)
        self.vly_frm_form_users.setSpacing(3)
        self.vly_frm_form_users.setObjectName(u"vly_frm_form_users")
        self.vly_frm_form_users.setContentsMargins(4, 4, 4, 4)
        self.frm_users = QFrame(self.frm_form_users)
        self.frm_users.setObjectName(u"frm_users")
        sizePolicy.setHeightForWidth(self.frm_users.sizePolicy().hasHeightForWidth())
        self.frm_users.setSizePolicy(sizePolicy)
        self.frm_users.setMinimumSize(QSize(625, 433))
        self.frm_users.setMaximumSize(QSize(625, 433))
        self.frm_users.setStyleSheet(u"/* Estilos para la seccion de formularios */\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del marco */\n"
"QGroupBox {\n"
"    background-color: rgb(188, 246, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    color: #000000;                  /* Color del texto */\n"
"    font: bold 24pt \"Segoe UI\";     /* Fuente m\u00e1s grande y en negrita */\n"
"    subcontrol-origin: margin;      /* Posici\u00f3n del t\u00edtulo */\n"
"    subcontrol-position: top left;  /* Alineaci\u00f3n del t\u00edtulo */\n"
"    padding: 4px;                   /* Espacio alrededor del texto */\n"
"}\n"
"\n"
"/* Estilo de las etiquetas */\n"
"QLabel {\n"
"    color: #000000;                /* Color del texto */\n"
"    background-color: rgb(188, 246, 255); /* Opcional: fondo */\n"
"    font: 10pt \"Segoe UI\";        "
                        " /* Fuente de Etiquetas */\n"
"    line-height: 12px;\n"
"}\n"
"\n"
"/* Estilo de QTextEdit */\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QLineEdit */\n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Co"
                        "lor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QComboBox */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* Estilo de QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas r"
                        "edondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
"QComboBox:disabled, \n"
"QDateEdit:disabled, \n"
"QTimeEdit:disabled {\n"
"    background-color: #e1e1e1;\n"
"    color: #808080;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"\n"
"/* Forzamos el QTextEdit */\n"
"QTextEdit:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"/* Forzamos el QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_users.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_users.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_users = QVBoxLayout(self.frm_users)
        self.vly_users.setSpacing(3)
        self.vly_users.setObjectName(u"vly_users")
        self.vly_users.setContentsMargins(4, 4, 4, 4)
        self.grb_users = QGroupBox(self.frm_users)
        self.grb_users.setObjectName(u"grb_users")
        self.grb_users.setMinimumSize(QSize(0, 0))
        self.grb_users.setMaximumSize(QSize(16777215, 544))
        self.grb_users.setStyleSheet(u"")
        self.label_usr_codigo = QLabel(self.grb_users)
        self.label_usr_codigo.setObjectName(u"label_usr_codigo")
        self.label_usr_codigo.setGeometry(QRect(10, 30, 61, 20))
        self.label_usr_codigo.setMaximumSize(QSize(100, 20))
        self.label_usr_codigo.setAutoFillBackground(False)
        self.lineEdit_usr_codigo = QLineEdit(self.grb_users)
        self.lineEdit_usr_codigo.setObjectName(u"lineEdit_usr_codigo")
        self.lineEdit_usr_codigo.setGeometry(QRect(80, 30, 100, 20))
        self.lineEdit_usr_codigo.setMaximumSize(QSize(100, 20))
        self.label_usr_descripcion = QLabel(self.grb_users)
        self.label_usr_descripcion.setObjectName(u"label_usr_descripcion")
        self.label_usr_descripcion.setGeometry(QRect(10, 60, 90, 20))
        self.label_usr_descripcion.setMaximumSize(QSize(90, 20))
        self.lineEdit_usr_descripcion = QLineEdit(self.grb_users)
        self.lineEdit_usr_descripcion.setObjectName(u"lineEdit_usr_descripcion")
        self.lineEdit_usr_descripcion.setGeometry(QRect(99, 60, 400, 20))
        self.lineEdit_usr_descripcion.setMinimumSize(QSize(400, 20))
        self.lineEdit_usr_descripcion.setMaximumSize(QSize(400, 20))
        self.lineEdit_usr_descripcion.setStyleSheet(u"")
        self.label_usr_telefono = QLabel(self.grb_users)
        self.label_usr_telefono.setObjectName(u"label_usr_telefono")
        self.label_usr_telefono.setGeometry(QRect(10, 90, 70, 20))
        self.label_usr_telefono.setMinimumSize(QSize(70, 20))
        self.label_usr_telefono.setMaximumSize(QSize(70, 20))
        self.label_usr_status = QLabel(self.grb_users)
        self.label_usr_status.setObjectName(u"label_usr_status")
        self.label_usr_status.setGeometry(QRect(445, 30, 61, 20))
        self.label_usr_status.setMaximumSize(QSize(100, 20))
        self.lineEdit_usr_telefono = QLineEdit(self.grb_users)
        self.lineEdit_usr_telefono.setObjectName(u"lineEdit_usr_telefono")
        self.lineEdit_usr_telefono.setGeometry(QRect(80, 90, 100, 20))
        self.lineEdit_usr_telefono.setMaximumSize(QSize(100, 20))
        self.cmb_usr_status = QComboBox(self.grb_users)
        self.cmb_usr_status.addItem("")
        self.cmb_usr_status.addItem("")
        self.cmb_usr_status.setObjectName(u"cmb_usr_status")
        self.cmb_usr_status.setGeometry(QRect(512, 30, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_usr_status.sizePolicy().hasHeightForWidth())
        self.cmb_usr_status.setSizePolicy(sizePolicy)
        self.cmb_usr_status.setMinimumSize(QSize(80, 20))
        self.cmb_usr_status.setMaximumSize(QSize(80, 20))
        self.cmb_usr_status.setStyleSheet(u"")
        self.label_usr_cargo = QLabel(self.grb_users)
        self.label_usr_cargo.setObjectName(u"label_usr_cargo")
        self.label_usr_cargo.setGeometry(QRect(9, 120, 40, 20))
        self.label_usr_cargo.setMinimumSize(QSize(40, 20))
        self.label_usr_cargo.setMaximumSize(QSize(40, 20))
        self.label_usr_fechacreacion = QLabel(self.grb_users)
        self.label_usr_fechacreacion.setObjectName(u"label_usr_fechacreacion")
        self.label_usr_fechacreacion.setGeometry(QRect(10, 210, 130, 20))
        self.label_usr_fechacreacion.setMaximumSize(QSize(130, 20))
        self.dateEdit_usr_fechacreacion = QDateEdit(self.grb_users)
        self.dateEdit_usr_fechacreacion.setObjectName(u"dateEdit_usr_fechacreacion")
        self.dateEdit_usr_fechacreacion.setGeometry(QRect(140, 210, 100, 20))
        self.dateEdit_usr_fechacreacion.setMaximumSize(QSize(100, 20))
        self.dateEdit_usr_fechacreacion.setStyleSheet(u"")
        self.dateEdit_usr_fechacreacion.setCalendarPopup(True)
        self.cmb_usr_cargo = QComboBox(self.grb_users)
        self.cmb_usr_cargo.setObjectName(u"cmb_usr_cargo")
        self.cmb_usr_cargo.setGeometry(QRect(80, 120, 400, 20))
        self.cmb_usr_cargo.setMinimumSize(QSize(400, 20))
        self.cmb_usr_cargo.setMaximumSize(QSize(400, 20))
        self.cmb_usr_cargo.setStyleSheet(u"")
        self.label_usr_rol = QLabel(self.grb_users)
        self.label_usr_rol.setObjectName(u"label_usr_rol")
        self.label_usr_rol.setGeometry(QRect(10, 150, 70, 20))
        self.label_usr_rol.setMinimumSize(QSize(70, 20))
        self.label_usr_rol.setMaximumSize(QSize(70, 20))
        self.lineEdit_usr_rol = QLineEdit(self.grb_users)
        self.lineEdit_usr_rol.setObjectName(u"lineEdit_usr_rol")
        self.lineEdit_usr_rol.setGeometry(QRect(80, 150, 400, 20))
        self.lineEdit_usr_rol.setMaximumSize(QSize(400, 20))
        self.label_usr_emailusuario = QLabel(self.grb_users)
        self.label_usr_emailusuario.setObjectName(u"label_usr_emailusuario")
        self.label_usr_emailusuario.setGeometry(QRect(244, 90, 50, 20))
        self.label_usr_emailusuario.setMinimumSize(QSize(50, 20))
        self.label_usr_emailusuario.setMaximumSize(QSize(50, 20))
        self.lineEdit_usr_emailusuario = QLineEdit(self.grb_users)
        self.lineEdit_usr_emailusuario.setObjectName(u"lineEdit_usr_emailusuario")
        self.lineEdit_usr_emailusuario.setGeometry(QRect(297, 90, 200, 20))
        self.lineEdit_usr_emailusuario.setMaximumSize(QSize(200, 20))
        self.label_usr_password_in = QLabel(self.grb_users)
        self.label_usr_password_in.setObjectName(u"label_usr_password_in")
        self.label_usr_password_in.setGeometry(QRect(10, 180, 70, 20))
        self.label_usr_password_in.setMinimumSize(QSize(70, 20))
        self.label_usr_password_in.setMaximumSize(QSize(70, 20))
        self.lineEdit_usr_password_in = QLineEdit(self.grb_users)
        self.lineEdit_usr_password_in.setObjectName(u"lineEdit_usr_password_in")
        self.lineEdit_usr_password_in.setGeometry(QRect(80, 180, 100, 20))
        self.lineEdit_usr_password_in.setMaximumSize(QSize(100, 20))
        self.label_usr_password_rin = QLabel(self.grb_users)
        self.label_usr_password_rin.setObjectName(u"label_usr_password_rin")
        self.label_usr_password_rin.setGeometry(QRect(272, 180, 100, 20))
        self.label_usr_password_rin.setMinimumSize(QSize(100, 20))
        self.label_usr_password_rin.setMaximumSize(QSize(100, 20))
        self.lineEdit_usr_password_rin = QLineEdit(self.grb_users)
        self.lineEdit_usr_password_rin.setObjectName(u"lineEdit_usr_password_rin")
        self.lineEdit_usr_password_rin.setGeometry(QRect(377, 180, 100, 20))
        self.lineEdit_usr_password_rin.setMaximumSize(QSize(100, 20))

        self.vly_users.addWidget(self.grb_users)


        self.vly_frm_form_users.addWidget(self.frm_users)

        self.frm_bar_users = QFrame(self.frm_form_users)
        self.frm_bar_users.setObjectName(u"frm_bar_users")
        sizePolicy1.setHeightForWidth(self.frm_bar_users.sizePolicy().hasHeightForWidth())
        self.frm_bar_users.setSizePolicy(sizePolicy1)
        self.frm_bar_users.setMinimumSize(QSize(629, 64))
        self.frm_bar_users.setMaximumSize(QSize(629, 64))
        self.frm_bar_users.setStyleSheet(u"/*Estilos para la barra de acciones*/\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(79, 179, 255);\n"
"    border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    min-width: 625px;\n"
"    max-width: 625px;\n"
"    min-height: 60px;\n"
"    max-height: 60px;\n"
"   \n"
"}\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"   border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    padding: 10px;\n"
"    font: 10pt ;\n"
"	font: 9pt \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    margin: 2px;               /* Espaciado uniforme alrededor */\n"
"}\n"
"\n"
"/* Estado hover */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estado p"
                        "resionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.frm_bar_users.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bar_users.setFrameShadow(QFrame.Shadow.Sunken)
        self.hly_frm_bar_users = QHBoxLayout(self.frm_bar_users)
        self.hly_frm_bar_users.setSpacing(2)
        self.hly_frm_bar_users.setObjectName(u"hly_frm_bar_users")
        self.hly_frm_bar_users.setContentsMargins(4, 4, 4, 4)
        self.btn_add_users = QPushButton(self.frm_bar_users)
        self.btn_add_users.setObjectName(u"btn_add_users")
        sizePolicy1.setHeightForWidth(self.btn_add_users.sizePolicy().hasHeightForWidth())
        self.btn_add_users.setSizePolicy(sizePolicy1)
        self.btn_add_users.setMinimumSize(QSize(118, 48))
        self.btn_add_users.setMaximumSize(QSize(118, 48))
        self.btn_add_users.setFont(font4)
        self.btn_add_users.setStyleSheet(u"")
        self.btn_add_users.setIcon(icon37)
        self.btn_add_users.setIconSize(QSize(22, 22))

        self.hly_frm_bar_users.addWidget(self.btn_add_users)

        self.btn_save_users = QPushButton(self.frm_bar_users)
        self.btn_save_users.setObjectName(u"btn_save_users")
        self.btn_save_users.setMinimumSize(QSize(118, 48))
        self.btn_save_users.setMaximumSize(QSize(118, 48))
        self.btn_save_users.setFont(font4)
        self.btn_save_users.setStyleSheet(u"")
        self.btn_save_users.setIcon(icon38)
        self.btn_save_users.setIconSize(QSize(22, 22))

        self.hly_frm_bar_users.addWidget(self.btn_save_users)

        self.btn_edit_users = QPushButton(self.frm_bar_users)
        self.btn_edit_users.setObjectName(u"btn_edit_users")
        sizePolicy1.setHeightForWidth(self.btn_edit_users.sizePolicy().hasHeightForWidth())
        self.btn_edit_users.setSizePolicy(sizePolicy1)
        self.btn_edit_users.setMinimumSize(QSize(118, 48))
        self.btn_edit_users.setMaximumSize(QSize(118, 48))
        self.btn_edit_users.setFont(font4)
        self.btn_edit_users.setStyleSheet(u"")
        self.btn_edit_users.setIcon(icon39)
        self.btn_edit_users.setIconSize(QSize(22, 22))

        self.hly_frm_bar_users.addWidget(self.btn_edit_users)

        self.btn_cancel_users = QPushButton(self.frm_bar_users)
        self.btn_cancel_users.setObjectName(u"btn_cancel_users")
        self.btn_cancel_users.setMinimumSize(QSize(118, 48))
        self.btn_cancel_users.setMaximumSize(QSize(118, 48))
        self.btn_cancel_users.setFont(font4)
        self.btn_cancel_users.setStyleSheet(u"")
        self.btn_cancel_users.setIcon(icon40)
        self.btn_cancel_users.setIconSize(QSize(22, 22))

        self.hly_frm_bar_users.addWidget(self.btn_cancel_users)

        self.btn_delete_users = QPushButton(self.frm_bar_users)
        self.btn_delete_users.setObjectName(u"btn_delete_users")
        sizePolicy1.setHeightForWidth(self.btn_delete_users.sizePolicy().hasHeightForWidth())
        self.btn_delete_users.setSizePolicy(sizePolicy1)
        self.btn_delete_users.setMinimumSize(QSize(118, 48))
        self.btn_delete_users.setMaximumSize(QSize(118, 48))
        self.btn_delete_users.setStyleSheet(u"")
        self.btn_delete_users.setIcon(icon41)
        self.btn_delete_users.setIconSize(QSize(22, 22))

        self.hly_frm_bar_users.addWidget(self.btn_delete_users)


        self.vly_frm_form_users.addWidget(self.frm_bar_users)

        self.vly_frm_form_users.setStretch(0, 4)
        self.vly_frm_form_users.setStretch(1, 1)

        self.hly_page_frm_users.addWidget(self.frm_form_users)

        self.qsw_forms.addWidget(self.page_frm_users)
        self.page_frm_sessions = QWidget()
        self.page_frm_sessions.setObjectName(u"page_frm_sessions")
        sizePolicy.setHeightForWidth(self.page_frm_sessions.sizePolicy().hasHeightForWidth())
        self.page_frm_sessions.setSizePolicy(sizePolicy)
        self.page_frm_sessions.setMinimumSize(QSize(825, 544))
        self.page_frm_sessions.setMaximumSize(QSize(1920, 1080))
        self.page_frm_sessions.setStyleSheet(u"")
        self.hly_page_frm_sessions = QHBoxLayout(self.page_frm_sessions)
        self.hly_page_frm_sessions.setSpacing(0)
        self.hly_page_frm_sessions.setObjectName(u"hly_page_frm_sessions")
        self.hly_page_frm_sessions.setContentsMargins(0, 0, 0, 0)
        self.frm_form_sessions = QFrame(self.page_frm_sessions)
        self.frm_form_sessions.setObjectName(u"frm_form_sessions")
        sizePolicy.setHeightForWidth(self.frm_form_sessions.sizePolicy().hasHeightForWidth())
        self.frm_form_sessions.setSizePolicy(sizePolicy)
        self.frm_form_sessions.setMinimumSize(QSize(625, 0))
        self.frm_form_sessions.setMaximumSize(QSize(1920, 1080))
        self.frm_form_sessions.setStyleSheet(u"")
        self.frm_form_sessions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_sessions.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_sessions = QVBoxLayout(self.frm_form_sessions)
        self.vly_frm_form_sessions.setSpacing(3)
        self.vly_frm_form_sessions.setObjectName(u"vly_frm_form_sessions")
        self.vly_frm_form_sessions.setContentsMargins(4, 4, 4, 4)
        self.frm_sessions = QFrame(self.frm_form_sessions)
        self.frm_sessions.setObjectName(u"frm_sessions")
        sizePolicy.setHeightForWidth(self.frm_sessions.sizePolicy().hasHeightForWidth())
        self.frm_sessions.setSizePolicy(sizePolicy)
        self.frm_sessions.setMinimumSize(QSize(625, 433))
        self.frm_sessions.setMaximumSize(QSize(625, 433))
        self.frm_sessions.setStyleSheet(u"/* Estilos para la seccion de formularios */\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del marco */\n"
"QGroupBox {\n"
"    background-color: rgb(188, 246, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    color: #000000;                  /* Color del texto */\n"
"    font: bold 24pt \"Segoe UI\";     /* Fuente m\u00e1s grande y en negrita */\n"
"    subcontrol-origin: margin;      /* Posici\u00f3n del t\u00edtulo */\n"
"    subcontrol-position: top left;  /* Alineaci\u00f3n del t\u00edtulo */\n"
"    padding: 4px;                   /* Espacio alrededor del texto */\n"
"}\n"
"\n"
"/* Estilo de las etiquetas */\n"
"QLabel {\n"
"    color: #000000;                /* Color del texto */\n"
"    background-color: rgb(188, 246, 255); /* Opcional: fondo */\n"
"    font: 10pt \"Segoe UI\";        "
                        " /* Fuente de Etiquetas */\n"
"    line-height: 12px;\n"
"}\n"
"\n"
"/* Estilo de QTextEdit */\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QLineEdit */\n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Co"
                        "lor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QComboBox */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* Estilo de QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas r"
                        "edondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
"QComboBox:disabled, \n"
"QDateEdit:disabled, \n"
"QTimeEdit:disabled {\n"
"    background-color: #e1e1e1;\n"
"    color: #808080;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"\n"
"/* Forzamos el QTextEdit */\n"
"QTextEdit:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"/* Forzamos el QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_sessions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_sessions.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_sessions = QVBoxLayout(self.frm_sessions)
        self.vly_frm_sessions.setSpacing(3)
        self.vly_frm_sessions.setObjectName(u"vly_frm_sessions")
        self.vly_frm_sessions.setContentsMargins(4, 4, 4, 4)
        self.grb_sessions = QGroupBox(self.frm_sessions)
        self.grb_sessions.setObjectName(u"grb_sessions")
        self.grb_sessions.setMinimumSize(QSize(0, 0))
        self.grb_sessions.setMaximumSize(QSize(16777215, 544))
        self.grb_sessions.setStyleSheet(u"")
        self.grb_sessions.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_ses_numero = QLabel(self.grb_sessions)
        self.label_ses_numero.setObjectName(u"label_ses_numero")
        self.label_ses_numero.setGeometry(QRect(10, 30, 50, 20))
        self.label_ses_numero.setMinimumSize(QSize(50, 20))
        self.label_ses_numero.setMaximumSize(QSize(50, 20))
        self.label_ses_numero.setAutoFillBackground(False)
        self.lineEdit_ses_numero = QLineEdit(self.grb_sessions)
        self.lineEdit_ses_numero.setObjectName(u"lineEdit_ses_numero")
        self.lineEdit_ses_numero.setGeometry(QRect(67, 30, 100, 20))
        self.lineEdit_ses_numero.setMaximumSize(QSize(100, 20))
        self.label_ses_clt_descripcion = QLabel(self.grb_sessions)
        self.label_ses_clt_descripcion.setObjectName(u"label_ses_clt_descripcion")
        self.label_ses_clt_descripcion.setGeometry(QRect(10, 60, 101, 20))
        self.label_ses_clt_descripcion.setMaximumSize(QSize(150, 20))
        self.label_ses_clt_idfiscal = QLabel(self.grb_sessions)
        self.label_ses_clt_idfiscal.setObjectName(u"label_ses_clt_idfiscal")
        self.label_ses_clt_idfiscal.setGeometry(QRect(10, 90, 115, 20))
        self.label_ses_clt_idfiscal.setMinimumSize(QSize(115, 0))
        self.label_ses_clt_idfiscal.setMaximumSize(QSize(110, 20))
        self.label_ses_status = QLabel(self.grb_sessions)
        self.label_ses_status.setObjectName(u"label_ses_status")
        self.label_ses_status.setGeometry(QRect(10, 173, 50, 20))
        self.label_ses_status.setMaximumSize(QSize(50, 20))
        self.lineEdit_ses_clt_idfiscal = QLineEdit(self.grb_sessions)
        self.lineEdit_ses_clt_idfiscal.setObjectName(u"lineEdit_ses_clt_idfiscal")
        self.lineEdit_ses_clt_idfiscal.setGeometry(QRect(133, 90, 100, 20))
        self.lineEdit_ses_clt_idfiscal.setMaximumSize(QSize(100, 20))
        self.cmb_ses_status = QComboBox(self.grb_sessions)
        self.cmb_ses_status.addItem("")
        self.cmb_ses_status.addItem("")
        self.cmb_ses_status.setObjectName(u"cmb_ses_status")
        self.cmb_ses_status.setGeometry(QRect(67, 173, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_ses_status.sizePolicy().hasHeightForWidth())
        self.cmb_ses_status.setSizePolicy(sizePolicy)
        self.cmb_ses_status.setMinimumSize(QSize(80, 20))
        self.cmb_ses_status.setMaximumSize(QSize(80, 20))
        self.cmb_ses_status.setStyleSheet(u"")
        self.label_ses_fechaemision = QLabel(self.grb_sessions)
        self.label_ses_fechaemision.setObjectName(u"label_ses_fechaemision")
        self.label_ses_fechaemision.setGeometry(QRect(375, 30, 120, 20))
        self.label_ses_fechaemision.setMinimumSize(QSize(120, 20))
        self.label_ses_fechaemision.setMaximumSize(QSize(120, 20))
        self.dateEdit_ses_fechaemision = QDateEdit(self.grb_sessions)
        self.dateEdit_ses_fechaemision.setObjectName(u"dateEdit_ses_fechaemision")
        self.dateEdit_ses_fechaemision.setGeometry(QRect(504, 30, 100, 20))
        self.dateEdit_ses_fechaemision.setMinimumSize(QSize(100, 20))
        self.dateEdit_ses_fechaemision.setMaximumSize(QSize(100, 20))
        self.dateEdit_ses_fechaemision.setStyleSheet(u"")
        self.dateEdit_ses_fechaemision.setMaximumDateTime(QDateTime(QDate(2501, 1, 3), QTime(23, 59, 59)))
        self.dateEdit_ses_fechaemision.setMinimumDateTime(QDateTime(QDate(1752, 12, 1), QTime(0, 0, 0)))
        self.dateEdit_ses_fechaemision.setMinimumDate(QDate(1752, 12, 1))
        self.dateEdit_ses_fechaemision.setMaximumTime(QTime(23, 59, 59))
        self.dateEdit_ses_fechaemision.setMinimumTime(QTime(0, 0, 0))
        self.dateEdit_ses_fechaemision.setCalendarPopup(True)
        self.cmb_ses_clt_descripcion = QComboBox(self.grb_sessions)
        self.cmb_ses_clt_descripcion.setObjectName(u"cmb_ses_clt_descripcion")
        self.cmb_ses_clt_descripcion.setGeometry(QRect(110, 60, 400, 20))
        self.cmb_ses_clt_descripcion.setMinimumSize(QSize(400, 20))
        self.cmb_ses_clt_descripcion.setMaximumSize(QSize(400, 20))
        self.textEdit_ses_direccionf = QTextEdit(self.grb_sessions)
        self.textEdit_ses_direccionf.setObjectName(u"textEdit_ses_direccionf")
        self.textEdit_ses_direccionf.setGeometry(QRect(110, 120, 400, 45))
        sizePolicy.setHeightForWidth(self.textEdit_ses_direccionf.sizePolicy().hasHeightForWidth())
        self.textEdit_ses_direccionf.setSizePolicy(sizePolicy)
        self.textEdit_ses_direccionf.setMinimumSize(QSize(400, 45))
        self.textEdit_ses_direccionf.setMaximumSize(QSize(400, 45))
        self.textEdit_ses_direccionf.setStyleSheet(u"")
        self.label_ses_direccionf = QLabel(self.grb_sessions)
        self.label_ses_direccionf.setObjectName(u"label_ses_direccionf")
        self.label_ses_direccionf.setGeometry(QRect(10, 120, 70, 40))
        sizePolicy1.setHeightForWidth(self.label_ses_direccionf.sizePolicy().hasHeightForWidth())
        self.label_ses_direccionf.setSizePolicy(sizePolicy1)
        self.label_ses_direccionf.setMinimumSize(QSize(70, 40))
        self.label_ses_direccionf.setMaximumSize(QSize(70, 40))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setHintingPreference(QFont.PreferNoHinting)
        self.label_ses_direccionf.setFont(font5)
        self.label_ses_direccionf.setStyleSheet(u"QLabel {\n"
"    line-height: 12px;\n"
"}")
        self.label_ses_direccionf.setScaledContents(False)
        self.label_ses_direccionf.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lineEdit_ses_clt_telefono1 = QLineEdit(self.grb_sessions)
        self.lineEdit_ses_clt_telefono1.setObjectName(u"lineEdit_ses_clt_telefono1")
        self.lineEdit_ses_clt_telefono1.setGeometry(QRect(333, 90, 100, 20))
        self.lineEdit_ses_clt_telefono1.setMaximumSize(QSize(100, 20))
        self.label_ses_clt_telefono1 = QLabel(self.grb_sessions)
        self.label_ses_clt_telefono1.setObjectName(u"label_ses_clt_telefono1")
        self.label_ses_clt_telefono1.setGeometry(QRect(259, 90, 70, 20))
        self.label_ses_clt_telefono1.setMinimumSize(QSize(70, 20))
        self.label_ses_clt_telefono1.setMaximumSize(QSize(70, 20))
        self.lineEdit_ses_clt_telefono2 = QLineEdit(self.grb_sessions)
        self.lineEdit_ses_clt_telefono2.setObjectName(u"lineEdit_ses_clt_telefono2")
        self.lineEdit_ses_clt_telefono2.setGeometry(QRect(504, 90, 100, 20))
        self.lineEdit_ses_clt_telefono2.setMaximumSize(QSize(100, 20))
        self.label_ses_clt_telefono2 = QLabel(self.grb_sessions)
        self.label_ses_clt_telefono2.setObjectName(u"label_ses_clt_telefono2")
        self.label_ses_clt_telefono2.setGeometry(QRect(457, 90, 40, 20))
        self.label_ses_clt_telefono2.setMinimumSize(QSize(40, 20))
        self.label_ses_clt_telefono2.setMaximumSize(QSize(40, 20))

        self.vly_frm_sessions.addWidget(self.grb_sessions)

        self.grb_ark_sessions_details = QGroupBox(self.frm_sessions)
        self.grb_ark_sessions_details.setObjectName(u"grb_ark_sessions_details")
        self.grb_ark_sessions_details.setMinimumSize(QSize(0, 0))
        self.grb_ark_sessions_details.setMaximumSize(QSize(16777215, 16777215))
        self.grb_ark_sessions_details.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)
        self.grb_ark_sessions_details.setFlat(True)
        self.grb_ark_sessions_details.setCheckable(False)
        self.label__ses_horafinal = QLabel(self.grb_ark_sessions_details)
        self.label__ses_horafinal.setObjectName(u"label__ses_horafinal")
        self.label__ses_horafinal.setGeometry(QRect(468, 30, 30, 20))
        self.label__ses_horafinal.setMinimumSize(QSize(30, 20))
        self.label__ses_horafinal.setMaximumSize(QSize(30, 20))
        self.label__ses_horainicial = QLabel(self.grb_ark_sessions_details)
        self.label__ses_horainicial.setObjectName(u"label__ses_horainicial")
        self.label__ses_horainicial.setGeometry(QRect(264, 30, 90, 20))
        self.label__ses_horainicial.setMinimumSize(QSize(90, 0))
        self.label__ses_horainicial.setMaximumSize(QSize(90, 20))
        self.timeEdit_ses_horainicial = QTimeEdit(self.grb_ark_sessions_details)
        self.timeEdit_ses_horainicial.setObjectName(u"timeEdit_ses_horainicial")
        self.timeEdit_ses_horainicial.setGeometry(QRect(357, 30, 90, 20))
        self.timeEdit_ses_horainicial.setMinimumSize(QSize(90, 20))
        self.timeEdit_ses_horainicial.setMaximumSize(QSize(90, 20))
        self.timeEdit_ses_horainicial.setStyleSheet(u"")
        self.timeEdit_ses_horainicial.setTime(QTime(0, 0, 0))
        self.dateEdit_ses_fechasesion = QDateEdit(self.grb_ark_sessions_details)
        self.dateEdit_ses_fechasesion.setObjectName(u"dateEdit_ses_fechasesion")
        self.dateEdit_ses_fechasesion.setGeometry(QRect(136, 30, 100, 20))
        self.dateEdit_ses_fechasesion.setMinimumSize(QSize(100, 20))
        self.dateEdit_ses_fechasesion.setMaximumSize(QSize(100, 20))
        self.dateEdit_ses_fechasesion.setStyleSheet(u"")
        self.dateEdit_ses_fechasesion.setMaximumDateTime(QDateTime(QDate(2501, 1, 5), QTime(23, 59, 59)))
        self.dateEdit_ses_fechasesion.setMinimumDateTime(QDateTime(QDate(1752, 12, 1), QTime(0, 0, 0)))
        self.dateEdit_ses_fechasesion.setMinimumDate(QDate(1752, 12, 1))
        self.dateEdit_ses_fechasesion.setMaximumTime(QTime(23, 59, 59))
        self.dateEdit_ses_fechasesion.setMinimumTime(QTime(0, 0, 0))
        self.dateEdit_ses_fechasesion.setCalendarPopup(True)
        self.label_ses_fechasesion = QLabel(self.grb_ark_sessions_details)
        self.label_ses_fechasesion.setObjectName(u"label_ses_fechasesion")
        self.label_ses_fechasesion.setGeometry(QRect(10, 30, 120, 20))
        self.label_ses_fechasesion.setMinimumSize(QSize(120, 20))
        self.label_ses_fechasesion.setMaximumSize(QSize(120, 20))
        self.timeEdit_ses_horafinal = QTimeEdit(self.grb_ark_sessions_details)
        self.timeEdit_ses_horafinal.setObjectName(u"timeEdit_ses_horafinal")
        self.timeEdit_ses_horafinal.setGeometry(QRect(504, 30, 90, 20))
        self.timeEdit_ses_horafinal.setMinimumSize(QSize(90, 20))
        self.timeEdit_ses_horafinal.setMaximumSize(QSize(90, 20))
        self.timeEdit_ses_horafinal.setStyleSheet(u"")
        self.textEdit_dts_description = QTextEdit(self.grb_ark_sessions_details)
        self.textEdit_dts_description.setObjectName(u"textEdit_dts_description")
        self.textEdit_dts_description.setGeometry(QRect(110, 60, 450, 80))
        sizePolicy.setHeightForWidth(self.textEdit_dts_description.sizePolicy().hasHeightForWidth())
        self.textEdit_dts_description.setSizePolicy(sizePolicy)
        self.textEdit_dts_description.setMinimumSize(QSize(450, 80))
        self.textEdit_dts_description.setMaximumSize(QSize(450, 80))
        self.textEdit_dts_description.setStyleSheet(u"f")
        self.label_dts_description = QLabel(self.grb_ark_sessions_details)
        self.label_dts_description.setObjectName(u"label_dts_description")
        self.label_dts_description.setGeometry(QRect(10, 60, 70, 40))
        sizePolicy1.setHeightForWidth(self.label_dts_description.sizePolicy().hasHeightForWidth())
        self.label_dts_description.setSizePolicy(sizePolicy1)
        self.label_dts_description.setMinimumSize(QSize(70, 40))
        self.label_dts_description.setMaximumSize(QSize(70, 40))
        self.label_dts_description.setFont(font5)
        self.label_dts_description.setStyleSheet(u"QLabel {\n"
"    line-height: 12px;\n"
"}")
        self.label_dts_description.setScaledContents(False)
        self.label_dts_description.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lineEdit_dts_time_spent = QLineEdit(self.grb_ark_sessions_details)
        self.lineEdit_dts_time_spent.setObjectName(u"lineEdit_dts_time_spent")
        self.lineEdit_dts_time_spent.setGeometry(QRect(130, 150, 100, 20))
        self.lineEdit_dts_time_spent.setMaximumSize(QSize(100, 20))
        self.label_dts_time_spent = QLabel(self.grb_ark_sessions_details)
        self.label_dts_time_spent.setObjectName(u"label_dts_time_spent")
        self.label_dts_time_spent.setGeometry(QRect(10, 150, 115, 20))
        self.label_dts_time_spent.setMinimumSize(QSize(115, 0))
        self.label_dts_time_spent.setMaximumSize(QSize(110, 20))
        self.label_dts_result = QLabel(self.grb_ark_sessions_details)
        self.label_dts_result.setObjectName(u"label_dts_result")
        self.label_dts_result.setGeometry(QRect(270, 150, 70, 20))
        self.label_dts_result.setMinimumSize(QSize(70, 20))
        self.label_dts_result.setMaximumSize(QSize(70, 20))
        self.lineEdit_dts_result = QLineEdit(self.grb_ark_sessions_details)
        self.lineEdit_dts_result.setObjectName(u"lineEdit_dts_result")
        self.lineEdit_dts_result.setGeometry(QRect(347, 150, 100, 20))
        self.lineEdit_dts_result.setMaximumSize(QSize(100, 20))

        self.vly_frm_sessions.addWidget(self.grb_ark_sessions_details)

        self.vly_frm_sessions.setStretch(0, 1)
        self.vly_frm_sessions.setStretch(1, 1)

        self.vly_frm_form_sessions.addWidget(self.frm_sessions)

        self.frm_bar_sessions = QFrame(self.frm_form_sessions)
        self.frm_bar_sessions.setObjectName(u"frm_bar_sessions")
        sizePolicy1.setHeightForWidth(self.frm_bar_sessions.sizePolicy().hasHeightForWidth())
        self.frm_bar_sessions.setSizePolicy(sizePolicy1)
        self.frm_bar_sessions.setMinimumSize(QSize(629, 64))
        self.frm_bar_sessions.setMaximumSize(QSize(629, 64))
        self.frm_bar_sessions.setStyleSheet(u"/*Estilos para la barra de acciones*/\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(79, 179, 255);\n"
"    border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    min-width: 625px;\n"
"    max-width: 625px;\n"
"    min-height: 60px;\n"
"    max-height: 60px;\n"
"   \n"
"}\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"   border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    padding: 10px;\n"
"    font: 10pt ;\n"
"	font: 9pt \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    margin: 2px;               /* Espaciado uniforme alrededor */\n"
"}\n"
"\n"
"/* Estado hover */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estado p"
                        "resionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.frm_bar_sessions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bar_sessions.setFrameShadow(QFrame.Shadow.Sunken)
        self.hly_frm_bar_sessions = QHBoxLayout(self.frm_bar_sessions)
        self.hly_frm_bar_sessions.setSpacing(2)
        self.hly_frm_bar_sessions.setObjectName(u"hly_frm_bar_sessions")
        self.hly_frm_bar_sessions.setContentsMargins(4, 4, 4, 4)
        self.btn_add_sessions = QPushButton(self.frm_bar_sessions)
        self.btn_add_sessions.setObjectName(u"btn_add_sessions")
        sizePolicy1.setHeightForWidth(self.btn_add_sessions.sizePolicy().hasHeightForWidth())
        self.btn_add_sessions.setSizePolicy(sizePolicy1)
        self.btn_add_sessions.setMinimumSize(QSize(118, 48))
        self.btn_add_sessions.setMaximumSize(QSize(118, 48))
        self.btn_add_sessions.setFont(font4)
        self.btn_add_sessions.setStyleSheet(u"")
        self.btn_add_sessions.setIcon(icon37)
        self.btn_add_sessions.setIconSize(QSize(22, 22))

        self.hly_frm_bar_sessions.addWidget(self.btn_add_sessions)

        self.btn_save_sessions = QPushButton(self.frm_bar_sessions)
        self.btn_save_sessions.setObjectName(u"btn_save_sessions")
        self.btn_save_sessions.setMinimumSize(QSize(118, 48))
        self.btn_save_sessions.setMaximumSize(QSize(118, 48))
        self.btn_save_sessions.setFont(font4)
        self.btn_save_sessions.setStyleSheet(u"")
        self.btn_save_sessions.setIcon(icon38)
        self.btn_save_sessions.setIconSize(QSize(22, 22))

        self.hly_frm_bar_sessions.addWidget(self.btn_save_sessions)

        self.btn_edit_sessions = QPushButton(self.frm_bar_sessions)
        self.btn_edit_sessions.setObjectName(u"btn_edit_sessions")
        sizePolicy1.setHeightForWidth(self.btn_edit_sessions.sizePolicy().hasHeightForWidth())
        self.btn_edit_sessions.setSizePolicy(sizePolicy1)
        self.btn_edit_sessions.setMinimumSize(QSize(118, 48))
        self.btn_edit_sessions.setMaximumSize(QSize(118, 48))
        self.btn_edit_sessions.setFont(font4)
        self.btn_edit_sessions.setStyleSheet(u"")
        self.btn_edit_sessions.setIcon(icon39)
        self.btn_edit_sessions.setIconSize(QSize(22, 22))

        self.hly_frm_bar_sessions.addWidget(self.btn_edit_sessions)

        self.btn_cancel_sessions = QPushButton(self.frm_bar_sessions)
        self.btn_cancel_sessions.setObjectName(u"btn_cancel_sessions")
        self.btn_cancel_sessions.setMinimumSize(QSize(118, 48))
        self.btn_cancel_sessions.setMaximumSize(QSize(118, 48))
        self.btn_cancel_sessions.setFont(font4)
        self.btn_cancel_sessions.setStyleSheet(u"")
        self.btn_cancel_sessions.setIcon(icon40)
        self.btn_cancel_sessions.setIconSize(QSize(22, 22))

        self.hly_frm_bar_sessions.addWidget(self.btn_cancel_sessions)

        self.btn_delete_sessions = QPushButton(self.frm_bar_sessions)
        self.btn_delete_sessions.setObjectName(u"btn_delete_sessions")
        sizePolicy1.setHeightForWidth(self.btn_delete_sessions.sizePolicy().hasHeightForWidth())
        self.btn_delete_sessions.setSizePolicy(sizePolicy1)
        self.btn_delete_sessions.setMinimumSize(QSize(118, 48))
        self.btn_delete_sessions.setMaximumSize(QSize(118, 48))
        self.btn_delete_sessions.setStyleSheet(u"")
        self.btn_delete_sessions.setIcon(icon41)
        self.btn_delete_sessions.setIconSize(QSize(22, 22))

        self.hly_frm_bar_sessions.addWidget(self.btn_delete_sessions)


        self.vly_frm_form_sessions.addWidget(self.frm_bar_sessions)

        self.vly_frm_form_sessions.setStretch(0, 4)
        self.vly_frm_form_sessions.setStretch(1, 1)

        self.hly_page_frm_sessions.addWidget(self.frm_form_sessions)

        self.qsw_forms.addWidget(self.page_frm_sessions)
        self.page_frm_requests = QWidget()
        self.page_frm_requests.setObjectName(u"page_frm_requests")
        sizePolicy.setHeightForWidth(self.page_frm_requests.sizePolicy().hasHeightForWidth())
        self.page_frm_requests.setSizePolicy(sizePolicy)
        self.page_frm_requests.setMinimumSize(QSize(825, 544))
        self.page_frm_requests.setMaximumSize(QSize(1920, 1080))
        self.page_frm_requests.setStyleSheet(u"")
        self.hly_page_frm_requests = QHBoxLayout(self.page_frm_requests)
        self.hly_page_frm_requests.setSpacing(0)
        self.hly_page_frm_requests.setObjectName(u"hly_page_frm_requests")
        self.hly_page_frm_requests.setContentsMargins(0, 0, 0, 0)
        self.frm_form_requests = QFrame(self.page_frm_requests)
        self.frm_form_requests.setObjectName(u"frm_form_requests")
        sizePolicy.setHeightForWidth(self.frm_form_requests.sizePolicy().hasHeightForWidth())
        self.frm_form_requests.setSizePolicy(sizePolicy)
        self.frm_form_requests.setMinimumSize(QSize(625, 0))
        self.frm_form_requests.setMaximumSize(QSize(1920, 1080))
        self.frm_form_requests.setStyleSheet(u"")
        self.frm_form_requests.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_requests.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_requests = QVBoxLayout(self.frm_form_requests)
        self.vly_frm_form_requests.setSpacing(3)
        self.vly_frm_form_requests.setObjectName(u"vly_frm_form_requests")
        self.vly_frm_form_requests.setContentsMargins(4, 4, 4, 4)
        self.frm_requests = QFrame(self.frm_form_requests)
        self.frm_requests.setObjectName(u"frm_requests")
        sizePolicy.setHeightForWidth(self.frm_requests.sizePolicy().hasHeightForWidth())
        self.frm_requests.setSizePolicy(sizePolicy)
        self.frm_requests.setMinimumSize(QSize(625, 433))
        self.frm_requests.setMaximumSize(QSize(625, 433))
        self.frm_requests.setStyleSheet(u"/* Estilos para la seccion de formularios */\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del marco */\n"
"QGroupBox {\n"
"    background-color: rgb(188, 246, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    color: #000000;                  /* Color del texto */\n"
"    font: bold 24pt \"Segoe UI\";     /* Fuente m\u00e1s grande y en negrita */\n"
"    subcontrol-origin: margin;      /* Posici\u00f3n del t\u00edtulo */\n"
"    subcontrol-position: top left;  /* Alineaci\u00f3n del t\u00edtulo */\n"
"    padding: 4px;                   /* Espacio alrededor del texto */\n"
"}\n"
"\n"
"/* Estilo de las etiquetas */\n"
"QLabel {\n"
"    color: #000000;                /* Color del texto */\n"
"    background-color: rgb(188, 246, 255); /* Opcional: fondo */\n"
"    font: 10pt \"Segoe UI\";        "
                        " /* Fuente de Etiquetas */\n"
"    line-height: 12px;\n"
"}\n"
"\n"
"/* Estilo de QTextEdit */\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QLineEdit */\n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Co"
                        "lor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QComboBox */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* Estilo de QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas r"
                        "edondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
"QComboBox:disabled, \n"
"QDateEdit:disabled, \n"
"QTimeEdit:disabled {\n"
"    background-color: #e1e1e1;\n"
"    color: #808080;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"\n"
"/* Forzamos el QTextEdit */\n"
"QTextEdit:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"/* Forzamos el QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_requests.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_requests.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_requests = QVBoxLayout(self.frm_requests)
        self.vly_requests.setSpacing(3)
        self.vly_requests.setObjectName(u"vly_requests")
        self.vly_requests.setContentsMargins(4, 4, 4, 4)
        self.grb_requests = QGroupBox(self.frm_requests)
        self.grb_requests.setObjectName(u"grb_requests")
        self.grb_requests.setMinimumSize(QSize(0, 0))
        self.grb_requests.setMaximumSize(QSize(16777215, 544))
        self.grb_requests.setStyleSheet(u"")
        self.label_req_codigo = QLabel(self.grb_requests)
        self.label_req_codigo.setObjectName(u"label_req_codigo")
        self.label_req_codigo.setGeometry(QRect(10, 30, 50, 20))
        self.label_req_codigo.setMaximumSize(QSize(80, 20))
        self.label_req_codigo.setAutoFillBackground(False)
        self.lineEdit_req_codigo = QLineEdit(self.grb_requests)
        self.lineEdit_req_codigo.setObjectName(u"lineEdit_req_codigo")
        self.lineEdit_req_codigo.setGeometry(QRect(66, 30, 100, 20))
        self.lineEdit_req_codigo.setMaximumSize(QSize(100, 20))
        self.label_req_descripcion = QLabel(self.grb_requests)
        self.label_req_descripcion.setObjectName(u"label_req_descripcion")
        self.label_req_descripcion.setGeometry(QRect(10, 60, 90, 20))
        self.label_req_descripcion.setMinimumSize(QSize(90, 20))
        self.label_req_descripcion.setMaximumSize(QSize(90, 20))
        self.lineEdit_req_descripcion = QLineEdit(self.grb_requests)
        self.lineEdit_req_descripcion.setObjectName(u"lineEdit_req_descripcion")
        self.lineEdit_req_descripcion.setGeometry(QRect(101, 60, 400, 20))
        self.lineEdit_req_descripcion.setMinimumSize(QSize(400, 20))
        self.lineEdit_req_descripcion.setMaximumSize(QSize(400, 20))
        self.lineEdit_req_descripcion.setStyleSheet(u"")
        self.label_req_status = QLabel(self.grb_requests)
        self.label_req_status.setObjectName(u"label_req_status")
        self.label_req_status.setGeometry(QRect(458, 30, 50, 20))
        self.label_req_status.setMinimumSize(QSize(50, 20))
        self.label_req_status.setMaximumSize(QSize(50, 20))
        self.cmb_req_status = QComboBox(self.grb_requests)
        self.cmb_req_status.addItem("")
        self.cmb_req_status.addItem("")
        self.cmb_req_status.setObjectName(u"cmb_req_status")
        self.cmb_req_status.setGeometry(QRect(512, 30, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_req_status.sizePolicy().hasHeightForWidth())
        self.cmb_req_status.setSizePolicy(sizePolicy)
        self.cmb_req_status.setMinimumSize(QSize(80, 20))
        self.cmb_req_status.setMaximumSize(QSize(80, 20))
        self.cmb_req_status.setStyleSheet(u"")
        self.label_req_fechacreacion = QLabel(self.grb_requests)
        self.label_req_fechacreacion.setObjectName(u"label_req_fechacreacion")
        self.label_req_fechacreacion.setGeometry(QRect(10, 180, 130, 20))
        self.label_req_fechacreacion.setMinimumSize(QSize(130, 20))
        self.label_req_fechacreacion.setMaximumSize(QSize(130, 20))
        self.dateEdit_req_fechacreacion = QDateEdit(self.grb_requests)
        self.dateEdit_req_fechacreacion.setObjectName(u"dateEdit_req_fechacreacion")
        self.dateEdit_req_fechacreacion.setGeometry(QRect(140, 180, 100, 20))
        self.dateEdit_req_fechacreacion.setMaximumSize(QSize(100, 20))
        self.dateEdit_req_fechacreacion.setStyleSheet(u"")
        self.dateEdit_req_fechacreacion.setCalendarPopup(True)
        self.textEdit_req_descripciontec = QTextEdit(self.grb_requests)
        self.textEdit_req_descripciontec.setObjectName(u"textEdit_req_descripciontec")
        self.textEdit_req_descripciontec.setGeometry(QRect(101, 85, 400, 60))
        self.textEdit_req_descripciontec.setMinimumSize(QSize(400, 60))
        self.textEdit_req_descripciontec.setMaximumSize(QSize(400, 60))
        self.textEdit_req_descripciontec.setStyleSheet(u"")
        self.label_req_descripciontec = QLabel(self.grb_requests)
        self.label_req_descripciontec.setObjectName(u"label_req_descripciontec")
        self.label_req_descripciontec.setGeometry(QRect(10, 90, 80, 41))
        self.label_req_descripciontec.setMinimumSize(QSize(80, 0))
        self.label_req_descripciontec.setMaximumSize(QSize(100, 60))
        self.label_req_descripciontec.setScaledContents(False)
        self.cmb_req_codigocliente = QComboBox(self.grb_requests)
        self.cmb_req_codigocliente.setObjectName(u"cmb_req_codigocliente")
        self.cmb_req_codigocliente.setGeometry(QRect(101, 150, 400, 20))
        self.cmb_req_codigocliente.setMinimumSize(QSize(400, 20))
        self.cmb_req_codigocliente.setMaximumSize(QSize(400, 20))
        self.cmb_req_codigocliente.setStyleSheet(u"")
        self.label_req_codigocliente = QLabel(self.grb_requests)
        self.label_req_codigocliente.setObjectName(u"label_req_codigocliente")
        self.label_req_codigocliente.setGeometry(QRect(10, 150, 80, 20))
        self.label_req_codigocliente.setMinimumSize(QSize(80, 20))
        self.label_req_codigocliente.setMaximumSize(QSize(80, 20))
        self.label_req_codigocliente.setAutoFillBackground(False)

        self.vly_requests.addWidget(self.grb_requests)


        self.vly_frm_form_requests.addWidget(self.frm_requests)

        self.frm_bar_requests = QFrame(self.frm_form_requests)
        self.frm_bar_requests.setObjectName(u"frm_bar_requests")
        sizePolicy1.setHeightForWidth(self.frm_bar_requests.sizePolicy().hasHeightForWidth())
        self.frm_bar_requests.setSizePolicy(sizePolicy1)
        self.frm_bar_requests.setMinimumSize(QSize(629, 64))
        self.frm_bar_requests.setMaximumSize(QSize(629, 64))
        self.frm_bar_requests.setStyleSheet(u"/*Estilos para la barra de acciones*/\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(79, 179, 255);\n"
"    border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    min-width: 625px;\n"
"    max-width: 625px;\n"
"    min-height: 60px;\n"
"    max-height: 60px;\n"
"   \n"
"}\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"   border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    padding: 10px;\n"
"    font: 10pt ;\n"
"	font: 9pt \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    margin: 2px;               /* Espaciado uniforme alrededor */\n"
"}\n"
"\n"
"/* Estado hover */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estado p"
                        "resionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.frm_bar_requests.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bar_requests.setFrameShadow(QFrame.Shadow.Sunken)
        self.hly_frm_bar_requests = QHBoxLayout(self.frm_bar_requests)
        self.hly_frm_bar_requests.setSpacing(2)
        self.hly_frm_bar_requests.setObjectName(u"hly_frm_bar_requests")
        self.hly_frm_bar_requests.setContentsMargins(4, 4, 4, 4)
        self.btn_add_requests = QPushButton(self.frm_bar_requests)
        self.btn_add_requests.setObjectName(u"btn_add_requests")
        sizePolicy1.setHeightForWidth(self.btn_add_requests.sizePolicy().hasHeightForWidth())
        self.btn_add_requests.setSizePolicy(sizePolicy1)
        self.btn_add_requests.setMinimumSize(QSize(118, 48))
        self.btn_add_requests.setMaximumSize(QSize(118, 48))
        self.btn_add_requests.setFont(font4)
        self.btn_add_requests.setStyleSheet(u"")
        self.btn_add_requests.setIcon(icon37)
        self.btn_add_requests.setIconSize(QSize(22, 22))

        self.hly_frm_bar_requests.addWidget(self.btn_add_requests)

        self.btn_save_requests = QPushButton(self.frm_bar_requests)
        self.btn_save_requests.setObjectName(u"btn_save_requests")
        self.btn_save_requests.setMinimumSize(QSize(118, 48))
        self.btn_save_requests.setMaximumSize(QSize(118, 48))
        self.btn_save_requests.setFont(font4)
        self.btn_save_requests.setStyleSheet(u"")
        self.btn_save_requests.setIcon(icon38)
        self.btn_save_requests.setIconSize(QSize(22, 22))

        self.hly_frm_bar_requests.addWidget(self.btn_save_requests)

        self.btn_edit_requests = QPushButton(self.frm_bar_requests)
        self.btn_edit_requests.setObjectName(u"btn_edit_requests")
        sizePolicy1.setHeightForWidth(self.btn_edit_requests.sizePolicy().hasHeightForWidth())
        self.btn_edit_requests.setSizePolicy(sizePolicy1)
        self.btn_edit_requests.setMinimumSize(QSize(118, 48))
        self.btn_edit_requests.setMaximumSize(QSize(118, 48))
        self.btn_edit_requests.setFont(font4)
        self.btn_edit_requests.setStyleSheet(u"")
        self.btn_edit_requests.setIcon(icon39)
        self.btn_edit_requests.setIconSize(QSize(22, 22))

        self.hly_frm_bar_requests.addWidget(self.btn_edit_requests)

        self.btn_cancel_requests = QPushButton(self.frm_bar_requests)
        self.btn_cancel_requests.setObjectName(u"btn_cancel_requests")
        self.btn_cancel_requests.setMinimumSize(QSize(118, 48))
        self.btn_cancel_requests.setMaximumSize(QSize(118, 48))
        self.btn_cancel_requests.setFont(font4)
        self.btn_cancel_requests.setStyleSheet(u"")
        self.btn_cancel_requests.setIcon(icon40)
        self.btn_cancel_requests.setIconSize(QSize(22, 22))

        self.hly_frm_bar_requests.addWidget(self.btn_cancel_requests)

        self.btn_delete_requests = QPushButton(self.frm_bar_requests)
        self.btn_delete_requests.setObjectName(u"btn_delete_requests")
        sizePolicy1.setHeightForWidth(self.btn_delete_requests.sizePolicy().hasHeightForWidth())
        self.btn_delete_requests.setSizePolicy(sizePolicy1)
        self.btn_delete_requests.setMinimumSize(QSize(118, 48))
        self.btn_delete_requests.setMaximumSize(QSize(118, 48))
        self.btn_delete_requests.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_delete_requests.setStyleSheet(u"")
        self.btn_delete_requests.setIcon(icon41)
        self.btn_delete_requests.setIconSize(QSize(22, 22))

        self.hly_frm_bar_requests.addWidget(self.btn_delete_requests)


        self.vly_frm_form_requests.addWidget(self.frm_bar_requests)

        self.vly_frm_form_requests.setStretch(0, 4)
        self.vly_frm_form_requests.setStretch(1, 1)

        self.hly_page_frm_requests.addWidget(self.frm_form_requests)

        self.qsw_forms.addWidget(self.page_frm_requests)
        self.page_frm_job_titles = QWidget()
        self.page_frm_job_titles.setObjectName(u"page_frm_job_titles")
        sizePolicy.setHeightForWidth(self.page_frm_job_titles.sizePolicy().hasHeightForWidth())
        self.page_frm_job_titles.setSizePolicy(sizePolicy)
        self.page_frm_job_titles.setMinimumSize(QSize(825, 544))
        self.page_frm_job_titles.setMaximumSize(QSize(1920, 1080))
        self.page_frm_job_titles.setStyleSheet(u"")
        self.hly_page_frm_job_titles = QHBoxLayout(self.page_frm_job_titles)
        self.hly_page_frm_job_titles.setSpacing(0)
        self.hly_page_frm_job_titles.setObjectName(u"hly_page_frm_job_titles")
        self.hly_page_frm_job_titles.setContentsMargins(0, 0, 0, 0)
        self.frm_form_job_titles = QFrame(self.page_frm_job_titles)
        self.frm_form_job_titles.setObjectName(u"frm_form_job_titles")
        sizePolicy.setHeightForWidth(self.frm_form_job_titles.sizePolicy().hasHeightForWidth())
        self.frm_form_job_titles.setSizePolicy(sizePolicy)
        self.frm_form_job_titles.setMinimumSize(QSize(625, 0))
        self.frm_form_job_titles.setMaximumSize(QSize(1920, 1080))
        self.frm_form_job_titles.setStyleSheet(u"")
        self.frm_form_job_titles.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_job_titles.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_job_titles = QVBoxLayout(self.frm_form_job_titles)
        self.vly_frm_form_job_titles.setSpacing(3)
        self.vly_frm_form_job_titles.setObjectName(u"vly_frm_form_job_titles")
        self.vly_frm_form_job_titles.setContentsMargins(4, 4, 4, 4)
        self.frm_job_titles = QFrame(self.frm_form_job_titles)
        self.frm_job_titles.setObjectName(u"frm_job_titles")
        sizePolicy.setHeightForWidth(self.frm_job_titles.sizePolicy().hasHeightForWidth())
        self.frm_job_titles.setSizePolicy(sizePolicy)
        self.frm_job_titles.setMinimumSize(QSize(625, 433))
        self.frm_job_titles.setMaximumSize(QSize(625, 433))
        self.frm_job_titles.setStyleSheet(u"/* Estilos para la seccion de formularios */\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del marco */\n"
"QGroupBox {\n"
"    background-color: rgb(188, 246, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    color: #000000;                  /* Color del texto */\n"
"    font: bold 24pt \"Segoe UI\";     /* Fuente m\u00e1s grande y en negrita */\n"
"    subcontrol-origin: margin;      /* Posici\u00f3n del t\u00edtulo */\n"
"    subcontrol-position: top left;  /* Alineaci\u00f3n del t\u00edtulo */\n"
"    padding: 4px;                   /* Espacio alrededor del texto */\n"
"}\n"
"\n"
"/* Estilo de las etiquetas */\n"
"QLabel {\n"
"    color: #000000;                /* Color del texto */\n"
"    background-color: rgb(188, 246, 255); /* Opcional: fondo */\n"
"    font: 10pt \"Segoe UI\";        "
                        " /* Fuente de Etiquetas */\n"
"    line-height: 12px;\n"
"}\n"
"\n"
"/* Estilo de QTextEdit */\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QLineEdit */\n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Co"
                        "lor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QComboBox */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* Estilo de QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas r"
                        "edondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
"QComboBox:disabled, \n"
"QDateEdit:disabled, \n"
"QTimeEdit:disabled {\n"
"    background-color: #e1e1e1;\n"
"    color: #808080;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"\n"
"/* Forzamos el QTextEdit */\n"
"QTextEdit:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"/* Forzamos el QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_job_titles.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_job_titles.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_job_titles = QVBoxLayout(self.frm_job_titles)
        self.vly_job_titles.setSpacing(3)
        self.vly_job_titles.setObjectName(u"vly_job_titles")
        self.vly_job_titles.setContentsMargins(4, 4, 4, 4)
        self.grb_job_titles = QGroupBox(self.frm_job_titles)
        self.grb_job_titles.setObjectName(u"grb_job_titles")
        self.grb_job_titles.setMinimumSize(QSize(0, 0))
        self.grb_job_titles.setMaximumSize(QSize(16777215, 544))
        self.grb_job_titles.setStyleSheet(u"")
        self.label_job_codigo = QLabel(self.grb_job_titles)
        self.label_job_codigo.setObjectName(u"label_job_codigo")
        self.label_job_codigo.setGeometry(QRect(10, 30, 61, 20))
        self.label_job_codigo.setMaximumSize(QSize(100, 20))
        self.label_job_codigo.setAutoFillBackground(False)
        self.lineEdit_job_codigo = QLineEdit(self.grb_job_titles)
        self.lineEdit_job_codigo.setObjectName(u"lineEdit_job_codigo")
        self.lineEdit_job_codigo.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_job_codigo.setMaximumSize(QSize(100, 20))
        self.label_job_descripcion = QLabel(self.grb_job_titles)
        self.label_job_descripcion.setObjectName(u"label_job_descripcion")
        self.label_job_descripcion.setGeometry(QRect(10, 60, 90, 20))
        sizePolicy1.setHeightForWidth(self.label_job_descripcion.sizePolicy().hasHeightForWidth())
        self.label_job_descripcion.setSizePolicy(sizePolicy1)
        self.label_job_descripcion.setMinimumSize(QSize(80, 20))
        self.label_job_descripcion.setMaximumSize(QSize(100, 20))
        self.lineEdit_job_descripcion = QLineEdit(self.grb_job_titles)
        self.lineEdit_job_descripcion.setObjectName(u"lineEdit_job_descripcion")
        self.lineEdit_job_descripcion.setGeometry(QRect(101, 60, 400, 20))
        self.lineEdit_job_descripcion.setMinimumSize(QSize(400, 20))
        self.lineEdit_job_descripcion.setMaximumSize(QSize(400, 20))
        self.lineEdit_job_descripcion.setStyleSheet(u"")
        self.label_job_status = QLabel(self.grb_job_titles)
        self.label_job_status.setObjectName(u"label_job_status")
        self.label_job_status.setGeometry(QRect(458, 30, 50, 20))
        self.label_job_status.setMinimumSize(QSize(50, 20))
        self.label_job_status.setMaximumSize(QSize(50, 20))
        self.cmb_job_status = QComboBox(self.grb_job_titles)
        self.cmb_job_status.addItem("")
        self.cmb_job_status.addItem("")
        self.cmb_job_status.setObjectName(u"cmb_job_status")
        self.cmb_job_status.setGeometry(QRect(512, 30, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_job_status.sizePolicy().hasHeightForWidth())
        self.cmb_job_status.setSizePolicy(sizePolicy)
        self.cmb_job_status.setMinimumSize(QSize(80, 20))
        self.cmb_job_status.setMaximumSize(QSize(80, 20))
        self.cmb_job_status.setStyleSheet(u"")
        self.label_job_fechacreacion = QLabel(self.grb_job_titles)
        self.label_job_fechacreacion.setObjectName(u"label_job_fechacreacion")
        self.label_job_fechacreacion.setGeometry(QRect(10, 160, 130, 20))
        self.label_job_fechacreacion.setMinimumSize(QSize(130, 20))
        self.label_job_fechacreacion.setMaximumSize(QSize(130, 23))
        self.dateEdit_job_fechacreacion = QDateEdit(self.grb_job_titles)
        self.dateEdit_job_fechacreacion.setObjectName(u"dateEdit_job_fechacreacion")
        self.dateEdit_job_fechacreacion.setGeometry(QRect(140, 160, 100, 20))
        self.dateEdit_job_fechacreacion.setMaximumSize(QSize(100, 20))
        self.dateEdit_job_fechacreacion.setStyleSheet(u"")
        self.dateEdit_job_fechacreacion.setCalendarPopup(True)
        self.textEdit_job_descripciontec = QTextEdit(self.grb_job_titles)
        self.textEdit_job_descripciontec.setObjectName(u"textEdit_job_descripciontec")
        self.textEdit_job_descripciontec.setGeometry(QRect(101, 90, 400, 60))
        self.textEdit_job_descripciontec.setMinimumSize(QSize(400, 60))
        self.textEdit_job_descripciontec.setMaximumSize(QSize(400, 60))
        self.textEdit_job_descripciontec.setStyleSheet(u"")
        self.label_job_descripciontec = QLabel(self.grb_job_titles)
        self.label_job_descripciontec.setObjectName(u"label_job_descripciontec")
        self.label_job_descripciontec.setGeometry(QRect(10, 95, 80, 41))
        self.label_job_descripciontec.setMinimumSize(QSize(80, 0))
        self.label_job_descripciontec.setMaximumSize(QSize(100, 60))
        self.label_job_descripciontec.setScaledContents(False)

        self.vly_job_titles.addWidget(self.grb_job_titles)


        self.vly_frm_form_job_titles.addWidget(self.frm_job_titles)

        self.frm_bar_job_titles = QFrame(self.frm_form_job_titles)
        self.frm_bar_job_titles.setObjectName(u"frm_bar_job_titles")
        sizePolicy1.setHeightForWidth(self.frm_bar_job_titles.sizePolicy().hasHeightForWidth())
        self.frm_bar_job_titles.setSizePolicy(sizePolicy1)
        self.frm_bar_job_titles.setMinimumSize(QSize(629, 64))
        self.frm_bar_job_titles.setMaximumSize(QSize(629, 64))
        self.frm_bar_job_titles.setStyleSheet(u"/*Estilos para la barra de acciones*/\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(79, 179, 255);\n"
"    border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    min-width: 625px;\n"
"    max-width: 625px;\n"
"    min-height: 60px;\n"
"    max-height: 60px;\n"
"   \n"
"}\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"   border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    padding: 10px;\n"
"    font: 10pt ;\n"
"	font: 9pt \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    margin: 2px;               /* Espaciado uniforme alrededor */\n"
"}\n"
"\n"
"/* Estado hover */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estado p"
                        "resionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.frm_bar_job_titles.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bar_job_titles.setFrameShadow(QFrame.Shadow.Sunken)
        self.hly_frm_bar_job_titles = QHBoxLayout(self.frm_bar_job_titles)
        self.hly_frm_bar_job_titles.setSpacing(2)
        self.hly_frm_bar_job_titles.setObjectName(u"hly_frm_bar_job_titles")
        self.hly_frm_bar_job_titles.setContentsMargins(4, 4, 4, 4)
        self.btn_add_job_titles = QPushButton(self.frm_bar_job_titles)
        self.btn_add_job_titles.setObjectName(u"btn_add_job_titles")
        sizePolicy1.setHeightForWidth(self.btn_add_job_titles.sizePolicy().hasHeightForWidth())
        self.btn_add_job_titles.setSizePolicy(sizePolicy1)
        self.btn_add_job_titles.setMinimumSize(QSize(118, 48))
        self.btn_add_job_titles.setMaximumSize(QSize(118, 48))
        self.btn_add_job_titles.setFont(font4)
        self.btn_add_job_titles.setStyleSheet(u"")
        self.btn_add_job_titles.setIcon(icon37)
        self.btn_add_job_titles.setIconSize(QSize(22, 22))

        self.hly_frm_bar_job_titles.addWidget(self.btn_add_job_titles)

        self.btn_save_job_titles = QPushButton(self.frm_bar_job_titles)
        self.btn_save_job_titles.setObjectName(u"btn_save_job_titles")
        self.btn_save_job_titles.setMinimumSize(QSize(118, 48))
        self.btn_save_job_titles.setMaximumSize(QSize(118, 48))
        self.btn_save_job_titles.setFont(font4)
        self.btn_save_job_titles.setStyleSheet(u"")
        self.btn_save_job_titles.setIcon(icon38)
        self.btn_save_job_titles.setIconSize(QSize(22, 22))

        self.hly_frm_bar_job_titles.addWidget(self.btn_save_job_titles)

        self.btn_edit_job_titles = QPushButton(self.frm_bar_job_titles)
        self.btn_edit_job_titles.setObjectName(u"btn_edit_job_titles")
        sizePolicy1.setHeightForWidth(self.btn_edit_job_titles.sizePolicy().hasHeightForWidth())
        self.btn_edit_job_titles.setSizePolicy(sizePolicy1)
        self.btn_edit_job_titles.setMinimumSize(QSize(118, 48))
        self.btn_edit_job_titles.setMaximumSize(QSize(118, 48))
        self.btn_edit_job_titles.setFont(font4)
        self.btn_edit_job_titles.setStyleSheet(u"")
        self.btn_edit_job_titles.setIcon(icon39)
        self.btn_edit_job_titles.setIconSize(QSize(22, 22))

        self.hly_frm_bar_job_titles.addWidget(self.btn_edit_job_titles)

        self.btn_cancel_job_titles = QPushButton(self.frm_bar_job_titles)
        self.btn_cancel_job_titles.setObjectName(u"btn_cancel_job_titles")
        self.btn_cancel_job_titles.setMinimumSize(QSize(118, 48))
        self.btn_cancel_job_titles.setMaximumSize(QSize(118, 48))
        self.btn_cancel_job_titles.setFont(font4)
        self.btn_cancel_job_titles.setStyleSheet(u"")
        self.btn_cancel_job_titles.setIcon(icon40)
        self.btn_cancel_job_titles.setIconSize(QSize(22, 22))

        self.hly_frm_bar_job_titles.addWidget(self.btn_cancel_job_titles)

        self.btn_delete_job_titles = QPushButton(self.frm_bar_job_titles)
        self.btn_delete_job_titles.setObjectName(u"btn_delete_job_titles")
        sizePolicy1.setHeightForWidth(self.btn_delete_job_titles.sizePolicy().hasHeightForWidth())
        self.btn_delete_job_titles.setSizePolicy(sizePolicy1)
        self.btn_delete_job_titles.setMinimumSize(QSize(118, 48))
        self.btn_delete_job_titles.setMaximumSize(QSize(118, 48))
        self.btn_delete_job_titles.setStyleSheet(u"")
        self.btn_delete_job_titles.setIcon(icon41)
        self.btn_delete_job_titles.setIconSize(QSize(22, 22))

        self.hly_frm_bar_job_titles.addWidget(self.btn_delete_job_titles)


        self.vly_frm_form_job_titles.addWidget(self.frm_bar_job_titles)

        self.vly_frm_form_job_titles.setStretch(0, 4)
        self.vly_frm_form_job_titles.setStretch(1, 1)

        self.hly_page_frm_job_titles.addWidget(self.frm_form_job_titles)

        self.qsw_forms.addWidget(self.page_frm_job_titles)
        self.page_frm_functional_units = QWidget()
        self.page_frm_functional_units.setObjectName(u"page_frm_functional_units")
        sizePolicy.setHeightForWidth(self.page_frm_functional_units.sizePolicy().hasHeightForWidth())
        self.page_frm_functional_units.setSizePolicy(sizePolicy)
        self.page_frm_functional_units.setMinimumSize(QSize(825, 544))
        self.page_frm_functional_units.setMaximumSize(QSize(1920, 1080))
        self.page_frm_functional_units.setStyleSheet(u"")
        self.hly_page_frm_functional_units = QHBoxLayout(self.page_frm_functional_units)
        self.hly_page_frm_functional_units.setSpacing(0)
        self.hly_page_frm_functional_units.setObjectName(u"hly_page_frm_functional_units")
        self.hly_page_frm_functional_units.setContentsMargins(0, 0, 0, 0)
        self.frm_form_functional_units = QFrame(self.page_frm_functional_units)
        self.frm_form_functional_units.setObjectName(u"frm_form_functional_units")
        sizePolicy.setHeightForWidth(self.frm_form_functional_units.sizePolicy().hasHeightForWidth())
        self.frm_form_functional_units.setSizePolicy(sizePolicy)
        self.frm_form_functional_units.setMinimumSize(QSize(625, 0))
        self.frm_form_functional_units.setMaximumSize(QSize(1920, 1080))
        self.frm_form_functional_units.setStyleSheet(u"")
        self.frm_form_functional_units.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_functional_units.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_functional_units = QVBoxLayout(self.frm_form_functional_units)
        self.vly_frm_form_functional_units.setSpacing(3)
        self.vly_frm_form_functional_units.setObjectName(u"vly_frm_form_functional_units")
        self.vly_frm_form_functional_units.setContentsMargins(4, 4, 4, 4)
        self.frm_functional_units = QFrame(self.frm_form_functional_units)
        self.frm_functional_units.setObjectName(u"frm_functional_units")
        sizePolicy.setHeightForWidth(self.frm_functional_units.sizePolicy().hasHeightForWidth())
        self.frm_functional_units.setSizePolicy(sizePolicy)
        self.frm_functional_units.setMinimumSize(QSize(625, 433))
        self.frm_functional_units.setMaximumSize(QSize(625, 433))
        self.frm_functional_units.setStyleSheet(u"/* Estilos para la seccion de formularios */\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del marco */\n"
"QGroupBox {\n"
"    background-color: rgb(188, 246, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    color: #000000;                  /* Color del texto */\n"
"    font: bold 24pt \"Segoe UI\";     /* Fuente m\u00e1s grande y en negrita */\n"
"    subcontrol-origin: margin;      /* Posici\u00f3n del t\u00edtulo */\n"
"    subcontrol-position: top left;  /* Alineaci\u00f3n del t\u00edtulo */\n"
"    padding: 4px;                   /* Espacio alrededor del texto */\n"
"}\n"
"\n"
"/* Estilo de las etiquetas */\n"
"QLabel {\n"
"    color: #000000;                /* Color del texto */\n"
"    background-color: rgb(188, 246, 255); /* Opcional: fondo */\n"
"    font: 10pt \"Segoe UI\";        "
                        " /* Fuente de Etiquetas */\n"
"    line-height: 12px;\n"
"}\n"
"\n"
"/* Estilo de QTextEdit */\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QLineEdit */\n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Co"
                        "lor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QComboBox */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* Estilo de QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas r"
                        "edondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
"QComboBox:disabled, \n"
"QDateEdit:disabled, \n"
"QTimeEdit:disabled {\n"
"    background-color: #e1e1e1;\n"
"    color: #808080;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"\n"
"/* Forzamos el QTextEdit */\n"
"QTextEdit:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"/* Forzamos el QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_functional_units.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_functional_units.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_functional_units = QVBoxLayout(self.frm_functional_units)
        self.vly_functional_units.setSpacing(3)
        self.vly_functional_units.setObjectName(u"vly_functional_units")
        self.vly_functional_units.setContentsMargins(4, 4, 4, 4)
        self.grb_functional_units = QGroupBox(self.frm_functional_units)
        self.grb_functional_units.setObjectName(u"grb_functional_units")
        self.grb_functional_units.setMinimumSize(QSize(0, 0))
        self.grb_functional_units.setMaximumSize(QSize(16777215, 544))
        self.grb_functional_units.setStyleSheet(u"")
        self.label_fun_codigo = QLabel(self.grb_functional_units)
        self.label_fun_codigo.setObjectName(u"label_fun_codigo")
        self.label_fun_codigo.setGeometry(QRect(10, 30, 61, 20))
        self.label_fun_codigo.setMaximumSize(QSize(100, 20))
        self.label_fun_codigo.setAutoFillBackground(False)
        self.lineEdit_fun_codigo = QLineEdit(self.grb_functional_units)
        self.lineEdit_fun_codigo.setObjectName(u"lineEdit_fun_codigo")
        self.lineEdit_fun_codigo.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_fun_codigo.setMaximumSize(QSize(100, 20))
        self.label_fun_descripcion = QLabel(self.grb_functional_units)
        self.label_fun_descripcion.setObjectName(u"label_fun_descripcion")
        self.label_fun_descripcion.setGeometry(QRect(10, 70, 101, 20))
        self.label_fun_descripcion.setMaximumSize(QSize(150, 20))
        self.lineEdit_fun_descripcion = QLineEdit(self.grb_functional_units)
        self.lineEdit_fun_descripcion.setObjectName(u"lineEdit_fun_descripcion")
        self.lineEdit_fun_descripcion.setGeometry(QRect(120, 70, 400, 20))
        self.lineEdit_fun_descripcion.setMinimumSize(QSize(400, 20))
        self.lineEdit_fun_descripcion.setMaximumSize(QSize(400, 20))
        self.lineEdit_fun_descripcion.setStyleSheet(u"")
        self.label_fun_status = QLabel(self.grb_functional_units)
        self.label_fun_status.setObjectName(u"label_fun_status")
        self.label_fun_status.setGeometry(QRect(434, 30, 61, 20))
        self.label_fun_status.setMaximumSize(QSize(100, 20))
        self.cmb_fun_status = QComboBox(self.grb_functional_units)
        self.cmb_fun_status.addItem("")
        self.cmb_fun_status.addItem("")
        self.cmb_fun_status.setObjectName(u"cmb_fun_status")
        self.cmb_fun_status.setGeometry(QRect(498, 30, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_fun_status.sizePolicy().hasHeightForWidth())
        self.cmb_fun_status.setSizePolicy(sizePolicy)
        self.cmb_fun_status.setMinimumSize(QSize(80, 20))
        self.cmb_fun_status.setMaximumSize(QSize(80, 20))
        self.cmb_fun_status.setStyleSheet(u"")
        self.label_fun_fechacreacion = QLabel(self.grb_functional_units)
        self.label_fun_fechacreacion.setObjectName(u"label_fun_fechacreacion")
        self.label_fun_fechacreacion.setGeometry(QRect(12, 180, 130, 20))
        self.label_fun_fechacreacion.setMinimumSize(QSize(130, 20))
        self.label_fun_fechacreacion.setMaximumSize(QSize(130, 20))
        self.dateEdit_fun_fechacreacion = QDateEdit(self.grb_functional_units)
        self.dateEdit_fun_fechacreacion.setObjectName(u"dateEdit_fun_fechacreacion")
        self.dateEdit_fun_fechacreacion.setGeometry(QRect(142, 180, 100, 20))
        self.dateEdit_fun_fechacreacion.setMaximumSize(QSize(100, 20))
        self.dateEdit_fun_fechacreacion.setStyleSheet(u"")
        self.dateEdit_fun_fechacreacion.setCalendarPopup(True)
        self.label_fun_DescripcionTec = QLabel(self.grb_functional_units)
        self.label_fun_DescripcionTec.setObjectName(u"label_fun_DescripcionTec")
        self.label_fun_DescripcionTec.setGeometry(QRect(10, 100, 100, 41))
        self.label_fun_DescripcionTec.setMinimumSize(QSize(100, 0))
        self.label_fun_DescripcionTec.setMaximumSize(QSize(100, 60))
        self.label_fun_DescripcionTec.setScaledContents(False)
        self.textEdit_fun_descripciontec = QTextEdit(self.grb_functional_units)
        self.textEdit_fun_descripciontec.setObjectName(u"textEdit_fun_descripciontec")
        self.textEdit_fun_descripciontec.setGeometry(QRect(120, 100, 400, 60))
        self.textEdit_fun_descripciontec.setMinimumSize(QSize(400, 60))
        self.textEdit_fun_descripciontec.setMaximumSize(QSize(400, 60))
        self.textEdit_fun_descripciontec.setStyleSheet(u"")

        self.vly_functional_units.addWidget(self.grb_functional_units)


        self.vly_frm_form_functional_units.addWidget(self.frm_functional_units)

        self.frm_bar_functional_units = QFrame(self.frm_form_functional_units)
        self.frm_bar_functional_units.setObjectName(u"frm_bar_functional_units")
        sizePolicy1.setHeightForWidth(self.frm_bar_functional_units.sizePolicy().hasHeightForWidth())
        self.frm_bar_functional_units.setSizePolicy(sizePolicy1)
        self.frm_bar_functional_units.setMinimumSize(QSize(629, 64))
        self.frm_bar_functional_units.setMaximumSize(QSize(629, 64))
        self.frm_bar_functional_units.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frm_bar_functional_units.setStyleSheet(u"/*Estilos para la barra de acciones*/\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(79, 179, 255);\n"
"    border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    min-width: 625px;\n"
"    max-width: 625px;\n"
"    min-height: 60px;\n"
"    max-height: 60px;\n"
"   \n"
"}\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"   border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    padding: 10px;\n"
"    font: 10pt ;\n"
"	font: 9pt \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    margin: 2px;               /* Espaciado uniforme alrededor */\n"
"}\n"
"\n"
"/* Estado hover */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estado p"
                        "resionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.frm_bar_functional_units.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bar_functional_units.setFrameShadow(QFrame.Shadow.Sunken)
        self.hly_frm_bar_functional_units = QHBoxLayout(self.frm_bar_functional_units)
        self.hly_frm_bar_functional_units.setSpacing(2)
        self.hly_frm_bar_functional_units.setObjectName(u"hly_frm_bar_functional_units")
        self.hly_frm_bar_functional_units.setContentsMargins(4, 4, 4, 4)
        self.btn_add_functional_units = QPushButton(self.frm_bar_functional_units)
        self.btn_add_functional_units.setObjectName(u"btn_add_functional_units")
        sizePolicy1.setHeightForWidth(self.btn_add_functional_units.sizePolicy().hasHeightForWidth())
        self.btn_add_functional_units.setSizePolicy(sizePolicy1)
        self.btn_add_functional_units.setMinimumSize(QSize(118, 48))
        self.btn_add_functional_units.setMaximumSize(QSize(118, 48))
        self.btn_add_functional_units.setFont(font4)
        self.btn_add_functional_units.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_add_functional_units.setStyleSheet(u"")
        self.btn_add_functional_units.setIcon(icon37)
        self.btn_add_functional_units.setIconSize(QSize(22, 22))

        self.hly_frm_bar_functional_units.addWidget(self.btn_add_functional_units)

        self.btn_save_functional_units = QPushButton(self.frm_bar_functional_units)
        self.btn_save_functional_units.setObjectName(u"btn_save_functional_units")
        self.btn_save_functional_units.setMinimumSize(QSize(118, 48))
        self.btn_save_functional_units.setMaximumSize(QSize(118, 48))
        self.btn_save_functional_units.setFont(font4)
        self.btn_save_functional_units.setStyleSheet(u"")
        self.btn_save_functional_units.setIcon(icon38)
        self.btn_save_functional_units.setIconSize(QSize(22, 22))

        self.hly_frm_bar_functional_units.addWidget(self.btn_save_functional_units)

        self.btn_edit_functional_units = QPushButton(self.frm_bar_functional_units)
        self.btn_edit_functional_units.setObjectName(u"btn_edit_functional_units")
        sizePolicy1.setHeightForWidth(self.btn_edit_functional_units.sizePolicy().hasHeightForWidth())
        self.btn_edit_functional_units.setSizePolicy(sizePolicy1)
        self.btn_edit_functional_units.setMinimumSize(QSize(118, 48))
        self.btn_edit_functional_units.setMaximumSize(QSize(118, 48))
        self.btn_edit_functional_units.setFont(font4)
        self.btn_edit_functional_units.setStyleSheet(u"")
        self.btn_edit_functional_units.setIcon(icon39)
        self.btn_edit_functional_units.setIconSize(QSize(22, 22))

        self.hly_frm_bar_functional_units.addWidget(self.btn_edit_functional_units)

        self.btn_cancel_functional_units = QPushButton(self.frm_bar_functional_units)
        self.btn_cancel_functional_units.setObjectName(u"btn_cancel_functional_units")
        self.btn_cancel_functional_units.setMinimumSize(QSize(118, 48))
        self.btn_cancel_functional_units.setMaximumSize(QSize(118, 48))
        self.btn_cancel_functional_units.setFont(font4)
        self.btn_cancel_functional_units.setStyleSheet(u"")
        self.btn_cancel_functional_units.setIcon(icon40)
        self.btn_cancel_functional_units.setIconSize(QSize(22, 22))

        self.hly_frm_bar_functional_units.addWidget(self.btn_cancel_functional_units)

        self.btn_delete_functional_units = QPushButton(self.frm_bar_functional_units)
        self.btn_delete_functional_units.setObjectName(u"btn_delete_functional_units")
        sizePolicy1.setHeightForWidth(self.btn_delete_functional_units.sizePolicy().hasHeightForWidth())
        self.btn_delete_functional_units.setSizePolicy(sizePolicy1)
        self.btn_delete_functional_units.setMinimumSize(QSize(118, 48))
        self.btn_delete_functional_units.setMaximumSize(QSize(118, 48))
        self.btn_delete_functional_units.setStyleSheet(u"")
        self.btn_delete_functional_units.setIcon(icon41)
        self.btn_delete_functional_units.setIconSize(QSize(22, 22))

        self.hly_frm_bar_functional_units.addWidget(self.btn_delete_functional_units)


        self.vly_frm_form_functional_units.addWidget(self.frm_bar_functional_units)

        self.vly_frm_form_functional_units.setStretch(0, 4)
        self.vly_frm_form_functional_units.setStretch(1, 1)

        self.hly_page_frm_functional_units.addWidget(self.frm_form_functional_units)

        self.qsw_forms.addWidget(self.page_frm_functional_units)
        self.page_frm_a_company = QWidget()
        self.page_frm_a_company.setObjectName(u"page_frm_a_company")
        sizePolicy.setHeightForWidth(self.page_frm_a_company.sizePolicy().hasHeightForWidth())
        self.page_frm_a_company.setSizePolicy(sizePolicy)
        self.page_frm_a_company.setMinimumSize(QSize(825, 544))
        self.page_frm_a_company.setMaximumSize(QSize(1980, 1080))
        self.hly_page_frm_aaa_company = QHBoxLayout(self.page_frm_a_company)
        self.hly_page_frm_aaa_company.setSpacing(0)
        self.hly_page_frm_aaa_company.setObjectName(u"hly_page_frm_aaa_company")
        self.hly_page_frm_aaa_company.setContentsMargins(0, 0, 0, 0)
        self.frm_form_a_company = QFrame(self.page_frm_a_company)
        self.frm_form_a_company.setObjectName(u"frm_form_a_company")
        sizePolicy.setHeightForWidth(self.frm_form_a_company.sizePolicy().hasHeightForWidth())
        self.frm_form_a_company.setSizePolicy(sizePolicy)
        self.frm_form_a_company.setMinimumSize(QSize(625, 0))
        self.frm_form_a_company.setMaximumSize(QSize(1920, 1080))
        self.frm_form_a_company.setStyleSheet(u"")
        self.frm_form_a_company.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_a_company.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_clients_2 = QVBoxLayout(self.frm_form_a_company)
        self.vly_frm_form_clients_2.setSpacing(2)
        self.vly_frm_form_clients_2.setObjectName(u"vly_frm_form_clients_2")
        self.vly_frm_form_clients_2.setContentsMargins(4, 4, 4, 4)
        self.frm_a_company = QFrame(self.frm_form_a_company)
        self.frm_a_company.setObjectName(u"frm_a_company")
        sizePolicy.setHeightForWidth(self.frm_a_company.sizePolicy().hasHeightForWidth())
        self.frm_a_company.setSizePolicy(sizePolicy)
        self.frm_a_company.setMinimumSize(QSize(625, 450))
        self.frm_a_company.setMaximumSize(QSize(625, 450))
        self.frm_a_company.setStyleSheet(u"/* Estilos para la seccion de formularios */\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del marco */\n"
"QGroupBox {\n"
"    background-color: rgb(188, 246, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    color: #000000;                  /* Color del texto */\n"
"    font: bold 24pt \"Segoe UI\";     /* Fuente m\u00e1s grande y en negrita */\n"
"    subcontrol-origin: margin;      /* Posici\u00f3n del t\u00edtulo */\n"
"    subcontrol-position: top left;  /* Alineaci\u00f3n del t\u00edtulo */\n"
"    padding: 4px;                   /* Espacio alrededor del texto */\n"
"}\n"
"\n"
"/* Estilo de las etiquetas */\n"
"QLabel {\n"
"    color: #000000;                /* Color del texto */\n"
"    background-color: rgb(188, 246, 255); /* Opcional: fondo */\n"
"    font: 10pt \"Segoe UI\";        "
                        " /* Fuente de Etiquetas */\n"
"    line-height: 12px;\n"
"}\n"
"\n"
"/* Estilo de QTextEdit */\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QLineEdit */\n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Co"
                        "lor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QComboBox */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* Estilo de QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas r"
                        "edondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
"QComboBox:disabled, \n"
"QDateEdit:disabled, \n"
"QTimeEdit:disabled {\n"
"    background-color: #e1e1e1;\n"
"    color: #808080;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"\n"
"/* Forzamos el QTextEdit */\n"
"QTextEdit:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"/* Forzamos el QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_a_company.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_a_company.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_a_company = QVBoxLayout(self.frm_a_company)
        self.vly_frm_a_company.setSpacing(3)
        self.vly_frm_a_company.setObjectName(u"vly_frm_a_company")
        self.vly_frm_a_company.setContentsMargins(4, 4, 4, 4)
        self.grb_datos_generales = QGroupBox(self.frm_a_company)
        self.grb_datos_generales.setObjectName(u"grb_datos_generales")
        self.grb_datos_generales.setMinimumSize(QSize(0, 0))
        self.grb_datos_generales.setMaximumSize(QSize(16777215, 544))
        self.grb_datos_generales.setStyleSheet(u"")
        self.label_emp_codigo = QLabel(self.grb_datos_generales)
        self.label_emp_codigo.setObjectName(u"label_emp_codigo")
        self.label_emp_codigo.setGeometry(QRect(10, 30, 61, 20))
        self.label_emp_codigo.setMaximumSize(QSize(100, 20))
        self.label_emp_codigo.setAutoFillBackground(False)
        self.lineEdit_emp_codigo = QLineEdit(self.grb_datos_generales)
        self.lineEdit_emp_codigo.setObjectName(u"lineEdit_emp_codigo")
        self.lineEdit_emp_codigo.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_emp_codigo.setMaximumSize(QSize(100, 20))
        self.label_emp_descripcion = QLabel(self.grb_datos_generales)
        self.label_emp_descripcion.setObjectName(u"label_emp_descripcion")
        self.label_emp_descripcion.setGeometry(QRect(10, 60, 101, 20))
        self.label_emp_descripcion.setMaximumSize(QSize(150, 20))
        self.lineEdit_emp_descripcion = QLineEdit(self.grb_datos_generales)
        self.lineEdit_emp_descripcion.setObjectName(u"lineEdit_emp_descripcion")
        self.lineEdit_emp_descripcion.setGeometry(QRect(120, 60, 400, 20))
        self.lineEdit_emp_descripcion.setMinimumSize(QSize(400, 20))
        self.lineEdit_emp_descripcion.setMaximumSize(QSize(400, 20))
        self.lineEdit_emp_descripcion.setStyleSheet(u"")
        self.label_emp_idfiscal = QLabel(self.grb_datos_generales)
        self.label_emp_idfiscal.setObjectName(u"label_emp_idfiscal")
        self.label_emp_idfiscal.setGeometry(QRect(10, 90, 115, 20))
        self.label_emp_idfiscal.setMinimumSize(QSize(115, 0))
        self.label_emp_idfiscal.setMaximumSize(QSize(110, 20))
        self.label_emp_status = QLabel(self.grb_datos_generales)
        self.label_emp_status.setObjectName(u"label_emp_status")
        self.label_emp_status.setGeometry(QRect(457, 30, 50, 20))
        self.label_emp_status.setMinimumSize(QSize(50, 20))
        self.label_emp_status.setMaximumSize(QSize(50, 20))
        self.lineEdit_emp_idfiscal = QLineEdit(self.grb_datos_generales)
        self.lineEdit_emp_idfiscal.setObjectName(u"lineEdit_emp_idfiscal")
        self.lineEdit_emp_idfiscal.setGeometry(QRect(133, 90, 100, 20))
        self.lineEdit_emp_idfiscal.setMaximumSize(QSize(100, 20))
        self.cmb_emp_ststus = QComboBox(self.grb_datos_generales)
        self.cmb_emp_ststus.addItem("")
        self.cmb_emp_ststus.addItem("")
        self.cmb_emp_ststus.setObjectName(u"cmb_emp_ststus")
        self.cmb_emp_ststus.setGeometry(QRect(512, 30, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_emp_ststus.sizePolicy().hasHeightForWidth())
        self.cmb_emp_ststus.setSizePolicy(sizePolicy)
        self.cmb_emp_ststus.setMinimumSize(QSize(80, 20))
        self.cmb_emp_ststus.setMaximumSize(QSize(80, 20))
        self.cmb_emp_ststus.setStyleSheet(u"")
        self.cmb_emp_tipo_contribuyente = QComboBox(self.grb_datos_generales)
        self.cmb_emp_tipo_contribuyente.addItem("")
        self.cmb_emp_tipo_contribuyente.addItem("")
        self.cmb_emp_tipo_contribuyente.setObjectName(u"cmb_emp_tipo_contribuyente")
        self.cmb_emp_tipo_contribuyente.setGeometry(QRect(512, 90, 100, 20))
        sizePolicy.setHeightForWidth(self.cmb_emp_tipo_contribuyente.sizePolicy().hasHeightForWidth())
        self.cmb_emp_tipo_contribuyente.setSizePolicy(sizePolicy)
        self.cmb_emp_tipo_contribuyente.setMaximumSize(QSize(100, 20))
        self.cmb_emp_tipo_contribuyente.setStyleSheet(u"")
        self.label_emp_tipo_contribuyente = QLabel(self.grb_datos_generales)
        self.label_emp_tipo_contribuyente.setObjectName(u"label_emp_tipo_contribuyente")
        self.label_emp_tipo_contribuyente.setGeometry(QRect(387, 90, 120, 20))
        self.label_emp_tipo_contribuyente.setMinimumSize(QSize(120, 20))
        self.label_emp_tipo_contribuyente.setMaximumSize(QSize(120, 20))

        self.vly_frm_a_company.addWidget(self.grb_datos_generales)

        self.grb_direccion_telefonos = QGroupBox(self.frm_a_company)
        self.grb_direccion_telefonos.setObjectName(u"grb_direccion_telefonos")
        self.grb_direccion_telefonos.setMinimumSize(QSize(0, 0))
        self.grb_direccion_telefonos.setStyleSheet(u"")
        self.textEdit_emp_direccionf = QTextEdit(self.grb_direccion_telefonos)
        self.textEdit_emp_direccionf.setObjectName(u"textEdit_emp_direccionf")
        self.textEdit_emp_direccionf.setGeometry(QRect(87, 22, 200, 60))
        self.textEdit_emp_direccionf.setMinimumSize(QSize(200, 60))
        self.textEdit_emp_direccionf.setMaximumSize(QSize(200, 60))
        self.textEdit_emp_direccionf.setStyleSheet(u"")
        self.label_emp_DireccionF = QLabel(self.grb_direccion_telefonos)
        self.label_emp_DireccionF.setObjectName(u"label_emp_DireccionF")
        self.label_emp_DireccionF.setGeometry(QRect(10, 22, 71, 41))
        self.label_emp_DireccionF.setScaledContents(False)
        self.label_emp_Direccionl = QLabel(self.grb_direccion_telefonos)
        self.label_emp_Direccionl.setObjectName(u"label_emp_Direccionl")
        self.label_emp_Direccionl.setGeometry(QRect(310, 22, 71, 41))
        self.textEdit_emp_direccionl = QTextEdit(self.grb_direccion_telefonos)
        self.textEdit_emp_direccionl.setObjectName(u"textEdit_emp_direccionl")
        self.textEdit_emp_direccionl.setGeometry(QRect(386, 22, 200, 60))
        self.textEdit_emp_direccionl.setMinimumSize(QSize(200, 60))
        self.textEdit_emp_direccionl.setMaximumSize(QSize(200, 60))
        self.textEdit_emp_direccionl.setStyleSheet(u"")
        self.label_emp_telefono1 = QLabel(self.grb_direccion_telefonos)
        self.label_emp_telefono1.setObjectName(u"label_emp_telefono1")
        self.label_emp_telefono1.setGeometry(QRect(10, 88, 101, 20))
        self.label_emp_telefono1.setMaximumSize(QSize(150, 20))
        self.label_emp_telefono2 = QLabel(self.grb_direccion_telefonos)
        self.label_emp_telefono2.setObjectName(u"label_emp_telefono2")
        self.label_emp_telefono2.setGeometry(QRect(310, 88, 101, 20))
        self.label_emp_telefono2.setMaximumSize(QSize(150, 20))
        self.lineEdit_emp_telefono1 = QLineEdit(self.grb_direccion_telefonos)
        self.lineEdit_emp_telefono1.setObjectName(u"lineEdit_emp_telefono1")
        self.lineEdit_emp_telefono1.setGeometry(QRect(119, 88, 165, 20))
        self.lineEdit_emp_telefono1.setMinimumSize(QSize(165, 0))
        self.lineEdit_emp_telefono1.setMaximumSize(QSize(165, 20))
        self.lineEdit_emp_telefono2 = QLineEdit(self.grb_direccion_telefonos)
        self.lineEdit_emp_telefono2.setObjectName(u"lineEdit_emp_telefono2")
        self.lineEdit_emp_telefono2.setGeometry(QRect(419, 88, 165, 20))
        self.lineEdit_emp_telefono2.setMinimumSize(QSize(165, 0))
        self.lineEdit_emp_telefono2.setMaximumSize(QSize(165, 20))
        self.label_emp_EmailEmpresa = QLabel(self.grb_direccion_telefonos)
        self.label_emp_EmailEmpresa.setObjectName(u"label_emp_EmailEmpresa")
        self.label_emp_EmailEmpresa.setGeometry(QRect(10, 115, 101, 20))
        self.label_emp_EmailEmpresa.setMaximumSize(QSize(150, 20))
        self.lineEdit_emp_EmailEmpresa = QLineEdit(self.grb_direccion_telefonos)
        self.lineEdit_emp_EmailEmpresa.setObjectName(u"lineEdit_emp_EmailEmpresa")
        self.lineEdit_emp_EmailEmpresa.setGeometry(QRect(119, 115, 260, 20))
        self.lineEdit_emp_EmailEmpresa.setMinimumSize(QSize(260, 0))
        self.lineEdit_emp_EmailEmpresa.setMaximumSize(QSize(260, 20))

        self.vly_frm_a_company.addWidget(self.grb_direccion_telefonos)

        self.grb_sontactos = QGroupBox(self.frm_a_company)
        self.grb_sontactos.setObjectName(u"grb_sontactos")
        self.grb_sontactos.setMinimumSize(QSize(0, 0))
        self.grb_sontactos.setStyleSheet(u"")
        self.label_emp_representante = QLabel(self.grb_sontactos)
        self.label_emp_representante.setObjectName(u"label_emp_representante")
        self.label_emp_representante.setGeometry(QRect(10, 20, 150, 20))
        self.label_emp_representante.setMinimumSize(QSize(150, 20))
        self.label_emp_representante.setMaximumSize(QSize(150, 20))
        self.lineEdit_emp_representante = QLineEdit(self.grb_sontactos)
        self.lineEdit_emp_representante.setObjectName(u"lineEdit_emp_representante")
        self.lineEdit_emp_representante.setGeometry(QRect(162, 20, 260, 20))
        self.lineEdit_emp_representante.setMinimumSize(QSize(260, 0))
        self.lineEdit_emp_representante.setMaximumSize(QSize(260, 20))
        self.lineEdit_emp_representante.setStyleSheet(u"")
        self.label_emp_idrepresentante = QLabel(self.grb_sontactos)
        self.label_emp_idrepresentante.setObjectName(u"label_emp_idrepresentante")
        self.label_emp_idrepresentante.setGeometry(QRect(430, 20, 50, 20))
        self.label_emp_idrepresentante.setMinimumSize(QSize(50, 0))
        self.label_emp_idrepresentante.setMaximumSize(QSize(50, 20))
        self.lineEdit_emp_idrepresentante = QLineEdit(self.grb_sontactos)
        self.lineEdit_emp_idrepresentante.setObjectName(u"lineEdit_emp_idrepresentante")
        self.lineEdit_emp_idrepresentante.setGeometry(QRect(485, 20, 100, 20))
        self.lineEdit_emp_idrepresentante.setMaximumSize(QSize(100, 20))
        self.lineEdit_emp_TelefonoContacto = QLineEdit(self.grb_sontactos)
        self.lineEdit_emp_TelefonoContacto.setObjectName(u"lineEdit_emp_TelefonoContacto")
        self.lineEdit_emp_TelefonoContacto.setGeometry(QRect(162, 50, 165, 20))
        self.lineEdit_emp_TelefonoContacto.setMinimumSize(QSize(165, 0))
        self.lineEdit_emp_TelefonoContacto.setMaximumSize(QSize(165, 20))
        self.label_emp_TelefonoContacto = QLabel(self.grb_sontactos)
        self.label_emp_TelefonoContacto.setObjectName(u"label_emp_TelefonoContacto")
        self.label_emp_TelefonoContacto.setGeometry(QRect(10, 50, 150, 20))
        self.label_emp_TelefonoContacto.setMinimumSize(QSize(150, 0))
        self.label_emp_TelefonoContacto.setMaximumSize(QSize(150, 20))
        self.lineEdit_emp_EmailContacto = QLineEdit(self.grb_sontactos)
        self.lineEdit_emp_EmailContacto.setObjectName(u"lineEdit_emp_EmailContacto")
        self.lineEdit_emp_EmailContacto.setGeometry(QRect(162, 80, 260, 20))
        self.lineEdit_emp_EmailContacto.setMinimumSize(QSize(260, 0))
        self.lineEdit_emp_EmailContacto.setMaximumSize(QSize(260, 20))
        self.label_emp_EmailContacto = QLabel(self.grb_sontactos)
        self.label_emp_EmailContacto.setObjectName(u"label_emp_EmailContacto")
        self.label_emp_EmailContacto.setGeometry(QRect(10, 80, 101, 20))
        self.label_emp_EmailContacto.setMaximumSize(QSize(150, 20))
        self.dateEdit_creation_company = QDateEdit(self.grb_sontactos)
        self.dateEdit_creation_company.setObjectName(u"dateEdit_creation_company")
        self.dateEdit_creation_company.setGeometry(QRect(512, 110, 100, 20))
        self.dateEdit_creation_company.setMaximumSize(QSize(100, 20))
        self.dateEdit_creation_company.setStyleSheet(u"")
        self.dateEdit_creation_company.setCalendarPopup(True)
        self.label_emp_creation_company = QLabel(self.grb_sontactos)
        self.label_emp_creation_company.setObjectName(u"label_emp_creation_company")
        self.label_emp_creation_company.setGeometry(QRect(391, 110, 120, 20))
        self.label_emp_creation_company.setMaximumSize(QSize(130, 20))

        self.vly_frm_a_company.addWidget(self.grb_sontactos)


        self.vly_frm_form_clients_2.addWidget(self.frm_a_company)

        self.frm_bar_a_company = QFrame(self.frm_form_a_company)
        self.frm_bar_a_company.setObjectName(u"frm_bar_a_company")
        sizePolicy1.setHeightForWidth(self.frm_bar_a_company.sizePolicy().hasHeightForWidth())
        self.frm_bar_a_company.setSizePolicy(sizePolicy1)
        self.frm_bar_a_company.setMinimumSize(QSize(629, 64))
        self.frm_bar_a_company.setMaximumSize(QSize(629, 64))
        self.frm_bar_a_company.setStyleSheet(u"/*Estilos para la barra de acciones*/\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(79, 179, 255);\n"
"    border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    min-width: 625px;\n"
"    max-width: 625px;\n"
"    min-height: 60px;\n"
"    max-height: 60px;\n"
"   \n"
"}\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"   border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    padding: 10px;\n"
"    font: 10pt ;\n"
"	font: 9pt \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    margin: 2px;               /* Espaciado uniforme alrededor */\n"
"}\n"
"\n"
"/* Estado hover */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estado p"
                        "resionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.frm_bar_a_company.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bar_a_company.setFrameShadow(QFrame.Shadow.Sunken)
        self.hly_frm_bar_clients_2 = QHBoxLayout(self.frm_bar_a_company)
        self.hly_frm_bar_clients_2.setSpacing(2)
        self.hly_frm_bar_clients_2.setObjectName(u"hly_frm_bar_clients_2")
        self.hly_frm_bar_clients_2.setContentsMargins(4, 4, 4, 4)
        self.btn_add_a_company = QPushButton(self.frm_bar_a_company)
        self.btn_add_a_company.setObjectName(u"btn_add_a_company")
        sizePolicy1.setHeightForWidth(self.btn_add_a_company.sizePolicy().hasHeightForWidth())
        self.btn_add_a_company.setSizePolicy(sizePolicy1)
        self.btn_add_a_company.setMinimumSize(QSize(118, 48))
        self.btn_add_a_company.setMaximumSize(QSize(118, 48))
        self.btn_add_a_company.setFont(font4)
        self.btn_add_a_company.setStyleSheet(u"")
        self.btn_add_a_company.setIcon(icon37)
        self.btn_add_a_company.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients_2.addWidget(self.btn_add_a_company)

        self.btn_save_a_company = QPushButton(self.frm_bar_a_company)
        self.btn_save_a_company.setObjectName(u"btn_save_a_company")
        self.btn_save_a_company.setMinimumSize(QSize(118, 48))
        self.btn_save_a_company.setMaximumSize(QSize(118, 48))
        self.btn_save_a_company.setFont(font4)
        self.btn_save_a_company.setStyleSheet(u"")
        self.btn_save_a_company.setIcon(icon38)
        self.btn_save_a_company.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients_2.addWidget(self.btn_save_a_company)

        self.btn_edit_a_company = QPushButton(self.frm_bar_a_company)
        self.btn_edit_a_company.setObjectName(u"btn_edit_a_company")
        sizePolicy1.setHeightForWidth(self.btn_edit_a_company.sizePolicy().hasHeightForWidth())
        self.btn_edit_a_company.setSizePolicy(sizePolicy1)
        self.btn_edit_a_company.setMinimumSize(QSize(118, 48))
        self.btn_edit_a_company.setMaximumSize(QSize(118, 48))
        self.btn_edit_a_company.setFont(font4)
        self.btn_edit_a_company.setStyleSheet(u"")
        self.btn_edit_a_company.setIcon(icon39)
        self.btn_edit_a_company.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients_2.addWidget(self.btn_edit_a_company)

        self.btn_cancel_a_company = QPushButton(self.frm_bar_a_company)
        self.btn_cancel_a_company.setObjectName(u"btn_cancel_a_company")
        self.btn_cancel_a_company.setMinimumSize(QSize(118, 48))
        self.btn_cancel_a_company.setMaximumSize(QSize(118, 48))
        self.btn_cancel_a_company.setFont(font4)
        self.btn_cancel_a_company.setStyleSheet(u"")
        self.btn_cancel_a_company.setIcon(icon40)
        self.btn_cancel_a_company.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients_2.addWidget(self.btn_cancel_a_company)

        self.btn_delete_a_company = QPushButton(self.frm_bar_a_company)
        self.btn_delete_a_company.setObjectName(u"btn_delete_a_company")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_delete_a_company.sizePolicy().hasHeightForWidth())
        self.btn_delete_a_company.setSizePolicy(sizePolicy5)
        self.btn_delete_a_company.setMinimumSize(QSize(118, 48))
        self.btn_delete_a_company.setMaximumSize(QSize(118, 48))
        self.btn_delete_a_company.setStyleSheet(u"")
        self.btn_delete_a_company.setIcon(icon41)
        self.btn_delete_a_company.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients_2.addWidget(self.btn_delete_a_company)


        self.vly_frm_form_clients_2.addWidget(self.frm_bar_a_company)


        self.hly_page_frm_aaa_company.addWidget(self.frm_form_a_company)

        self.qsw_forms.addWidget(self.page_frm_a_company)
        self.page_frm_zz_opcional = QWidget()
        self.page_frm_zz_opcional.setObjectName(u"page_frm_zz_opcional")
        self.page_frm_zz_opcional.setEnabled(False)
        sizePolicy.setHeightForWidth(self.page_frm_zz_opcional.sizePolicy().hasHeightForWidth())
        self.page_frm_zz_opcional.setSizePolicy(sizePolicy)
        self.page_frm_zz_opcional.setMinimumSize(QSize(825, 544))
        self.page_frm_zz_opcional.setMaximumSize(QSize(1920, 1080))
        self.page_frm_zz_opcional.setStyleSheet(u"")
        self.hly_frm_company = QHBoxLayout(self.page_frm_zz_opcional)
        self.hly_frm_company.setSpacing(0)
        self.hly_frm_company.setObjectName(u"hly_frm_company")
        self.hly_frm_company.setContentsMargins(0, 0, 0, 0)
        self.frm_form_zz_opcional = QFrame(self.page_frm_zz_opcional)
        self.frm_form_zz_opcional.setObjectName(u"frm_form_zz_opcional")
        self.frm_form_zz_opcional.setEnabled(False)
        sizePolicy.setHeightForWidth(self.frm_form_zz_opcional.sizePolicy().hasHeightForWidth())
        self.frm_form_zz_opcional.setSizePolicy(sizePolicy)
        self.frm_form_zz_opcional.setMinimumSize(QSize(625, 0))
        self.frm_form_zz_opcional.setMaximumSize(QSize(1920, 1080))
        self.frm_form_zz_opcional.setFont(font2)
        self.frm_form_zz_opcional.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frm_form_zz_opcional.setStyleSheet(u"")
        self.frm_form_zz_opcional.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_zz_opcional.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_company = QVBoxLayout(self.frm_form_zz_opcional)
        self.vly_frm_form_company.setSpacing(2)
        self.vly_frm_form_company.setObjectName(u"vly_frm_form_company")
        self.vly_frm_form_company.setContentsMargins(4, 4, 4, 4)

        self.hly_frm_company.addWidget(self.frm_form_zz_opcional)

        self.qsw_forms.addWidget(self.page_frm_zz_opcional)
        self.page_frm_actions = QWidget()
        self.page_frm_actions.setObjectName(u"page_frm_actions")
        sizePolicy.setHeightForWidth(self.page_frm_actions.sizePolicy().hasHeightForWidth())
        self.page_frm_actions.setSizePolicy(sizePolicy)
        self.page_frm_actions.setMinimumSize(QSize(825, 544))
        self.page_frm_actions.setMaximumSize(QSize(1920, 1080))
        self.page_frm_actions.setStyleSheet(u"")
        self.hly_frm__actions = QHBoxLayout(self.page_frm_actions)
        self.hly_frm__actions.setSpacing(0)
        self.hly_frm__actions.setObjectName(u"hly_frm__actions")
        self.hly_frm__actions.setContentsMargins(0, 0, 0, 0)
        self.frm_form_action = QFrame(self.page_frm_actions)
        self.frm_form_action.setObjectName(u"frm_form_action")
        sizePolicy.setHeightForWidth(self.frm_form_action.sizePolicy().hasHeightForWidth())
        self.frm_form_action.setSizePolicy(sizePolicy)
        self.frm_form_action.setMinimumSize(QSize(625, 0))
        self.frm_form_action.setMaximumSize(QSize(1920, 1080))
        self.frm_form_action.setFont(font2)
        self.frm_form_action.setStyleSheet(u"")
        self.frm_form_action.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_action.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_action = QVBoxLayout(self.frm_form_action)
        self.vly_frm_form_action.setSpacing(3)
        self.vly_frm_form_action.setObjectName(u"vly_frm_form_action")
        self.vly_frm_form_action.setContentsMargins(4, 4, 4, 4)
        self.frm_actions = QFrame(self.frm_form_action)
        self.frm_actions.setObjectName(u"frm_actions")
        sizePolicy.setHeightForWidth(self.frm_actions.sizePolicy().hasHeightForWidth())
        self.frm_actions.setSizePolicy(sizePolicy)
        self.frm_actions.setMinimumSize(QSize(625, 433))
        self.frm_actions.setMaximumSize(QSize(625, 433))
        self.frm_actions.setStyleSheet(u"/* Estilos para la seccion de formularios */\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del marco */\n"
"QGroupBox {\n"
"    background-color: rgb(188, 246, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    color: #000000;                  /* Color del texto */\n"
"    font: bold 24pt \"Segoe UI\";     /* Fuente m\u00e1s grande y en negrita */\n"
"    subcontrol-origin: margin;      /* Posici\u00f3n del t\u00edtulo */\n"
"    subcontrol-position: top left;  /* Alineaci\u00f3n del t\u00edtulo */\n"
"    padding: 4px;                   /* Espacio alrededor del texto */\n"
"}\n"
"\n"
"/* Estilo de las etiquetas */\n"
"QLabel {\n"
"    color: #000000;                /* Color del texto */\n"
"    background-color: rgb(188, 246, 255); /* Opcional: fondo */\n"
"    font: 10pt \"Segoe UI\";        "
                        " /* Fuente de Etiquetas */\n"
"    line-height: 12px;\n"
"}\n"
"\n"
"/* Estilo de QTextEdit */\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QLineEdit */\n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Co"
                        "lor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QComboBox */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* Estilo de QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas r"
                        "edondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
"QComboBox:disabled, \n"
"QDateEdit:disabled, \n"
"QTimeEdit:disabled {\n"
"    background-color: #e1e1e1;\n"
"    color: #808080;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"\n"
"/* Forzamos el QTextEdit */\n"
"QTextEdit:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"/* Forzamos el QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_actions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_actions.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_action = QVBoxLayout(self.frm_actions)
        self.vly_action.setSpacing(3)
        self.vly_action.setObjectName(u"vly_action")
        self.vly_action.setContentsMargins(4, 4, 4, 4)
        self.grb_frm_actions = QGroupBox(self.frm_actions)
        self.grb_frm_actions.setObjectName(u"grb_frm_actions")
        self.grb_frm_actions.setMinimumSize(QSize(0, 0))
        self.grb_frm_actions.setMaximumSize(QSize(16777215, 544))
        self.grb_frm_actions.setStyleSheet(u"")
        self.label_act_codigo = QLabel(self.grb_frm_actions)
        self.label_act_codigo.setObjectName(u"label_act_codigo")
        self.label_act_codigo.setGeometry(QRect(10, 30, 61, 20))
        self.label_act_codigo.setMaximumSize(QSize(100, 20))
        self.label_act_codigo.setAutoFillBackground(False)
        self.lineEdit_act_codigo = QLineEdit(self.grb_frm_actions)
        self.lineEdit_act_codigo.setObjectName(u"lineEdit_act_codigo")
        self.lineEdit_act_codigo.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_act_codigo.setMaximumSize(QSize(100, 20))
        self.label_act_descripcion = QLabel(self.grb_frm_actions)
        self.label_act_descripcion.setObjectName(u"label_act_descripcion")
        self.label_act_descripcion.setGeometry(QRect(10, 60, 101, 20))
        self.label_act_descripcion.setMaximumSize(QSize(150, 20))
        self.lineEdit_act_descripcion = QLineEdit(self.grb_frm_actions)
        self.lineEdit_act_descripcion.setObjectName(u"lineEdit_act_descripcion")
        self.lineEdit_act_descripcion.setGeometry(QRect(120, 60, 400, 20))
        self.lineEdit_act_descripcion.setMinimumSize(QSize(400, 20))
        self.lineEdit_act_descripcion.setMaximumSize(QSize(400, 20))
        self.lineEdit_act_descripcion.setStyleSheet(u"")
        self.label_id_category = QLabel(self.grb_frm_actions)
        self.label_id_category.setObjectName(u"label_id_category")
        self.label_id_category.setGeometry(QRect(10, 90, 101, 20))
        self.label_id_category.setMinimumSize(QSize(101, 0))
        self.label_id_category.setMaximumSize(QSize(101, 20))
        self.label_act_status = QLabel(self.grb_frm_actions)
        self.label_act_status.setObjectName(u"label_act_status")
        self.label_act_status.setGeometry(QRect(364, 30, 61, 20))
        self.label_act_status.setMaximumSize(QSize(100, 20))
        self.lineEdit_id_category = QLineEdit(self.grb_frm_actions)
        self.lineEdit_id_category.setObjectName(u"lineEdit_id_category")
        self.lineEdit_id_category.setGeometry(QRect(120, 90, 400, 20))
        self.lineEdit_id_category.setMinimumSize(QSize(400, 20))
        self.lineEdit_id_category.setMaximumSize(QSize(400, 20))
        self.cmb_act_status = QComboBox(self.grb_frm_actions)
        self.cmb_act_status.addItem("")
        self.cmb_act_status.addItem("")
        self.cmb_act_status.setObjectName(u"cmb_act_status")
        self.cmb_act_status.setGeometry(QRect(434, 30, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_act_status.sizePolicy().hasHeightForWidth())
        self.cmb_act_status.setSizePolicy(sizePolicy)
        self.cmb_act_status.setMinimumSize(QSize(80, 20))
        self.cmb_act_status.setMaximumSize(QSize(80, 20))
        self.cmb_act_status.setStyleSheet(u"")
        self.label_act_fechacreacion = QLabel(self.grb_frm_actions)
        self.label_act_fechacreacion.setObjectName(u"label_act_fechacreacion")
        self.label_act_fechacreacion.setGeometry(QRect(10, 190, 130, 20))
        self.label_act_fechacreacion.setMaximumSize(QSize(130, 20))
        self.dateEdit_act_fechacreacion = QDateEdit(self.grb_frm_actions)
        self.dateEdit_act_fechacreacion.setObjectName(u"dateEdit_act_fechacreacion")
        self.dateEdit_act_fechacreacion.setGeometry(QRect(146, 190, 100, 20))
        self.dateEdit_act_fechacreacion.setMaximumSize(QSize(100, 20))
        self.dateEdit_act_fechacreacion.setStyleSheet(u"")
        self.dateEdit_act_fechacreacion.setCalendarPopup(True)
        self.label_act_descripciontec = QLabel(self.grb_frm_actions)
        self.label_act_descripciontec.setObjectName(u"label_act_descripciontec")
        self.label_act_descripciontec.setGeometry(QRect(10, 120, 100, 41))
        self.label_act_descripciontec.setMinimumSize(QSize(100, 0))
        self.label_act_descripciontec.setMaximumSize(QSize(100, 60))
        self.label_act_descripciontec.setScaledContents(False)
        self.textEdit_act_descripciontec = QTextEdit(self.grb_frm_actions)
        self.textEdit_act_descripciontec.setObjectName(u"textEdit_act_descripciontec")
        self.textEdit_act_descripciontec.setGeometry(QRect(120, 120, 400, 60))
        self.textEdit_act_descripciontec.setMinimumSize(QSize(400, 60))
        self.textEdit_act_descripciontec.setMaximumSize(QSize(400, 60))
        self.textEdit_act_descripciontec.setStyleSheet(u"")

        self.vly_action.addWidget(self.grb_frm_actions)


        self.vly_frm_form_action.addWidget(self.frm_actions)

        self.frm_bar_action = QFrame(self.frm_form_action)
        self.frm_bar_action.setObjectName(u"frm_bar_action")
        sizePolicy.setHeightForWidth(self.frm_bar_action.sizePolicy().hasHeightForWidth())
        self.frm_bar_action.setSizePolicy(sizePolicy)
        self.frm_bar_action.setMinimumSize(QSize(629, 64))
        self.frm_bar_action.setMaximumSize(QSize(629, 64))
        self.frm_bar_action.setStyleSheet(u"/*Estilos para la barra de acciones*/\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(79, 179, 255);\n"
"    border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    min-width: 625px;\n"
"    max-width: 625px;\n"
"    min-height: 60px;\n"
"    max-height: 60px;\n"
"   \n"
"}\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"   border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    padding: 10px;\n"
"    font: 10pt ;\n"
"	font: 9pt \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    margin: 2px;               /* Espaciado uniforme alrededor */\n"
"}\n"
"\n"
"/* Estado hover */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estado p"
                        "resionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.frm_bar_action.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bar_action.setFrameShadow(QFrame.Shadow.Sunken)
        self.hly_frm_bar_action = QHBoxLayout(self.frm_bar_action)
        self.hly_frm_bar_action.setSpacing(2)
        self.hly_frm_bar_action.setObjectName(u"hly_frm_bar_action")
        self.hly_frm_bar_action.setContentsMargins(4, 4, 4, 4)
        self.btn_add_action = QPushButton(self.frm_bar_action)
        self.btn_add_action.setObjectName(u"btn_add_action")
        self.btn_add_action.setMinimumSize(QSize(118, 48))
        self.btn_add_action.setMaximumSize(QSize(118, 48))
        self.btn_add_action.setFont(font4)
        self.btn_add_action.setStyleSheet(u"")
        self.btn_add_action.setIcon(icon37)
        self.btn_add_action.setIconSize(QSize(22, 22))

        self.hly_frm_bar_action.addWidget(self.btn_add_action)

        self.btn_save_action = QPushButton(self.frm_bar_action)
        self.btn_save_action.setObjectName(u"btn_save_action")
        self.btn_save_action.setMinimumSize(QSize(118, 48))
        self.btn_save_action.setMaximumSize(QSize(118, 48))
        self.btn_save_action.setFont(font4)
        self.btn_save_action.setStyleSheet(u"")
        self.btn_save_action.setIcon(icon38)
        self.btn_save_action.setIconSize(QSize(22, 22))

        self.hly_frm_bar_action.addWidget(self.btn_save_action)

        self.btn_edit_action = QPushButton(self.frm_bar_action)
        self.btn_edit_action.setObjectName(u"btn_edit_action")
        self.btn_edit_action.setMinimumSize(QSize(118, 48))
        self.btn_edit_action.setMaximumSize(QSize(118, 48))
        self.btn_edit_action.setFont(font4)
        self.btn_edit_action.setStyleSheet(u"")
        self.btn_edit_action.setIcon(icon39)
        self.btn_edit_action.setIconSize(QSize(22, 22))

        self.hly_frm_bar_action.addWidget(self.btn_edit_action)

        self.btn_cancel_action = QPushButton(self.frm_bar_action)
        self.btn_cancel_action.setObjectName(u"btn_cancel_action")
        self.btn_cancel_action.setMinimumSize(QSize(118, 48))
        self.btn_cancel_action.setMaximumSize(QSize(118, 48))
        self.btn_cancel_action.setFont(font4)
        self.btn_cancel_action.setStyleSheet(u"")
        self.btn_cancel_action.setIcon(icon40)
        self.btn_cancel_action.setIconSize(QSize(22, 22))

        self.hly_frm_bar_action.addWidget(self.btn_cancel_action)

        self.btn_delete_action = QPushButton(self.frm_bar_action)
        self.btn_delete_action.setObjectName(u"btn_delete_action")
        self.btn_delete_action.setMinimumSize(QSize(118, 48))
        self.btn_delete_action.setMaximumSize(QSize(118, 48))
        self.btn_delete_action.setStyleSheet(u"")
        self.btn_delete_action.setIcon(icon41)
        self.btn_delete_action.setIconSize(QSize(22, 22))

        self.hly_frm_bar_action.addWidget(self.btn_delete_action)


        self.vly_frm_form_action.addWidget(self.frm_bar_action)

        self.vly_frm_form_action.setStretch(0, 4)
        self.vly_frm_form_action.setStretch(1, 1)

        self.hly_frm__actions.addWidget(self.frm_form_action)

        self.qsw_forms.addWidget(self.page_frm_actions)
        self.page_frm_clients = QWidget()
        self.page_frm_clients.setObjectName(u"page_frm_clients")
        sizePolicy.setHeightForWidth(self.page_frm_clients.sizePolicy().hasHeightForWidth())
        self.page_frm_clients.setSizePolicy(sizePolicy)
        self.page_frm_clients.setMinimumSize(QSize(825, 544))
        self.page_frm_clients.setMaximumSize(QSize(1980, 1080))
        self.page_frm_clients.setStyleSheet(u"")
        self.hly_frm_clients = QHBoxLayout(self.page_frm_clients)
        self.hly_frm_clients.setSpacing(0)
        self.hly_frm_clients.setObjectName(u"hly_frm_clients")
        self.hly_frm_clients.setContentsMargins(0, 0, 0, 0)
        self.frm_form_clients = QFrame(self.page_frm_clients)
        self.frm_form_clients.setObjectName(u"frm_form_clients")
        sizePolicy.setHeightForWidth(self.frm_form_clients.sizePolicy().hasHeightForWidth())
        self.frm_form_clients.setSizePolicy(sizePolicy)
        self.frm_form_clients.setMinimumSize(QSize(625, 0))
        self.frm_form_clients.setMaximumSize(QSize(1920, 1080))
        self.frm_form_clients.setStyleSheet(u"")
        self.frm_form_clients.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_clients.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_clients = QVBoxLayout(self.frm_form_clients)
        self.vly_frm_form_clients.setSpacing(2)
        self.vly_frm_form_clients.setObjectName(u"vly_frm_form_clients")
        self.vly_frm_form_clients.setContentsMargins(4, 4, 4, 4)
        self.frm_clients = QFrame(self.frm_form_clients)
        self.frm_clients.setObjectName(u"frm_clients")
        sizePolicy.setHeightForWidth(self.frm_clients.sizePolicy().hasHeightForWidth())
        self.frm_clients.setSizePolicy(sizePolicy)
        self.frm_clients.setMinimumSize(QSize(625, 433))
        self.frm_clients.setMaximumSize(QSize(625, 433))
        self.frm_clients.setStyleSheet(u"/* Estilos para la seccion de formularios */\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del marco */\n"
"QGroupBox {\n"
"    background-color: rgb(188, 246, 255);\n"
"    border-radius: 10px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    color: #000000;                  /* Color del texto */\n"
"    font: bold 24pt \"Segoe UI\";     /* Fuente m\u00e1s grande y en negrita */\n"
"    subcontrol-origin: margin;      /* Posici\u00f3n del t\u00edtulo */\n"
"    subcontrol-position: top left;  /* Alineaci\u00f3n del t\u00edtulo */\n"
"    padding: 4px;                   /* Espacio alrededor del texto */\n"
"}\n"
"\n"
"/* Estilo de las etiquetas */\n"
"QLabel {\n"
"    color: #000000;                /* Color del texto */\n"
"    background-color: rgb(188, 246, 255); /* Opcional: fondo */\n"
"    font: 10pt \"Segoe UI\";        "
                        " /* Fuente de Etiquetas */\n"
"    line-height: 12px;\n"
"}\n"
"\n"
"/* Estilo de QTextEdit */\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 8pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 8pt \"Segoe UI\";                /* Fuente para QLineEdit */\n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Colo"
                        "r del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 8pt \"Segoe UI\";                /* Fuente para QComboBox */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 8pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* Estilo de QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redon"
                        "deadas */\n"
"    font: 8pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
"QComboBox:disabled, \n"
"QDateEdit:disabled, \n"
"QTimeEdit:disabled {\n"
"    background-color: #e1e1e1;\n"
"    color: #808080;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"\n"
"/* Forzamos el QTextEdit */\n"
"QTextEdit:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}\n"
"/* Forzamos el QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #e1e1e1 !important; \n"
"    color: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_clients.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_clients.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_clients = QVBoxLayout(self.frm_clients)
        self.vly_clients.setSpacing(3)
        self.vly_clients.setObjectName(u"vly_clients")
        self.vly_clients.setContentsMargins(4, 4, 4, 4)
        self.grb_frm_clients = QGroupBox(self.frm_clients)
        self.grb_frm_clients.setObjectName(u"grb_frm_clients")
        self.grb_frm_clients.setMinimumSize(QSize(0, 0))
        self.grb_frm_clients.setMaximumSize(QSize(16777215, 544))
        self.grb_frm_clients.setStyleSheet(u"")
        self.label_clt_codigo = QLabel(self.grb_frm_clients)
        self.label_clt_codigo.setObjectName(u"label_clt_codigo")
        self.label_clt_codigo.setGeometry(QRect(10, 30, 61, 20))
        self.label_clt_codigo.setMaximumSize(QSize(100, 20))
        self.label_clt_codigo.setAutoFillBackground(False)
        self.lineEdit_clt_codigo = QLineEdit(self.grb_frm_clients)
        self.lineEdit_clt_codigo.setObjectName(u"lineEdit_clt_codigo")
        self.lineEdit_clt_codigo.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_clt_codigo.setMaximumSize(QSize(100, 20))
        self.label_clt_descripcion = QLabel(self.grb_frm_clients)
        self.label_clt_descripcion.setObjectName(u"label_clt_descripcion")
        self.label_clt_descripcion.setGeometry(QRect(10, 60, 101, 20))
        self.label_clt_descripcion.setMaximumSize(QSize(150, 20))
        self.lineEdit_clt_descripcion = QLineEdit(self.grb_frm_clients)
        self.lineEdit_clt_descripcion.setObjectName(u"lineEdit_clt_descripcion")
        self.lineEdit_clt_descripcion.setGeometry(QRect(120, 60, 400, 20))
        self.lineEdit_clt_descripcion.setMinimumSize(QSize(400, 20))
        self.lineEdit_clt_descripcion.setMaximumSize(QSize(400, 20))
        self.lineEdit_clt_descripcion.setStyleSheet(u"")
        self.label_clt_idfiscaliscal = QLabel(self.grb_frm_clients)
        self.label_clt_idfiscaliscal.setObjectName(u"label_clt_idfiscaliscal")
        self.label_clt_idfiscaliscal.setGeometry(QRect(10, 90, 115, 20))
        self.label_clt_idfiscaliscal.setMinimumSize(QSize(115, 0))
        self.label_clt_idfiscaliscal.setMaximumSize(QSize(110, 20))
        self.label_clt_status = QLabel(self.grb_frm_clients)
        self.label_clt_status.setObjectName(u"label_clt_status")
        self.label_clt_status.setGeometry(QRect(238, 30, 61, 20))
        self.label_clt_status.setMaximumSize(QSize(100, 20))
        self.lineEdit_clt_idfiscaliscal = QLineEdit(self.grb_frm_clients)
        self.lineEdit_clt_idfiscaliscal.setObjectName(u"lineEdit_clt_idfiscaliscal")
        self.lineEdit_clt_idfiscaliscal.setGeometry(QRect(133, 90, 100, 20))
        self.lineEdit_clt_idfiscaliscal.setMaximumSize(QSize(100, 20))
        self.cmb_clt_status = QComboBox(self.grb_frm_clients)
        self.cmb_clt_status.addItem("")
        self.cmb_clt_status.addItem("")
        self.cmb_clt_status.setObjectName(u"cmb_clt_status")
        self.cmb_clt_status.setGeometry(QRect(308, 30, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_clt_status.sizePolicy().hasHeightForWidth())
        self.cmb_clt_status.setSizePolicy(sizePolicy)
        self.cmb_clt_status.setMinimumSize(QSize(80, 20))
        self.cmb_clt_status.setMaximumSize(QSize(80, 20))
        self.cmb_clt_status.setStyleSheet(u"")
        self.cmb_clt_tipocontribuyente = QComboBox(self.grb_frm_clients)
        self.cmb_clt_tipocontribuyente.addItem("")
        self.cmb_clt_tipocontribuyente.addItem("")
        self.cmb_clt_tipocontribuyente.setObjectName(u"cmb_clt_tipocontribuyente")
        self.cmb_clt_tipocontribuyente.setGeometry(QRect(475, 90, 100, 20))
        sizePolicy.setHeightForWidth(self.cmb_clt_tipocontribuyente.sizePolicy().hasHeightForWidth())
        self.cmb_clt_tipocontribuyente.setSizePolicy(sizePolicy)
        self.cmb_clt_tipocontribuyente.setMaximumSize(QSize(100, 20))
        self.cmb_clt_tipocontribuyente.setStyleSheet(u"")
        self.label_clt_tipocontribuyente = QLabel(self.grb_frm_clients)
        self.label_clt_tipocontribuyente.setObjectName(u"label_clt_tipocontribuyente")
        self.label_clt_tipocontribuyente.setGeometry(QRect(330, 90, 140, 20))
        self.label_clt_tipocontribuyente.setMinimumSize(QSize(140, 20))
        self.label_clt_tipocontribuyente.setMaximumSize(QSize(80, 20))
        self.label_clt_fechacreacion = QLabel(self.grb_frm_clients)
        self.label_clt_fechacreacion.setObjectName(u"label_clt_fechacreacion")
        self.label_clt_fechacreacion.setGeometry(QRect(421, 30, 40, 20))
        self.label_clt_fechacreacion.setMaximumSize(QSize(40, 20))
        self.dateEdit_clt_fechacreacion = QDateEdit(self.grb_frm_clients)
        self.dateEdit_clt_fechacreacion.setObjectName(u"dateEdit_clt_fechacreacion")
        self.dateEdit_clt_fechacreacion.setGeometry(QRect(470, 30, 100, 20))
        self.dateEdit_clt_fechacreacion.setMaximumSize(QSize(100, 20))
        self.dateEdit_clt_fechacreacion.setStyleSheet(u"")
        self.dateEdit_clt_fechacreacion.setCalendarPopup(True)

        self.vly_clients.addWidget(self.grb_frm_clients)

        self.grb_direccion_telefono_cliente = QGroupBox(self.frm_clients)
        self.grb_direccion_telefono_cliente.setObjectName(u"grb_direccion_telefono_cliente")
        self.grb_direccion_telefono_cliente.setMinimumSize(QSize(0, 0))
        self.grb_direccion_telefono_cliente.setStyleSheet(u"")
        self.textEdit_clt_direccionF = QTextEdit(self.grb_direccion_telefono_cliente)
        self.textEdit_clt_direccionF.setObjectName(u"textEdit_clt_direccionF")
        self.textEdit_clt_direccionF.setGeometry(QRect(87, 22, 200, 60))
        self.textEdit_clt_direccionF.setMinimumSize(QSize(200, 60))
        self.textEdit_clt_direccionF.setMaximumSize(QSize(200, 60))
        self.textEdit_clt_direccionF.setStyleSheet(u"")
        self.label_clt_direccionF = QLabel(self.grb_direccion_telefono_cliente)
        self.label_clt_direccionF.setObjectName(u"label_clt_direccionF")
        self.label_clt_direccionF.setGeometry(QRect(10, 22, 71, 41))
        self.label_clt_direccionF.setScaledContents(False)
        self.label_clt_direccionL = QLabel(self.grb_direccion_telefono_cliente)
        self.label_clt_direccionL.setObjectName(u"label_clt_direccionL")
        self.label_clt_direccionL.setGeometry(QRect(310, 22, 71, 41))
        self.textEdit_clt_direccionL = QTextEdit(self.grb_direccion_telefono_cliente)
        self.textEdit_clt_direccionL.setObjectName(u"textEdit_clt_direccionL")
        self.textEdit_clt_direccionL.setGeometry(QRect(386, 22, 200, 60))
        self.textEdit_clt_direccionL.setMinimumSize(QSize(200, 60))
        self.textEdit_clt_direccionL.setMaximumSize(QSize(200, 60))
        self.textEdit_clt_direccionL.setStyleSheet(u"")
        self.label_clt_telefono1 = QLabel(self.grb_direccion_telefono_cliente)
        self.label_clt_telefono1.setObjectName(u"label_clt_telefono1")
        self.label_clt_telefono1.setGeometry(QRect(10, 88, 101, 20))
        self.label_clt_telefono1.setMaximumSize(QSize(150, 20))
        self.label_clt_telefono2 = QLabel(self.grb_direccion_telefono_cliente)
        self.label_clt_telefono2.setObjectName(u"label_clt_telefono2")
        self.label_clt_telefono2.setGeometry(QRect(310, 88, 101, 20))
        self.label_clt_telefono2.setMaximumSize(QSize(150, 20))
        self.lineEdit_clt_telefono1 = QLineEdit(self.grb_direccion_telefono_cliente)
        self.lineEdit_clt_telefono1.setObjectName(u"lineEdit_clt_telefono1")
        self.lineEdit_clt_telefono1.setGeometry(QRect(119, 88, 165, 20))
        self.lineEdit_clt_telefono1.setMinimumSize(QSize(165, 0))
        self.lineEdit_clt_telefono1.setMaximumSize(QSize(165, 20))
        self.lineEdit_clt_telefono2 = QLineEdit(self.grb_direccion_telefono_cliente)
        self.lineEdit_clt_telefono2.setObjectName(u"lineEdit_clt_telefono2")
        self.lineEdit_clt_telefono2.setGeometry(QRect(419, 88, 165, 20))
        self.lineEdit_clt_telefono2.setMinimumSize(QSize(165, 0))
        self.lineEdit_clt_telefono2.setMaximumSize(QSize(165, 20))
        self.label_clt_rmailempresa = QLabel(self.grb_direccion_telefono_cliente)
        self.label_clt_rmailempresa.setObjectName(u"label_clt_rmailempresa")
        self.label_clt_rmailempresa.setGeometry(QRect(10, 115, 101, 20))
        self.label_clt_rmailempresa.setMaximumSize(QSize(150, 20))
        self.lineEdit_clt_emailempresa = QLineEdit(self.grb_direccion_telefono_cliente)
        self.lineEdit_clt_emailempresa.setObjectName(u"lineEdit_clt_emailempresa")
        self.lineEdit_clt_emailempresa.setGeometry(QRect(119, 115, 260, 20))
        self.lineEdit_clt_emailempresa.setMinimumSize(QSize(260, 0))
        self.lineEdit_clt_emailempresa.setMaximumSize(QSize(260, 20))

        self.vly_clients.addWidget(self.grb_direccion_telefono_cliente)

        self.grb_sontactos_cliente = QGroupBox(self.frm_clients)
        self.grb_sontactos_cliente.setObjectName(u"grb_sontactos_cliente")
        self.grb_sontactos_cliente.setMinimumSize(QSize(0, 0))
        self.grb_sontactos_cliente.setStyleSheet(u"")
        self.label_clt_representante = QLabel(self.grb_sontactos_cliente)
        self.label_clt_representante.setObjectName(u"label_clt_representante")
        self.label_clt_representante.setGeometry(QRect(10, 20, 150, 20))
        self.label_clt_representante.setMinimumSize(QSize(150, 20))
        self.label_clt_representante.setMaximumSize(QSize(150, 20))
        self.lineEdit_clt_representante = QLineEdit(self.grb_sontactos_cliente)
        self.lineEdit_clt_representante.setObjectName(u"lineEdit_clt_representante")
        self.lineEdit_clt_representante.setGeometry(QRect(162, 20, 260, 20))
        self.lineEdit_clt_representante.setMinimumSize(QSize(260, 0))
        self.lineEdit_clt_representante.setMaximumSize(QSize(260, 20))
        self.lineEdit_clt_representante.setStyleSheet(u"")
        self.label_clt_idrepresentante = QLabel(self.grb_sontactos_cliente)
        self.label_clt_idrepresentante.setObjectName(u"label_clt_idrepresentante")
        self.label_clt_idrepresentante.setGeometry(QRect(430, 20, 50, 20))
        self.label_clt_idrepresentante.setMinimumSize(QSize(50, 0))
        self.label_clt_idrepresentante.setMaximumSize(QSize(50, 20))
        self.lineEdit_clt_idrepresentante = QLineEdit(self.grb_sontactos_cliente)
        self.lineEdit_clt_idrepresentante.setObjectName(u"lineEdit_clt_idrepresentante")
        self.lineEdit_clt_idrepresentante.setGeometry(QRect(485, 20, 100, 20))
        self.lineEdit_clt_idrepresentante.setMaximumSize(QSize(100, 20))
        self.lineEdit_clt_telefonocontacto = QLineEdit(self.grb_sontactos_cliente)
        self.lineEdit_clt_telefonocontacto.setObjectName(u"lineEdit_clt_telefonocontacto")
        self.lineEdit_clt_telefonocontacto.setGeometry(QRect(162, 50, 165, 20))
        self.lineEdit_clt_telefonocontacto.setMinimumSize(QSize(165, 0))
        self.lineEdit_clt_telefonocontacto.setMaximumSize(QSize(165, 20))
        self.label_clt_telefonocontacto = QLabel(self.grb_sontactos_cliente)
        self.label_clt_telefonocontacto.setObjectName(u"label_clt_telefonocontacto")
        self.label_clt_telefonocontacto.setGeometry(QRect(10, 50, 150, 20))
        self.label_clt_telefonocontacto.setMinimumSize(QSize(150, 0))
        self.label_clt_telefonocontacto.setMaximumSize(QSize(150, 20))
        self.lineEdit_clt_emailcontacto = QLineEdit(self.grb_sontactos_cliente)
        self.lineEdit_clt_emailcontacto.setObjectName(u"lineEdit_clt_emailcontacto")
        self.lineEdit_clt_emailcontacto.setGeometry(QRect(162, 80, 260, 20))
        self.lineEdit_clt_emailcontacto.setMinimumSize(QSize(260, 0))
        self.lineEdit_clt_emailcontacto.setMaximumSize(QSize(260, 20))
        self.label_clt_emailcontacto = QLabel(self.grb_sontactos_cliente)
        self.label_clt_emailcontacto.setObjectName(u"label_clt_emailcontacto")
        self.label_clt_emailcontacto.setGeometry(QRect(10, 80, 101, 20))
        self.label_clt_emailcontacto.setMaximumSize(QSize(150, 20))
        self.label_clt_origen = QLabel(self.grb_sontactos_cliente)
        self.label_clt_origen.setObjectName(u"label_clt_origen")
        self.label_clt_origen.setGeometry(QRect(10, 110, 101, 20))
        self.label_clt_origen.setMaximumSize(QSize(150, 20))
        self.cmb_clt_origen = QComboBox(self.grb_sontactos_cliente)
        self.cmb_clt_origen.addItem("")
        self.cmb_clt_origen.addItem("")
        self.cmb_clt_origen.addItem("")
        self.cmb_clt_origen.addItem("")
        self.cmb_clt_origen.addItem("")
        self.cmb_clt_origen.setObjectName(u"cmb_clt_origen")
        self.cmb_clt_origen.setGeometry(QRect(160, 110, 260, 20))
        sizePolicy.setHeightForWidth(self.cmb_clt_origen.sizePolicy().hasHeightForWidth())
        self.cmb_clt_origen.setSizePolicy(sizePolicy)
        self.cmb_clt_origen.setMinimumSize(QSize(260, 20))
        self.cmb_clt_origen.setMaximumSize(QSize(260, 20))
        self.cmb_clt_origen.setStyleSheet(u"")

        self.vly_clients.addWidget(self.grb_sontactos_cliente)


        self.vly_frm_form_clients.addWidget(self.frm_clients)

        self.frm_bar_clients = QFrame(self.frm_form_clients)
        self.frm_bar_clients.setObjectName(u"frm_bar_clients")
        sizePolicy1.setHeightForWidth(self.frm_bar_clients.sizePolicy().hasHeightForWidth())
        self.frm_bar_clients.setSizePolicy(sizePolicy1)
        self.frm_bar_clients.setMinimumSize(QSize(629, 64))
        self.frm_bar_clients.setMaximumSize(QSize(629, 64))
        self.frm_bar_clients.setStyleSheet(u"/*Estilos para la barra de acciones*/\n"
"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(79, 179, 255);\n"
"    border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    min-width: 625px;\n"
"    max-width: 625px;\n"
"    min-height: 60px;\n"
"    max-height: 60px;\n"
"   \n"
"}\n"
"/* Botones */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"   border: 2px solid rgb(188, 246, 255);     /* borde */\n"
"    border-radius: 8px;        /* Esquinas redondeadas */\n"
"    padding: 10px;\n"
"    font: 10pt ;\n"
"	font: 9pt \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    margin: 2px;               /* Espaciado uniforme alrededor */\n"
"}\n"
"\n"
"/* Estado hover */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estado p"
                        "resionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.frm_bar_clients.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bar_clients.setFrameShadow(QFrame.Shadow.Sunken)
        self.hly_frm_bar_clients = QHBoxLayout(self.frm_bar_clients)
        self.hly_frm_bar_clients.setSpacing(2)
        self.hly_frm_bar_clients.setObjectName(u"hly_frm_bar_clients")
        self.hly_frm_bar_clients.setContentsMargins(4, 4, 4, 4)
        self.btn_add_clients = QPushButton(self.frm_bar_clients)
        self.btn_add_clients.setObjectName(u"btn_add_clients")
        sizePolicy1.setHeightForWidth(self.btn_add_clients.sizePolicy().hasHeightForWidth())
        self.btn_add_clients.setSizePolicy(sizePolicy1)
        self.btn_add_clients.setMinimumSize(QSize(118, 48))
        self.btn_add_clients.setMaximumSize(QSize(118, 48))
        self.btn_add_clients.setFont(font4)
        self.btn_add_clients.setStyleSheet(u"")
        self.btn_add_clients.setIcon(icon37)
        self.btn_add_clients.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients.addWidget(self.btn_add_clients)

        self.btn_save_clients = QPushButton(self.frm_bar_clients)
        self.btn_save_clients.setObjectName(u"btn_save_clients")
        self.btn_save_clients.setMinimumSize(QSize(118, 48))
        self.btn_save_clients.setMaximumSize(QSize(118, 48))
        self.btn_save_clients.setFont(font4)
        self.btn_save_clients.setStyleSheet(u"")
        self.btn_save_clients.setIcon(icon38)
        self.btn_save_clients.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients.addWidget(self.btn_save_clients)

        self.btn_edit_clients = QPushButton(self.frm_bar_clients)
        self.btn_edit_clients.setObjectName(u"btn_edit_clients")
        sizePolicy1.setHeightForWidth(self.btn_edit_clients.sizePolicy().hasHeightForWidth())
        self.btn_edit_clients.setSizePolicy(sizePolicy1)
        self.btn_edit_clients.setMinimumSize(QSize(118, 48))
        self.btn_edit_clients.setMaximumSize(QSize(118, 48))
        self.btn_edit_clients.setFont(font4)
        self.btn_edit_clients.setStyleSheet(u"")
        self.btn_edit_clients.setIcon(icon39)
        self.btn_edit_clients.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients.addWidget(self.btn_edit_clients)

        self.btn_cancel_clients = QPushButton(self.frm_bar_clients)
        self.btn_cancel_clients.setObjectName(u"btn_cancel_clients")
        self.btn_cancel_clients.setMinimumSize(QSize(118, 48))
        self.btn_cancel_clients.setMaximumSize(QSize(118, 48))
        self.btn_cancel_clients.setFont(font4)
        self.btn_cancel_clients.setStyleSheet(u"")
        self.btn_cancel_clients.setIcon(icon40)
        self.btn_cancel_clients.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients.addWidget(self.btn_cancel_clients)

        self.btn_delete_clients = QPushButton(self.frm_bar_clients)
        self.btn_delete_clients.setObjectName(u"btn_delete_clients")
        sizePolicy5.setHeightForWidth(self.btn_delete_clients.sizePolicy().hasHeightForWidth())
        self.btn_delete_clients.setSizePolicy(sizePolicy5)
        self.btn_delete_clients.setMinimumSize(QSize(118, 48))
        self.btn_delete_clients.setMaximumSize(QSize(118, 48))
        self.btn_delete_clients.setStyleSheet(u"")
        self.btn_delete_clients.setIcon(icon41)
        self.btn_delete_clients.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients.addWidget(self.btn_delete_clients)


        self.vly_frm_form_clients.addWidget(self.frm_bar_clients)


        self.hly_frm_clients.addWidget(self.frm_form_clients)

        self.qsw_forms.addWidget(self.page_frm_clients)

        self.hly_page_forms.addWidget(self.qsw_forms)

        self.sw_consolas.addWidget(self.page_forms)
        self.page_inf_red = QWidget()
        self.page_inf_red.setObjectName(u"page_inf_red")
        self.page_inf_red.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.vly_page_inf_red = QVBoxLayout(self.page_inf_red)
        self.vly_page_inf_red.setObjectName(u"vly_page_inf_red")
        self.textEdit_info_red = QTextEdit(self.page_inf_red)
        self.textEdit_info_red.setObjectName(u"textEdit_info_red")
        self.textEdit_info_red.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")

        self.vly_page_inf_red.addWidget(self.textEdit_info_red)

        self.label_info_red = QLabel(self.page_inf_red)
        self.label_info_red.setObjectName(u"label_info_red")
        self.label_info_red.setMinimumSize(QSize(40, 40))
        self.label_info_red.setMaximumSize(QSize(80, 80))
        self.label_info_red.setPixmap(QPixmap(u":/rec/assets/icons/Red01.png"))
        self.label_info_red.setScaledContents(True)
        self.label_info_red.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vly_page_inf_red.addWidget(self.label_info_red)

        self.sw_consolas.addWidget(self.page_inf_red)
        self.page_inf_so = QWidget()
        self.page_inf_so.setObjectName(u"page_inf_so")
        self.page_inf_so.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.vly_page_inf_so = QVBoxLayout(self.page_inf_so)
        self.vly_page_inf_so.setObjectName(u"vly_page_inf_so")
        self.textEdit_info_so = QTextEdit(self.page_inf_so)
        self.textEdit_info_so.setObjectName(u"textEdit_info_so")
        self.textEdit_info_so.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")

        self.vly_page_inf_so.addWidget(self.textEdit_info_so)

        self.label_info_so = QLabel(self.page_inf_so)
        self.label_info_so.setObjectName(u"label_info_so")
        self.label_info_so.setMinimumSize(QSize(40, 40))
        self.label_info_so.setMaximumSize(QSize(80, 80))
        self.label_info_so.setPixmap(QPixmap(u":/rec/assets/icons/OS02.svg"))
        self.label_info_so.setScaledContents(True)
        self.label_info_so.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vly_page_inf_so.addWidget(self.label_info_so)

        self.sw_consolas.addWidget(self.page_inf_so)
        self.page_inf_regional = QWidget()
        self.page_inf_regional.setObjectName(u"page_inf_regional")
        self.page_inf_regional.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.vly_page_inf_regional = QVBoxLayout(self.page_inf_regional)
        self.vly_page_inf_regional.setObjectName(u"vly_page_inf_regional")
        self.textEdit_info_regional = QTextEdit(self.page_inf_regional)
        self.textEdit_info_regional.setObjectName(u"textEdit_info_regional")
        self.textEdit_info_regional.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")

        self.vly_page_inf_regional.addWidget(self.textEdit_info_regional)

        self.label_info_regional = QLabel(self.page_inf_regional)
        self.label_info_regional.setObjectName(u"label_info_regional")
        self.label_info_regional.setMinimumSize(QSize(80, 80))
        self.label_info_regional.setMaximumSize(QSize(80, 80))
        self.label_info_regional.setPixmap(QPixmap(u":/rec/assets/icons/filesettings_102180.svg"))
        self.label_info_regional.setScaledContents(True)
        self.label_info_regional.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vly_page_inf_regional.addWidget(self.label_info_regional)

        self.sw_consolas.addWidget(self.page_inf_regional)

        self.vly_frame_consolas.addWidget(self.sw_consolas)


        self.horizontalLayout.addWidget(self.frame_consolas)


        self.verticalLayout_2.addWidget(self.frame_inferior)


        self.horizontalLayout_2.addWidget(self.frm_principal)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimizar, self.btn_restaurar)
        QWidget.setTabOrder(self.btn_restaurar, self.btn_maximizar)
        QWidget.setTabOrder(self.btn_maximizar, self.btn_cerrar)
        QWidget.setTabOrder(self.btn_cerrar, self.btn_info_hardware)
        QWidget.setTabOrder(self.btn_info_hardware, self.btn_info_red)
        QWidget.setTabOrder(self.btn_info_red, self.btn_info_so)
        QWidget.setTabOrder(self.btn_info_so, self.btn_info_regional)
        QWidget.setTabOrder(self.btn_info_regional, self.btn_limpiar)
        QWidget.setTabOrder(self.btn_limpiar, self.btn_menu)
        QWidget.setTabOrder(self.btn_menu, self.btn_operations)
        QWidget.setTabOrder(self.btn_operations, self.btn_config)
        QWidget.setTabOrder(self.btn_config, self.btn_info_sistema)
        QWidget.setTabOrder(self.btn_info_sistema, self.btn_info_mbd)
        QWidget.setTabOrder(self.btn_info_mbd, self.btn_info_cpu)
        QWidget.setTabOrder(self.btn_info_cpu, self.btn_info_gpu)
        QWidget.setTabOrder(self.btn_info_gpu, self.btn_info_ram)
        QWidget.setTabOrder(self.btn_info_ram, self.btn_info_hdd)
        QWidget.setTabOrder(self.btn_info_hdd, self.btn_info_nic)
        QWidget.setTabOrder(self.btn_info_nic, self.btn_info_audio)
        QWidget.setTabOrder(self.btn_info_audio, self.btn_info_com)
        QWidget.setTabOrder(self.btn_info_com, self.btn_info_usb)
        QWidget.setTabOrder(self.btn_info_usb, self.btn_info_bth)
        QWidget.setTabOrder(self.btn_info_bth, self.btn_regresar_menu)
        QWidget.setTabOrder(self.btn_regresar_menu, self.btn_ark_company)
        QWidget.setTabOrder(self.btn_ark_company, self.btn_ark_clients)
        QWidget.setTabOrder(self.btn_ark_clients, self.btn_ark_currencies)
        QWidget.setTabOrder(self.btn_ark_currencies, self.btn_ark_categories)
        QWidget.setTabOrder(self.btn_ark_categories, self.btn_ark_functional_units)
        QWidget.setTabOrder(self.btn_ark_functional_units, self.btn_ark_actions)
        QWidget.setTabOrder(self.btn_ark_actions, self.btn_ark_employees)
        QWidget.setTabOrder(self.btn_ark_employees, self.btn_ark_device_types)
        QWidget.setTabOrder(self.btn_ark_device_types, self.btn_ark_it_assets)
        QWidget.setTabOrder(self.btn_ark_it_assets, self.btn_ark_job_titles)
        QWidget.setTabOrder(self.btn_ark_job_titles, self.btn_ark_users)
        QWidget.setTabOrder(self.btn_ark_users, self.btn_menu_ppal)
        QWidget.setTabOrder(self.btn_menu_ppal, self.textEdit_info_hw)
        QWidget.setTabOrder(self.textEdit_info_hw, self.btn_cambio_regional)
        QWidget.setTabOrder(self.btn_cambio_regional, self.btn_config_sql_tools)
        QWidget.setTabOrder(self.btn_config_sql_tools, self.btn_config_tools)
        QWidget.setTabOrder(self.btn_config_tools, self.textEdit_info_config)
        QWidget.setTabOrder(self.textEdit_info_config, self.textEdit_info_red)
        QWidget.setTabOrder(self.textEdit_info_red, self.textEdit_info_so)
        QWidget.setTabOrder(self.textEdit_info_so, self.textEdit_info_regional)

        self.retranslateUi(MainWindow)

        self.sw_consolas.setCurrentIndex(3)


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
        self.btn_ark_currencies.setText(QCoreApplication.translate("MainWindow", u"      Monedas", None))
        self.btn_ark_categories.setText(QCoreApplication.translate("MainWindow", u"    Categor\u00edas", None))
        self.btn_ark_functional_units.setText(QCoreApplication.translate("MainWindow", u" Unidades", None))
        self.btn_ark_actions.setText(QCoreApplication.translate("MainWindow", u"      Acciones", None))
        self.btn_ark_employees.setText(QCoreApplication.translate("MainWindow", u"      Empleados", None))
        self.btn_ark_device_types.setText(QCoreApplication.translate("MainWindow", u"      Tipos", None))
        self.btn_ark_it_assets.setText(QCoreApplication.translate("MainWindow", u"    Recursos", None))
        self.btn_ark_job_titles.setText(QCoreApplication.translate("MainWindow", u"   Profesiones", None))
        self.btn_ark_requests.setText(QCoreApplication.translate("MainWindow", u"   Solicitudes", None))
        self.btn_ark_sessions.setText(QCoreApplication.translate("MainWindow", u"   Sesiones", None))
        self.btn_ark_users.setText(QCoreApplication.translate("MainWindow", u"    Usuarios", None))
        self.btn_menu_ppal.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa Principal", None))
        self.title_arktoolspc.setText("")
#if QT_CONFIG(accessibility)
        self.label_logo_tools.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
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
        self.grb_currencies.setTitle(QCoreApplication.translate("MainWindow", u"Monedas", None))
        self.cmb_mda_iso4217.setItemText(0, QCoreApplication.translate("MainWindow", u"VES", None))
        self.cmb_mda_iso4217.setItemText(1, QCoreApplication.translate("MainWindow", u"USD", None))
        self.cmb_mda_iso4217.setItemText(2, QCoreApplication.translate("MainWindow", u"EUR", None))

        self.label_mda_simbolo.setText(QCoreApplication.translate("MainWindow", u"Simbolo Moneda:", None))
        self.label_mda_descripcion.setText(QCoreApplication.translate("MainWindow", u"Denominaci\u00f3n:", None))
        self.label_mda_iso4217.setText(QCoreApplication.translate("MainWindow", u"ISO 4217:", None))
        self.label_mda_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
#if QT_CONFIG(accessibility)
        self.label_mda_codigo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_mda_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_mda_fechacreacion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.cmb_mda_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_mda_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.cmb_mda_simbolo.setItemText(0, QCoreApplication.translate("MainWindow", u"Bs.", None))
        self.cmb_mda_simbolo.setItemText(1, QCoreApplication.translate("MainWindow", u"$", None))
        self.cmb_mda_simbolo.setItemText(2, QCoreApplication.translate("MainWindow", u"\u20ac", None))

        self.grb_mda_gestion.setTitle(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Factor", None))
        self.label_mda_fechaactualizacion.setText(QCoreApplication.translate("MainWindow", u"Fecha Actualizaci\u00f3n:", None))
#if QT_CONFIG(accessibility)
        self.label_mda_factorpasivo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_mda_factorpasivo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Factor Pasivo:</p></body></html>", None))
#if QT_CONFIG(accessibility)
        self.label_mda_factoractivo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_mda_factoractivo.setText(QCoreApplication.translate("MainWindow", u"Factor Activo:", None))
        self.label_mda_fechaultima.setText(QCoreApplication.translate("MainWindow", u"Ultima Actualizaci\u00f3n:", None))
        self.btn_add_currencies.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_save_currencies.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.btn_save_currencies.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_edit_currencies.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_cancel_currencies.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel_currencies.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_currencies.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.grb_employees.setTitle(QCoreApplication.translate("MainWindow", u"Empleados", None))
#if QT_CONFIG(accessibility)
        self.label_emy_codigo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_emy_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_emy_descripcion.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n Social:", None))
        self.label_emy_idemployees.setText(QCoreApplication.translate("MainWindow", u"ID/C\u00e9dula:", None))
        self.label_emy_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_emy_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_emy_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.grb_direccion_telefonos_employees.setTitle(QCoreApplication.translate("MainWindow", u"Tel\u00e9fonos y Correo", None))
        self.label_emy_telefono1.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.label_emy_rol.setText(QCoreApplication.translate("MainWindow", u"Rol:", None))
        self.label_emy_emailusuario.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.grb_sontactos__employees.setTitle(QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.label_emy_cliente.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_emy_password.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_emy_cargo.setText(QCoreApplication.translate("MainWindow", u"Cargo:", None))
        self.label_emy_fechacreacion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.btn_add_employees.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_save_employees.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.btn_save_employees.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_edit_employees.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_cancel_employees.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel_employees.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_employees.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.grb_device_types.setTitle(QCoreApplication.translate("MainWindow", u"Tipos de Dispositivos", None))
#if QT_CONFIG(accessibility)
        self.label_dty_vodigo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_dty_vodigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_dty_descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_dty_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_dty_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_dty_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_dty_fechacreacion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_dty_DescripcionTec.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n\n"
"Detallada:", None))
        self.btn_add_device_types.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_save_device_types.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.btn_save_device_types.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_edit_device_types.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_cancel_device_types.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel_device_types.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_device_types.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.grb_actions_categories.setTitle(QCoreApplication.translate("MainWindow", u"Categorias", None))
#if QT_CONFIG(accessibility)
        self.label_cat_codigo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_cat_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_cat_descripcion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Descripci\u00f3n:</p></body></html>", None))
        self.label_cat_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_cat_ststus.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_cat_ststus.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_cat_fechacreacion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_cat_descripciontec.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n\n"
"Detallada:", None))
        self.btn_add_actions_categories.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
#if QT_CONFIG(shortcut)
        self.btn_add_actions_categories.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.btn_save_actions_categories.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.btn_save_actions_categories.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_edit_actions_categories.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
#if QT_CONFIG(shortcut)
        self.btn_edit_actions_categories.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_cancel_actions_categories.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel_actions_categories.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_actions_categories.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
#if QT_CONFIG(shortcut)
        self.btn_delete_actions_categories.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.grb_it_assets.setTitle(QCoreApplication.translate("MainWindow", u"Recursos", None))
#if QT_CONFIG(accessibility)
        self.label_ita_codigo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_ita_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_ita_descripcion.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n Social:", None))
        self.label_ita_marca.setText(QCoreApplication.translate("MainWindow", u"Marca:", None))
        self.label_ita_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_ita_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_ita_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.cmb_ita_Clasificacion.setItemText(0, QCoreApplication.translate("MainWindow", u"Equipos de C\u00f3mputo Personal", None))
        self.cmb_ita_Clasificacion.setItemText(1, QCoreApplication.translate("MainWindow", u"Equipos de Servidor y Centro de Datos", None))
        self.cmb_ita_Clasificacion.setItemText(2, QCoreApplication.translate("MainWindow", u"Equipos Perif\u00e9ricos", None))
        self.cmb_ita_Clasificacion.setItemText(3, QCoreApplication.translate("MainWindow", u"Equipos de Red y Telecomunicaciones", None))
        self.cmb_ita_Clasificacion.setItemText(4, QCoreApplication.translate("MainWindow", u"Equipos M\u00f3viles", None))
        self.cmb_ita_Clasificacion.setItemText(5, QCoreApplication.translate("MainWindow", u"Equipos Audiovisuales", None))
        self.cmb_ita_Clasificacion.setItemText(6, QCoreApplication.translate("MainWindow", u"Equipos Especializados", None))

        self.label_ita_clasificacion.setText(QCoreApplication.translate("MainWindow", u"Clasificaci\u00f3n:", None))
        self.label_ita_fechavreacion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_ita_descripciontec.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n\n"
"T\u00e9cnica:", None))
        self.label_ita_rol.setText(QCoreApplication.translate("MainWindow", u"Rol:", None))
        self.label_ita_functional_units.setText(QCoreApplication.translate("MainWindow", u"Unidad Funcional:", None))
        self.label_ita_macadrees.setText(QCoreApplication.translate("MainWindow", u"MAC Adrees:", None))
        self.label_ita_ipadrees.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n IP:", None))
        self.label_ita_idRDP1.setText(QCoreApplication.translate("MainWindow", u"ID RDP 1:", None))
        self.label_ita_idRDP2.setText(QCoreApplication.translate("MainWindow", u"ID RDP 2:", None))
        self.label_ita_idemployees.setText(QCoreApplication.translate("MainWindow", u"Empleado Usuario:", None))
        self.label_ita_iprdp.setText(QCoreApplication.translate("MainWindow", u"IP RDP:", None))
        self.label_ita_NotasTech.setText(QCoreApplication.translate("MainWindow", u"Notas\n"
"T\u00e9cnicas:", None))
        self.btn_add_it_assets.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_save_it_assets.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.btn_save_it_assets.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_edit_it_assets.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_cancel_it_assets.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel_it_assets.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_it_assets.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.grb_users.setTitle(QCoreApplication.translate("MainWindow", u"Usuarios", None))
#if QT_CONFIG(accessibility)
        self.label_usr_codigo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_usr_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_usr_descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_usr_telefono.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.label_usr_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_usr_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_usr_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_usr_cargo.setText(QCoreApplication.translate("MainWindow", u"Cargo:", None))
        self.label_usr_fechacreacion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_usr_rol.setText(QCoreApplication.translate("MainWindow", u"Rol:", None))
        self.label_usr_emailusuario.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_usr_password_in.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_usr_password_rin.setText(QCoreApplication.translate("MainWindow", u"Re - Password:", None))
        self.btn_add_users.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_save_users.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.btn_save_users.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_edit_users.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_cancel_users.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel_users.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_users.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.grb_sessions.setTitle(QCoreApplication.translate("MainWindow", u"Sesiones", None))
#if QT_CONFIG(accessibility)
        self.label_ses_numero.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_ses_numero.setText(QCoreApplication.translate("MainWindow", u"N\u00famero:", None))
        self.label_ses_clt_descripcion.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n Social:", None))
        self.label_ses_clt_idfiscal.setText(QCoreApplication.translate("MainWindow", u"ID Fiscal (RIF):", None))
        self.label_ses_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_ses_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_ses_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_ses_fechaemision.setText(QCoreApplication.translate("MainWindow", u"Fecha de Emisi\u00f3n:", None))
        self.label_ses_direccionf.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n \n"
"Fiscal", None))
        self.label_ses_clt_telefono1.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.label_ses_clt_telefono2.setText(QCoreApplication.translate("MainWindow", u"M\u00f3vil:", None))
        self.grb_ark_sessions_details.setTitle(QCoreApplication.translate("MainWindow", u"Detalles de la sesi\u00f3n", None))
        self.label__ses_horafinal.setText(QCoreApplication.translate("MainWindow", u"Fin:", None))
        self.label__ses_horainicial.setText(QCoreApplication.translate("MainWindow", u"Hora Inicio:", None))
        self.label_ses_fechasesion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Sesi\u00f3n:", None))
        self.label_dts_description.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n \n"
"Actividad", None))
        self.label_dts_time_spent.setText(QCoreApplication.translate("MainWindow", u"Tiempo Empleado:", None))
        self.label_dts_result.setText(QCoreApplication.translate("MainWindow", u"Resultado:", None))
        self.btn_add_sessions.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_save_sessions.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.btn_save_sessions.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_edit_sessions.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_cancel_sessions.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel_sessions.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_sessions.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.grb_requests.setTitle(QCoreApplication.translate("MainWindow", u"Requerimientos", None))
#if QT_CONFIG(accessibility)
        self.label_req_codigo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_req_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_req_descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_req_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_req_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_req_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_req_fechacreacion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_req_descripciontec.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n\n"
"Detallada:", None))
#if QT_CONFIG(accessibility)
        self.label_req_codigocliente.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_req_codigocliente.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.btn_add_requests.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_save_requests.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.btn_save_requests.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_edit_requests.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_cancel_requests.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel_requests.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_requests.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.grb_job_titles.setTitle(QCoreApplication.translate("MainWindow", u"Profesiones", None))
#if QT_CONFIG(accessibility)
        self.label_job_codigo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_job_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_job_descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_job_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_job_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_job_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_job_fechacreacion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_job_descripciontec.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n\n"
"Detallada:", None))
        self.btn_add_job_titles.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_save_job_titles.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.btn_save_job_titles.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_edit_job_titles.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_cancel_job_titles.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel_job_titles.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_job_titles.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.grb_functional_units.setTitle(QCoreApplication.translate("MainWindow", u"Unidades Funcionales", None))
#if QT_CONFIG(accessibility)
        self.label_fun_codigo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_fun_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_fun_descripcion.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n Social:", None))
        self.label_fun_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_fun_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_fun_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_fun_fechacreacion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_fun_DescripcionTec.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n\n"
"Detallada:", None))
        self.btn_add_functional_units.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_save_functional_units.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.btn_save_functional_units.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_edit_functional_units.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_cancel_functional_units.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel_functional_units.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_functional_units.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.grb_datos_generales.setTitle(QCoreApplication.translate("MainWindow", u"Datos Generales", None))
#if QT_CONFIG(accessibility)
        self.label_emp_codigo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_emp_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_emp_descripcion.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n Social:", None))
        self.label_emp_idfiscal.setText(QCoreApplication.translate("MainWindow", u"ID Fiscal (RIF):", None))
        self.label_emp_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_emp_ststus.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_emp_ststus.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.cmb_emp_tipo_contribuyente.setItemText(0, QCoreApplication.translate("MainWindow", u"Ordibario", None))
        self.cmb_emp_tipo_contribuyente.setItemText(1, QCoreApplication.translate("MainWindow", u"Especial", None))

        self.label_emp_tipo_contribuyente.setText(QCoreApplication.translate("MainWindow", u"Tipo Contribuyente:", None))
        self.grb_direccion_telefonos.setTitle(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n y Tel\u00e9fonos", None))
        self.label_emp_DireccionF.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n \n"
"Fiscal", None))
        self.label_emp_Direccionl.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n \n"
"Fiscal", None))
        self.label_emp_telefono1.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono Ppal:", None))
        self.label_emp_telefono2.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono M\u00f3vil:", None))
        self.label_emp_EmailEmpresa.setText(QCoreApplication.translate("MainWindow", u"Email Empresa:", None))
        self.grb_sontactos.setTitle(QCoreApplication.translate("MainWindow", u"Contactos", None))
        self.label_emp_representante.setText(QCoreApplication.translate("MainWindow", u"Representante legal:", None))
        self.label_emp_idrepresentante.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C\u00e9dula:</p></body></html>", None))
        self.label_emp_TelefonoContacto.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono Contacto:", None))
        self.label_emp_EmailContacto.setText(QCoreApplication.translate("MainWindow", u"Email Contacto:", None))
        self.label_emp_creation_company.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.btn_add_a_company.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_save_a_company.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.btn_save_a_company.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_edit_a_company.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_cancel_a_company.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel_a_company.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_a_company.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.grb_frm_actions.setTitle(QCoreApplication.translate("MainWindow", u"Acciones", None))
#if QT_CONFIG(accessibility)
        self.label_act_codigo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_act_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_act_descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_id_category.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Categor\u00eda:</p></body></html>", None))
        self.label_act_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_act_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_act_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_act_fechacreacion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_act_descripciontec.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n\n"
"Detallada:", None))
        self.btn_add_action.setText(QCoreApplication.translate("MainWindow", u"  Incluir", None))
        self.btn_save_action.setText(QCoreApplication.translate("MainWindow", u" Guardar", None))
#if QT_CONFIG(shortcut)
        self.btn_save_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_edit_action.setText(QCoreApplication.translate("MainWindow", u"  Editar", None))
        self.btn_cancel_action.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_action.setText(QCoreApplication.translate("MainWindow", u" Borrar", None))
        self.grb_frm_clients.setTitle(QCoreApplication.translate("MainWindow", u"Cliente", None))
#if QT_CONFIG(accessibility)
        self.label_clt_codigo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_clt_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_clt_descripcion.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n Social:", None))
        self.label_clt_idfiscaliscal.setText(QCoreApplication.translate("MainWindow", u"ID Fiscal (RIF):", None))
        self.label_clt_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_clt_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_clt_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.cmb_clt_tipocontribuyente.setItemText(0, QCoreApplication.translate("MainWindow", u"Ordibario", None))
        self.cmb_clt_tipocontribuyente.setItemText(1, QCoreApplication.translate("MainWindow", u"Especial", None))

        self.label_clt_tipocontribuyente.setText(QCoreApplication.translate("MainWindow", u"Tipo Contribuyente:", None))
        self.label_clt_fechacreacion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.grb_direccion_telefono_cliente.setTitle(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n y Tel\u00e9fonos", None))
        self.label_clt_direccionF.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n\n"
"Fiscal:", None))
        self.label_clt_direccionL.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n\n"
"Antenci\u00f3n:", None))
        self.label_clt_telefono1.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono Ppal:", None))
        self.label_clt_telefono2.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono M\u00f3vil:", None))
        self.label_clt_rmailempresa.setText(QCoreApplication.translate("MainWindow", u"Email Empresa:", None))
        self.grb_sontactos_cliente.setTitle(QCoreApplication.translate("MainWindow", u"Contactos", None))
        self.label_clt_representante.setText(QCoreApplication.translate("MainWindow", u"Representante legal:", None))
        self.label_clt_idrepresentante.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C\u00e9dula:</p></body></html>", None))
        self.label_clt_telefonocontacto.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono Contacto:", None))
        self.label_clt_emailcontacto.setText(QCoreApplication.translate("MainWindow", u"Email Contacto:", None))
        self.label_clt_origen.setText(QCoreApplication.translate("MainWindow", u"Origen:", None))
        self.cmb_clt_origen.setItemText(0, QCoreApplication.translate("MainWindow", u"Hybrid", None))
        self.cmb_clt_origen.setItemText(1, QCoreApplication.translate("MainWindow", u"a2Softway", None))
        self.cmb_clt_origen.setItemText(2, QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Redes", None))
        self.cmb_clt_origen.setItemText(3, QCoreApplication.translate("MainWindow", u"Soporte Genberal", None))
        self.cmb_clt_origen.setItemText(4, "")

        self.btn_add_clients.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_save_clients.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.btn_save_clients.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_edit_clients.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_cancel_clients.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel_clients.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_clients.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.label_info_red.setText("")
        self.label_info_so.setText("")
        self.label_info_regional.setText("")
    # retranslateUi

