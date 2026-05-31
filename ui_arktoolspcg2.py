# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arktoolspcg2xuBqJj.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDoubleSpinBox, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,
    QTimeEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindow.resize(921, 613)
        MainWindow.setMinimumSize(QSize(0, 544))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(825, 544))
        self.centralwidget.setMaximumSize(QSize(1980, 1080))
        self.frm_principal = QFrame(self.centralwidget)
        self.frm_principal.setObjectName(u"frm_principal")
        self.frm_principal.setGeometry(QRect(9, 9, 837, 621))
        self.frm_principal.setMaximumSize(QSize(1980, 1080))
        self.frm_principal.setStyleSheet(u"")
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
        icon.addFile(u":/icons/assets/icons/fi-sr-rectangle-list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon1.addFile(u":/icons/assets/icons/fi-sr-arrow-down-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon2.addFile(u":/icons/assets/icons/fi-sr-expand.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon3.addFile(u":/icons/assets/icons/fi-sr-expand-arrows-alt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon4.addFile(u":/icons/assets/icons/fi-sr-cross-small.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.frame_menu_reports = QFrame(self.frame_inferior)
        self.frame_menu_reports.setObjectName(u"frame_menu_reports")
        self.frame_menu_reports.setMinimumSize(QSize(0, 0))
        self.frame_menu_reports.setMaximumSize(QSize(0, 16777215))
        self.frame_menu_reports.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}")
        self.frame_menu_reports.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu_reports.setFrameShadow(QFrame.Shadow.Sunken)
        self.vly_frame_operations_3 = QVBoxLayout(self.frame_menu_reports)
        self.vly_frame_operations_3.setSpacing(4)
        self.vly_frame_operations_3.setObjectName(u"vly_frame_operations_3")
        self.vly_frame_operations_3.setContentsMargins(0, 0, 0, 0)
        self.btn_ark_reports03 = QPushButton(self.frame_menu_reports)
        self.btn_ark_reports03.setObjectName(u"btn_ark_reports03")
        self.btn_ark_reports03.setMinimumSize(QSize(0, 28))
        self.btn_ark_reports03.setMaximumSize(QSize(180, 28))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setBold(True)
        font1.setKerning(False)
        self.btn_ark_reports03.setFont(font1)
        self.btn_ark_reports03.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/icons/002-Informes-General", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_reports03.setIcon(icon5)
        self.btn_ark_reports03.setIconSize(QSize(18, 18))

        self.vly_frame_operations_3.addWidget(self.btn_ark_reports03)

        self.btn_ark_reports02 = QPushButton(self.frame_menu_reports)
        self.btn_ark_reports02.setObjectName(u"btn_ark_reports02")
        self.btn_ark_reports02.setMinimumSize(QSize(0, 32))
        self.btn_ark_reports02.setMaximumSize(QSize(180, 28))
        self.btn_ark_reports02.setFont(font1)
        self.btn_ark_reports02.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_ark_reports02.setIcon(icon5)
        self.btn_ark_reports02.setIconSize(QSize(18, 18))

        self.vly_frame_operations_3.addWidget(self.btn_ark_reports02)

        self.btn_ark_reports06 = QPushButton(self.frame_menu_reports)
        self.btn_ark_reports06.setObjectName(u"btn_ark_reports06")
        self.btn_ark_reports06.setMinimumSize(QSize(0, 32))
        self.btn_ark_reports06.setMaximumSize(QSize(180, 28))
        self.btn_ark_reports06.setFont(font1)
        self.btn_ark_reports06.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_ark_reports06.setIcon(icon5)
        self.btn_ark_reports06.setIconSize(QSize(18, 18))

        self.vly_frame_operations_3.addWidget(self.btn_ark_reports06)

        self.btn_ark_reports01 = QPushButton(self.frame_menu_reports)
        self.btn_ark_reports01.setObjectName(u"btn_ark_reports01")
        self.btn_ark_reports01.setMinimumSize(QSize(0, 32))
        self.btn_ark_reports01.setMaximumSize(QSize(180, 28))
        self.btn_ark_reports01.setFont(font1)
        self.btn_ark_reports01.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_ark_reports01.setIcon(icon5)
        self.btn_ark_reports01.setIconSize(QSize(18, 18))

        self.vly_frame_operations_3.addWidget(self.btn_ark_reports01)

        self.btn_ark_reports07 = QPushButton(self.frame_menu_reports)
        self.btn_ark_reports07.setObjectName(u"btn_ark_reports07")
        self.btn_ark_reports07.setMinimumSize(QSize(0, 32))
        self.btn_ark_reports07.setMaximumSize(QSize(180, 28))
        self.btn_ark_reports07.setFont(font1)
        self.btn_ark_reports07.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_ark_reports07.setIcon(icon5)
        self.btn_ark_reports07.setIconSize(QSize(18, 18))

        self.vly_frame_operations_3.addWidget(self.btn_ark_reports07)

        self.btn_ark_reports08 = QPushButton(self.frame_menu_reports)
        self.btn_ark_reports08.setObjectName(u"btn_ark_reports08")
        self.btn_ark_reports08.setMinimumSize(QSize(0, 32))
        self.btn_ark_reports08.setMaximumSize(QSize(180, 28))
        self.btn_ark_reports08.setFont(font1)
        self.btn_ark_reports08.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_ark_reports08.setIcon(icon5)
        self.btn_ark_reports08.setIconSize(QSize(18, 18))

        self.vly_frame_operations_3.addWidget(self.btn_ark_reports08)

        self.btn_ark_reports05 = QPushButton(self.frame_menu_reports)
        self.btn_ark_reports05.setObjectName(u"btn_ark_reports05")
        self.btn_ark_reports05.setMinimumSize(QSize(0, 32))
        self.btn_ark_reports05.setMaximumSize(QSize(180, 28))
        self.btn_ark_reports05.setFont(font1)
        self.btn_ark_reports05.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_ark_reports05.setIcon(icon5)
        self.btn_ark_reports05.setIconSize(QSize(18, 18))

        self.vly_frame_operations_3.addWidget(self.btn_ark_reports05)

        self.btn_ark_reports04 = QPushButton(self.frame_menu_reports)
        self.btn_ark_reports04.setObjectName(u"btn_ark_reports04")
        self.btn_ark_reports04.setMinimumSize(QSize(0, 32))
        self.btn_ark_reports04.setMaximumSize(QSize(180, 28))
        self.btn_ark_reports04.setFont(font1)
        self.btn_ark_reports04.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_ark_reports04.setIcon(icon5)
        self.btn_ark_reports04.setIconSize(QSize(18, 18))

        self.vly_frame_operations_3.addWidget(self.btn_ark_reports04)

        self.btn_ark_reports09 = QPushButton(self.frame_menu_reports)
        self.btn_ark_reports09.setObjectName(u"btn_ark_reports09")
        self.btn_ark_reports09.setMinimumSize(QSize(0, 32))
        self.btn_ark_reports09.setMaximumSize(QSize(180, 28))
        self.btn_ark_reports09.setFont(font1)
        self.btn_ark_reports09.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_ark_reports09.setIcon(icon5)
        self.btn_ark_reports09.setIconSize(QSize(18, 18))

        self.vly_frame_operations_3.addWidget(self.btn_ark_reports09)

        self.btn_ark_reports10 = QPushButton(self.frame_menu_reports)
        self.btn_ark_reports10.setObjectName(u"btn_ark_reports10")
        self.btn_ark_reports10.setMinimumSize(QSize(0, 32))
        self.btn_ark_reports10.setMaximumSize(QSize(180, 28))
        self.btn_ark_reports10.setFont(font1)
        self.btn_ark_reports10.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_ark_reports10.setIcon(icon5)
        self.btn_ark_reports10.setIconSize(QSize(18, 18))

        self.vly_frame_operations_3.addWidget(self.btn_ark_reports10)

        self.btn_ark_reports11 = QPushButton(self.frame_menu_reports)
        self.btn_ark_reports11.setObjectName(u"btn_ark_reports11")
        self.btn_ark_reports11.setMinimumSize(QSize(0, 32))
        self.btn_ark_reports11.setMaximumSize(QSize(180, 28))
        self.btn_ark_reports11.setFont(font1)
        self.btn_ark_reports11.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_ark_reports11.setIcon(icon5)
        self.btn_ark_reports11.setIconSize(QSize(18, 18))

        self.vly_frame_operations_3.addWidget(self.btn_ark_reports11)

        self.btn_menu_repo_ppal = QPushButton(self.frame_menu_reports)
        self.btn_menu_repo_ppal.setObjectName(u"btn_menu_repo_ppal")
        self.btn_menu_repo_ppal.setMinimumSize(QSize(0, 32))
        self.btn_menu_repo_ppal.setMaximumSize(QSize(180, 28))
        self.btn_menu_repo_ppal.setFont(font1)
        self.btn_menu_repo_ppal.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/icons/fi-sr-angle-double-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu_repo_ppal.setIcon(icon6)
        self.btn_menu_repo_ppal.setIconSize(QSize(18, 18))

        self.vly_frame_operations_3.addWidget(self.btn_menu_repo_ppal)


        self.horizontalLayout.addWidget(self.frame_menu_reports)

        self.frame_menu_archives = QFrame(self.frame_inferior)
        self.frame_menu_archives.setObjectName(u"frame_menu_archives")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu_archives.sizePolicy().hasHeightForWidth())
        self.frame_menu_archives.setSizePolicy(sizePolicy)
        self.frame_menu_archives.setMinimumSize(QSize(0, 0))
        self.frame_menu_archives.setMaximumSize(QSize(0, 16777215))
        self.frame_menu_archives.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}")
        self.frame_menu_archives.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu_archives.setFrameShadow(QFrame.Shadow.Sunken)
        self.vly_frame_operations_2 = QVBoxLayout(self.frame_menu_archives)
        self.vly_frame_operations_2.setObjectName(u"vly_frame_operations_2")
        self.btn_ark_company = QPushButton(self.frame_menu_archives)
        self.btn_ark_company.setObjectName(u"btn_ark_company")
        self.btn_ark_company.setMinimumSize(QSize(0, 32))
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
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/icons/fi-sr-home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_company.setIcon(icon7)
        self.btn_ark_company.setIconSize(QSize(18, 18))

        self.vly_frame_operations_2.addWidget(self.btn_ark_company)

        self.btn_ark_clients = QPushButton(self.frame_menu_archives)
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
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/icons/fi-sr-person-shelter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_clients.setIcon(icon8)
        self.btn_ark_clients.setIconSize(QSize(18, 18))

        self.vly_frame_operations_2.addWidget(self.btn_ark_clients)

        self.btn_ark_currencies = QPushButton(self.frame_menu_archives)
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
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/icons/fi-sr-currency.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_currencies.setIcon(icon9)
        self.btn_ark_currencies.setIconSize(QSize(18, 18))

        self.vly_frame_operations_2.addWidget(self.btn_ark_currencies)

        self.btn_ark_categories = QPushButton(self.frame_menu_archives)
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
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/icons/fi-sr-category-alt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_categories.setIcon(icon10)
        self.btn_ark_categories.setIconSize(QSize(18, 18))

        self.vly_frame_operations_2.addWidget(self.btn_ark_categories)

        self.btn_ark_functional_units = QPushButton(self.frame_menu_archives)
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
        icon11 = QIcon()
        icon11.addFile(u":/icons/assets/icons/fi-sr-department-structure.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_functional_units.setIcon(icon11)
        self.btn_ark_functional_units.setIconSize(QSize(18, 18))

        self.vly_frame_operations_2.addWidget(self.btn_ark_functional_units)

        self.btn_ark_actions = QPushButton(self.frame_menu_archives)
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
        icon12 = QIcon()
        icon12.addFile(u":/icons/assets/icons/fi-sr-tasks.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_actions.setIcon(icon12)
        self.btn_ark_actions.setIconSize(QSize(18, 18))

        self.vly_frame_operations_2.addWidget(self.btn_ark_actions)

        self.btn_ark_employees = QPushButton(self.frame_menu_archives)
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
        icon13 = QIcon()
        icon13.addFile(u":/icons/assets/icons/fi-sr-employee-man-alt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_employees.setIcon(icon13)
        self.btn_ark_employees.setIconSize(QSize(18, 18))

        self.vly_frame_operations_2.addWidget(self.btn_ark_employees)

        self.btn_ark_device_types = QPushButton(self.frame_menu_archives)
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
        icon14 = QIcon()
        icon14.addFile(u":/icons/assets/icons/fi-sr-list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_device_types.setIcon(icon14)
        self.btn_ark_device_types.setIconSize(QSize(18, 18))

        self.vly_frame_operations_2.addWidget(self.btn_ark_device_types)

        self.btn_ark_it_assets = QPushButton(self.frame_menu_archives)
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
        icon15 = QIcon()
        icon15.addFile(u":/icons/assets/icons/fi-sr-resources.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_it_assets.setIcon(icon15)
        self.btn_ark_it_assets.setIconSize(QSize(18, 18))

        self.vly_frame_operations_2.addWidget(self.btn_ark_it_assets)

        self.btn_ark_job_titles = QPushButton(self.frame_menu_archives)
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
        icon16 = QIcon()
        icon16.addFile(u":/icons/assets/icons/fi-sr-person-chalkboard.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_job_titles.setIcon(icon16)
        self.btn_ark_job_titles.setIconSize(QSize(18, 18))

        self.vly_frame_operations_2.addWidget(self.btn_ark_job_titles)

        self.btn_ark_users = QPushButton(self.frame_menu_archives)
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
        icon17 = QIcon()
        icon17.addFile(u":/icons/assets/icons/fi-sr-person-simple.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_users.setIcon(icon17)
        self.btn_ark_users.setIconSize(QSize(18, 18))

        self.vly_frame_operations_2.addWidget(self.btn_ark_users)

        self.btn_menu_arch_ppal = QPushButton(self.frame_menu_archives)
        self.btn_menu_arch_ppal.setObjectName(u"btn_menu_arch_ppal")
        self.btn_menu_arch_ppal.setMinimumSize(QSize(0, 32))
        self.btn_menu_arch_ppal.setFont(font1)
        self.btn_menu_arch_ppal.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon18 = QIcon()
        icon18.addFile(u":/icons/assets/icons/fi-sr-angle-double-small-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu_arch_ppal.setIcon(icon18)
        self.btn_menu_arch_ppal.setIconSize(QSize(18, 18))

        self.vly_frame_operations_2.addWidget(self.btn_menu_arch_ppal)


        self.horizontalLayout.addWidget(self.frame_menu_archives)

        self.frame_menu_main = QFrame(self.frame_inferior)
        self.frame_menu_main.setObjectName(u"frame_menu_main")
        self.frame_menu_main.setEnabled(True)
        self.frame_menu_main.setMinimumSize(QSize(0, 0))
        self.frame_menu_main.setMaximumSize(QSize(0, 16777215))
        self.frame_menu_main.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}")
        self.frame_menu_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu_main.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_menu_main)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_archives_menu = QPushButton(self.frame_menu_main)
        self.btn_archives_menu.setObjectName(u"btn_archives_menu")
        self.btn_archives_menu.setMinimumSize(QSize(0, 0))
        self.btn_archives_menu.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon19.addFile(u":/icons/assets/icons/fi-sr-home-robot.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_archives_menu.setIcon(icon19)
        self.btn_archives_menu.setIconSize(QSize(35, 35))

        self.verticalLayout_6.addWidget(self.btn_archives_menu)

        self.btn_systems_menu = QPushButton(self.frame_menu_main)
        self.btn_systems_menu.setObjectName(u"btn_systems_menu")
        self.btn_systems_menu.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon20 = QIcon()
        icon20.addFile(u":/icons/assets/icons/fi-sr-house-chimney-window.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_systems_menu.setIcon(icon20)
        self.btn_systems_menu.setIconSize(QSize(35, 35))

        self.verticalLayout_6.addWidget(self.btn_systems_menu)

        self.btn_transactions_menu = QPushButton(self.frame_menu_main)
        self.btn_transactions_menu.setObjectName(u"btn_transactions_menu")
        self.btn_transactions_menu.setEnabled(True)
        self.btn_transactions_menu.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon21.addFile(u":/icons/assets/icons/fi-sr-house-flag.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_transactions_menu.setIcon(icon21)
        self.btn_transactions_menu.setIconSize(QSize(28, 29))

        self.verticalLayout_6.addWidget(self.btn_transactions_menu)

        self.btn_reports_menu = QPushButton(self.frame_menu_main)
        self.btn_reports_menu.setObjectName(u"btn_reports_menu")
        self.btn_reports_menu.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon22.addFile(u":/icons/assets/icons/fi-sr-homework.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_reports_menu.setIcon(icon22)
        self.btn_reports_menu.setIconSize(QSize(35, 35))

        self.verticalLayout_6.addWidget(self.btn_reports_menu)

        self.vs_main = QSpacerItem(20, 106, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.vs_main)

        self.zz_btn_Disponible_menu = QPushButton(self.frame_menu_main)
        self.zz_btn_Disponible_menu.setObjectName(u"zz_btn_Disponible_menu")
        self.zz_btn_Disponible_menu.setEnabled(False)
        self.zz_btn_Disponible_menu.setMaximumSize(QSize(0, 0))
        self.zz_btn_Disponible_menu.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon23 = QIcon()
        icon23.addFile(u":/icons/assets/icons/fi-sr-house-blank.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zz_btn_Disponible_menu.setIcon(icon23)
        self.zz_btn_Disponible_menu.setIconSize(QSize(35, 36))

        self.verticalLayout_6.addWidget(self.zz_btn_Disponible_menu)

        self.btn_settings_menu = QPushButton(self.frame_menu_main)
        self.btn_settings_menu.setObjectName(u"btn_settings_menu")
        self.btn_settings_menu.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon24 = QIcon()
        icon24.addFile(u":/icons/assets/icons/fi-sr-home-settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings_menu.setIcon(icon24)
        self.btn_settings_menu.setIconSize(QSize(35, 35))

        self.verticalLayout_6.addWidget(self.btn_settings_menu)

        self.btn_log_out = QPushButton(self.frame_menu_main)
        self.btn_log_out.setObjectName(u"btn_log_out")
        self.btn_log_out.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon25 = QIcon()
        icon25.addFile(u":/icons/assets/icons/fi-sr-house-return.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_log_out.setIcon(icon25)
        self.btn_log_out.setIconSize(QSize(35, 35))

        self.verticalLayout_6.addWidget(self.btn_log_out)


        self.horizontalLayout.addWidget(self.frame_menu_main)

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
        icon26 = QIcon()
        icon26.addFile(u":/icons/assets/icons/sys01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_sistema.setIcon(icon26)
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
        icon27 = QIcon()
        icon27.addFile(u":/icons/assets/icons/mbd_01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_mbd.setIcon(icon27)
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
        icon28 = QIcon()
        icon28.addFile(u":/icons/assets/icons/cpu01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_cpu.setIcon(icon28)
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
        icon29 = QIcon()
        icon29.addFile(u":/icons/assets/icons/Grafica01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_gpu.setIcon(icon29)
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
        icon30 = QIcon()
        icon30.addFile(u":/icons/assets/icons/RAM.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_ram.setIcon(icon30)
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
        icon31 = QIcon()
        icon31.addFile(u":/icons/assets/icons/hdd03.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_hdd.setIcon(icon31)
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
        icon32 = QIcon()
        icon32.addFile(u":/icons/assets/icons/nic01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_nic.setIcon(icon32)
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
        icon33 = QIcon()
        icon33.addFile(u":/icons/assets/icons/audio01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_audio.setIcon(icon33)
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
        icon34 = QIcon()
        icon34.addFile(u":/icons/assets/icons/com02.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_com.setIcon(icon34)
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
        icon35 = QIcon()
        icon35.addFile(u":/icons/assets/icons/usb03.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_usb.setIcon(icon35)
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
        icon36 = QIcon()
        icon36.addFile(u":/icons/assets/icons/bluetootht.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_bth.setIcon(icon36)
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
        self.btn_regresar_menu.setIcon(icon18)
        self.btn_regresar_menu.setIconSize(QSize(35, 35))

        self.vly_frame_sub_hardware.addWidget(self.btn_regresar_menu)


        self.horizontalLayout.addWidget(self.frame_sub_hardware)

        self.frame_menu_transactions = QFrame(self.frame_inferior)
        self.frame_menu_transactions.setObjectName(u"frame_menu_transactions")
        self.frame_menu_transactions.setMinimumSize(QSize(0, 0))
        self.frame_menu_transactions.setMaximumSize(QSize(0, 16777215))
        self.frame_menu_transactions.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}")
        self.frame_menu_transactions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu_transactions.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_4 = QVBoxLayout(self.frame_menu_transactions)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_ark_requests = QPushButton(self.frame_menu_transactions)
        self.btn_ark_requests.setObjectName(u"btn_ark_requests")
        self.btn_ark_requests.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(True)
        font2.setKerning(False)
        self.btn_ark_requests.setFont(font2)
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
        icon37 = QIcon()
        icon37.addFile(u":/icons/assets/icons/fi-sr-code-pull-request.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ark_requests.setIcon(icon37)
        self.btn_ark_requests.setIconSize(QSize(35, 35))

        self.verticalLayout_4.addWidget(self.btn_ark_requests)

        self.btn_ark_sessions = QPushButton(self.frame_menu_transactions)
        self.btn_ark_sessions.setObjectName(u"btn_ark_sessions")
        self.btn_ark_sessions.setMinimumSize(QSize(0, 0))
        self.btn_ark_sessions.setFont(font2)
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
        self.btn_ark_sessions.setIcon(icon12)
        self.btn_ark_sessions.setIconSize(QSize(35, 35))

        self.verticalLayout_4.addWidget(self.btn_ark_sessions)

        self.btn_menu_ppal = QPushButton(self.frame_menu_transactions)
        self.btn_menu_ppal.setObjectName(u"btn_menu_ppal")
        self.btn_menu_ppal.setMinimumSize(QSize(0, 0))
        self.btn_menu_ppal.setFont(font2)
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
        self.btn_menu_ppal.setIcon(icon18)
        self.btn_menu_ppal.setIconSize(QSize(35, 35))

        self.verticalLayout_4.addWidget(self.btn_menu_ppal)


        self.horizontalLayout.addWidget(self.frame_menu_transactions)

        self.frame_menu_systems = QFrame(self.frame_inferior)
        self.frame_menu_systems.setObjectName(u"frame_menu_systems")
        self.frame_menu_systems.setEnabled(True)
        self.frame_menu_systems.setMinimumSize(QSize(0, 0))
        self.frame_menu_systems.setMaximumSize(QSize(0, 16777215))
        self.frame_menu_systems.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}")
        self.frame_menu_systems.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu_systems.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menu_systems)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_info_hardware = QPushButton(self.frame_menu_systems)
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
        icon38 = QIcon()
        icon38.addFile(u":/icons/assets/icons/PC01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_hardware.setIcon(icon38)
        self.btn_info_hardware.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_info_hardware)

        self.btn_info_red = QPushButton(self.frame_menu_systems)
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
        icon39 = QIcon()
        icon39.addFile(u":/icons/assets/icons/Red01.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_red.setIcon(icon39)
        self.btn_info_red.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_info_red)

        self.btn_info_so = QPushButton(self.frame_menu_systems)
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
        icon40 = QIcon()
        icon40.addFile(u":/icons/assets/icons/fi-sr-computer-classic.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_so.setIcon(icon40)
        self.btn_info_so.setIconSize(QSize(35, 36))

        self.verticalLayout_3.addWidget(self.btn_info_so)

        self.btn_info_regional = QPushButton(self.frame_menu_systems)
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
        icon41 = QIcon()
        icon41.addFile(u":/icons/assets/icons/Regional01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_regional.setIcon(icon41)
        self.btn_info_regional.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_info_regional)

        self.btn_limpiar = QPushButton(self.frame_menu_systems)
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
        icon42 = QIcon()
        icon42.addFile(u":/icons/assets/icons/Clear01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_limpiar.setIcon(icon42)
        self.btn_limpiar.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_limpiar)

        self.btn_menu_sys_ppal = QPushButton(self.frame_menu_systems)
        self.btn_menu_sys_ppal.setObjectName(u"btn_menu_sys_ppal")
        self.btn_menu_sys_ppal.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_menu_sys_ppal.setIcon(icon6)
        self.btn_menu_sys_ppal.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.btn_menu_sys_ppal)


        self.horizontalLayout.addWidget(self.frame_menu_systems)

        self.frame_consolas = QFrame(self.frame_inferior)
        self.frame_consolas.setObjectName(u"frame_consolas")
        self.frame_consolas.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_consolas.sizePolicy().hasHeightForWidth())
        self.frame_consolas.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.sw_consolas.sizePolicy().hasHeightForWidth())
        self.sw_consolas.setSizePolicy(sizePolicy1)
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
"    background-color: rgb(255, 255, 255)\n"
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
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        self.title_arktoolspc.setFont(font3)
        self.title_arktoolspc.setStyleSheet(u"")
        self.title_arktoolspc.setFrameShadow(QFrame.Shadow.Sunken)
        self.title_arktoolspc.setTextFormat(Qt.TextFormat.PlainText)
        self.title_arktoolspc.setPixmap(QPixmap(u":/images/assets/images/ArlToolsPC2.png"))
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
        sizePolicy.setHeightForWidth(self.label_logo_tools.sizePolicy().hasHeightForWidth())
        self.label_logo_tools.setSizePolicy(sizePolicy)
        self.label_logo_tools.setMinimumSize(QSize(164, 164))
        self.label_logo_tools.setMaximumSize(QSize(200, 200))
        self.label_logo_tools.setAutoFillBackground(False)
        self.label_logo_tools.setStyleSheet(u"")
        self.label_logo_tools.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_logo_tools.setPixmap(QPixmap(u":/images/assets/images/ArkToolsPC_02.png"))
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
        self.pie_arkinfo.setFont(font3)
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
        self.label_info_hw.setPixmap(QPixmap(u":/icons/assets/icons/sys01.svg"))
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
        self.frame_settings = QFrame(self.page_inf_config)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_settings.setFrameShadow(QFrame.Shadow.Raised)
        self.hly_frame_config = QHBoxLayout(self.frame_settings)
        self.hly_frame_config.setSpacing(0)
        self.hly_frame_config.setObjectName(u"hly_frame_config")
        self.hly_frame_config.setContentsMargins(0, 0, 0, 0)
        self.frame_btns_config = QFrame(self.frame_settings)
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
        self.verticalLayout_7 = QVBoxLayout(self.frame_btns_config)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_cambio_regional = QPushButton(self.frame_btns_config)
        self.btn_cambio_regional.setObjectName(u"btn_cambio_regional")
        self.btn_cambio_regional.setMinimumSize(QSize(170, 90))
        self.btn_cambio_regional.setMaximumSize(QSize(170, 90))
        font4 = QFont()
        font4.setBold(True)
        self.btn_cambio_regional.setFont(font4)
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
        icon43 = QIcon()
        icon43.addFile(u":/icons/assets/icons/fi-sr-workflow-setting.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cambio_regional.setIcon(icon43)
        self.btn_cambio_regional.setIconSize(QSize(35, 35))

        self.verticalLayout_7.addWidget(self.btn_cambio_regional)

        self.btn_config_sql_tools = QPushButton(self.frame_btns_config)
        self.btn_config_sql_tools.setObjectName(u"btn_config_sql_tools")
        self.btn_config_sql_tools.setMinimumSize(QSize(170, 90))
        self.btn_config_sql_tools.setMaximumSize(QSize(170, 90))
        self.btn_config_sql_tools.setFont(font4)
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
        icon44 = QIcon()
        icon44.addFile(u":/icons/assets/icons/fi-sr-sql-server.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_config_sql_tools.setIcon(icon44)
        self.btn_config_sql_tools.setIconSize(QSize(35, 35))

        self.verticalLayout_7.addWidget(self.btn_config_sql_tools)

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
        icon45 = QIcon()
        icon45.addFile(u":/icons/assets/icons/filesettings_102180.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_config_tools.setIcon(icon45)
        self.btn_config_tools.setIconSize(QSize(35, 35))

        self.verticalLayout_7.addWidget(self.btn_config_tools)

        self.btn_menu_cnf_ppal = QPushButton(self.frame_btns_config)
        self.btn_menu_cnf_ppal.setObjectName(u"btn_menu_cnf_ppal")
        self.btn_menu_cnf_ppal.setMinimumSize(QSize(170, 0))
        self.btn_menu_cnf_ppal.setFont(font2)
        self.btn_menu_cnf_ppal.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_menu_cnf_ppal.setIcon(icon18)
        self.btn_menu_cnf_ppal.setIconSize(QSize(35, 35))

        self.verticalLayout_7.addWidget(self.btn_menu_cnf_ppal)


        self.hly_frame_config.addWidget(self.frame_btns_config)

        self.textEdit_info_config = QTextEdit(self.frame_settings)
        self.textEdit_info_config.setObjectName(u"textEdit_info_config")
        self.textEdit_info_config.setEnabled(False)
        self.textEdit_info_config.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.textEdit_info_config.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: rgb(170, 170, 127);")

        self.hly_frame_config.addWidget(self.textEdit_info_config)


        self.vly_page_inf_config.addWidget(self.frame_settings)

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
        sizePolicy1.setHeightForWidth(self.page_forms.sizePolicy().hasHeightForWidth())
        self.page_forms.setSizePolicy(sizePolicy1)
        self.page_forms.setMinimumSize(QSize(825, 544))
        self.page_forms.setMaximumSize(QSize(1920, 1080))
        self.page_forms.setStyleSheet(u"")
        self.hly_page_forms = QHBoxLayout(self.page_forms)
        self.hly_page_forms.setSpacing(4)
        self.hly_page_forms.setObjectName(u"hly_page_forms")
        self.hly_page_forms.setContentsMargins(0, 0, 0, 0)
        self.qsw_forms = QStackedWidget(self.page_forms)
        self.qsw_forms.setObjectName(u"qsw_forms")
        sizePolicy1.setHeightForWidth(self.qsw_forms.sizePolicy().hasHeightForWidth())
        self.qsw_forms.setSizePolicy(sizePolicy1)
        self.qsw_forms.setMinimumSize(QSize(825, 544))
        self.qsw_forms.setMaximumSize(QSize(1920, 1080))
        self.qsw_forms.setStyleSheet(u"")
        self.page_frm_currencies = QWidget()
        self.page_frm_currencies.setObjectName(u"page_frm_currencies")
        sizePolicy1.setHeightForWidth(self.page_frm_currencies.sizePolicy().hasHeightForWidth())
        self.page_frm_currencies.setSizePolicy(sizePolicy1)
        self.page_frm_currencies.setMinimumSize(QSize(825, 544))
        self.page_frm_currencies.setMaximumSize(QSize(1920, 1080))
        self.page_frm_currencies.setStyleSheet(u"")
        self.hly_frm_currencies = QHBoxLayout(self.page_frm_currencies)
        self.hly_frm_currencies.setSpacing(0)
        self.hly_frm_currencies.setObjectName(u"hly_frm_currencies")
        self.hly_frm_currencies.setContentsMargins(0, 0, 0, 0)
        self.frm_form_currencies = QFrame(self.page_frm_currencies)
        self.frm_form_currencies.setObjectName(u"frm_form_currencies")
        sizePolicy1.setHeightForWidth(self.frm_form_currencies.sizePolicy().hasHeightForWidth())
        self.frm_form_currencies.setSizePolicy(sizePolicy1)
        self.frm_form_currencies.setMinimumSize(QSize(625, 0))
        self.frm_form_currencies.setMaximumSize(QSize(1920, 1080))
        self.frm_form_currencies.setFont(font3)
        self.frm_form_currencies.setStyleSheet(u"")
        self.frm_form_currencies.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_currencies.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frm_form_currencies)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.frm_currencies = QFrame(self.frm_form_currencies)
        self.frm_currencies.setObjectName(u"frm_currencies")
        sizePolicy1.setHeightForWidth(self.frm_currencies.sizePolicy().hasHeightForWidth())
        self.frm_currencies.setSizePolicy(sizePolicy1)
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
"    \n"
"}\n"
"\n"
"/* Estilo de QDoubleSpinBox */\n"
"QDoubleSpinBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"    \n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255"
                        ", 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";  \n"
"    padding: 0px 5px;       \n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\"; \n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255); /* Color de realce de tu tema */\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"/* Estilo de QDateEdit */\n"
"QDateEdit {\n"
"  "
                        "  background-color: rgb(255, 255, 255); /* Color de fondo */\n"
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
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco para el cuerpo */\n"
"}\n"
"/* --- ESTADO DESHABILITADO REFORZADO --- */\n"
"\n"
"QLineEdit:disabled, \n"
""
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
"}\n"
"/* Forzamos el QDoubleSpinBox */\n"
"QDoubleSpinBox::disabled {\n"
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
        sizePolicy.setHeightForWidth(self.cmb_mda_iso4217.sizePolicy().hasHeightForWidth())
        self.cmb_mda_iso4217.setSizePolicy(sizePolicy)
        self.cmb_mda_iso4217.setMinimumSize(QSize(80, 20))
        self.cmb_mda_iso4217.setMaximumSize(QSize(80, 20))
        self.cmb_mda_iso4217.setStyleSheet(u"")
        self.label_mda_symbol = QLabel(self.grb_currencies)
        self.label_mda_symbol.setObjectName(u"label_mda_symbol")
        self.label_mda_symbol.setGeometry(QRect(387, 90, 105, 20))
        self.label_mda_symbol.setMinimumSize(QSize(105, 20))
        self.label_mda_symbol.setMaximumSize(QSize(105, 20))
        self.label_mda_description = QLabel(self.grb_currencies)
        self.label_mda_description.setObjectName(u"label_mda_description")
        self.label_mda_description.setGeometry(QRect(15, 60, 91, 16))
        self.label_mda_description.setMaximumSize(QSize(150, 20))
        self.lineEdit_mda_code = QLineEdit(self.grb_currencies)
        self.lineEdit_mda_code.setObjectName(u"lineEdit_mda_code")
        self.lineEdit_mda_code.setGeometry(QRect(90, 30, 100, 20))
        sizePolicy.setHeightForWidth(self.lineEdit_mda_code.sizePolicy().hasHeightForWidth())
        self.lineEdit_mda_code.setSizePolicy(sizePolicy)
        self.lineEdit_mda_code.setMaximumSize(QSize(100, 20))
        self.lineEdit_mda_description = QLineEdit(self.grb_currencies)
        self.lineEdit_mda_description.setObjectName(u"lineEdit_mda_description")
        self.lineEdit_mda_description.setGeometry(QRect(111, 60, 400, 20))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_mda_description.sizePolicy().hasHeightForWidth())
        self.lineEdit_mda_description.setSizePolicy(sizePolicy2)
        self.lineEdit_mda_description.setMinimumSize(QSize(400, 20))
        self.lineEdit_mda_description.setMaximumSize(QSize(400, 20))
        self.lineEdit_mda_description.setStyleSheet(u"")
        self.label_mda_iso4217 = QLabel(self.grb_currencies)
        self.label_mda_iso4217.setObjectName(u"label_mda_iso4217")
        self.label_mda_iso4217.setGeometry(QRect(15, 90, 65, 20))
        self.label_mda_iso4217.setMinimumSize(QSize(65, 20))
        self.label_mda_iso4217.setMaximumSize(QSize(65, 20))
        self.label_mda_status = QLabel(self.grb_currencies)
        self.label_mda_status.setObjectName(u"label_mda_status")
        self.label_mda_status.setGeometry(QRect(440, 30, 49, 16))
        self.label_mda_status.setMaximumSize(QSize(100, 20))
        self.label_mda_code = QLabel(self.grb_currencies)
        self.label_mda_code.setObjectName(u"label_mda_code")
        self.label_mda_code.setGeometry(QRect(15, 30, 49, 16))
        self.label_mda_code.setMaximumSize(QSize(100, 20))
        self.label_mda_code.setAutoFillBackground(False)
        self.cmb_mda_status = QComboBox(self.grb_currencies)
        self.cmb_mda_status.addItem("")
        self.cmb_mda_status.addItem("")
        self.cmb_mda_status.setObjectName(u"cmb_mda_status")
        self.cmb_mda_status.setGeometry(QRect(498, 30, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_mda_status.sizePolicy().hasHeightForWidth())
        self.cmb_mda_status.setSizePolicy(sizePolicy)
        self.cmb_mda_status.setMinimumSize(QSize(80, 20))
        self.cmb_mda_status.setMaximumSize(QSize(80, 20))
        self.cmb_mda_status.setStyleSheet(u"")
        self.cmb_mda_symbol = QComboBox(self.grb_currencies)
        self.cmb_mda_symbol.addItem("")
        self.cmb_mda_symbol.addItem("")
        self.cmb_mda_symbol.addItem("")
        self.cmb_mda_symbol.setObjectName(u"cmb_mda_symbol")
        self.cmb_mda_symbol.setGeometry(QRect(498, 90, 80, 20))
        sizePolicy.setHeightForWidth(self.cmb_mda_symbol.sizePolicy().hasHeightForWidth())
        self.cmb_mda_symbol.setSizePolicy(sizePolicy)
        self.cmb_mda_symbol.setMinimumSize(QSize(80, 20))
        self.cmb_mda_symbol.setMaximumSize(QSize(80, 20))
        self.cmb_mda_symbol.setStyleSheet(u"")
        self.label_mda_operator = QLabel(self.grb_currencies)
        self.label_mda_operator.setObjectName(u"label_mda_operator")
        self.label_mda_operator.setGeometry(QRect(15, 130, 80, 16))
        self.label_mda_operator.setMaximumSize(QSize(150, 20))
        self.cmb_mda_operator = QComboBox(self.grb_currencies)
        self.cmb_mda_operator.addItem("")
        self.cmb_mda_operator.addItem("")
        self.cmb_mda_operator.setObjectName(u"cmb_mda_operator")
        self.cmb_mda_operator.setGeometry(QRect(111, 130, 120, 20))
        sizePolicy.setHeightForWidth(self.cmb_mda_operator.sizePolicy().hasHeightForWidth())
        self.cmb_mda_operator.setSizePolicy(sizePolicy)
        self.cmb_mda_operator.setMinimumSize(QSize(120, 20))
        self.cmb_mda_operator.setMaximumSize(QSize(120, 20))
        self.cmb_mda_operator.setStyleSheet(u"")

        self.vly_frm_currencies.addWidget(self.grb_currencies)

        self.grb_mda_management = QGroupBox(self.frm_currencies)
        self.grb_mda_management.setObjectName(u"grb_mda_management")
        self.grb_mda_management.setMinimumSize(QSize(0, 0))
        self.grb_mda_management.setMaximumSize(QSize(625, 210))
        self.grb_mda_management.setStyleSheet(u"")
        self.label_mda_update_date = QLabel(self.grb_mda_management)
        self.label_mda_update_date.setObjectName(u"label_mda_update_date")
        self.label_mda_update_date.setGeometry(QRect(15, 30, 140, 20))
        self.label_mda_update_date.setMinimumSize(QSize(140, 20))
        self.label_mda_update_date.setMaximumSize(QSize(140, 20))
        self.dateEdit_mda_update_date = QDateEdit(self.grb_mda_management)
        self.dateEdit_mda_update_date.setObjectName(u"dateEdit_mda_update_date")
        self.dateEdit_mda_update_date.setGeometry(QRect(160, 30, 100, 20))
        self.dateEdit_mda_update_date.setMaximumSize(QSize(100, 20))
        self.dateEdit_mda_update_date.setStyleSheet(u"")
        self.dateEdit_mda_update_date.setCalendarPopup(True)
        self.label_mda_passivefactor = QLabel(self.grb_mda_management)
        self.label_mda_passivefactor.setObjectName(u"label_mda_passivefactor")
        self.label_mda_passivefactor.setGeometry(QRect(357, 70, 105, 20))
        self.label_mda_passivefactor.setMinimumSize(QSize(105, 20))
        self.label_mda_passivefactor.setMaximumSize(QSize(105, 20))
        self.label_mda_passivefactor.setAutoFillBackground(False)
        self.label_mda_passivefactor.setTextFormat(Qt.TextFormat.AutoText)
        self.label_mda_activefactor = QLabel(self.grb_mda_management)
        self.label_mda_activefactor.setObjectName(u"label_mda_activefactor")
        self.label_mda_activefactor.setGeometry(QRect(20, 70, 105, 20))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(10)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_mda_activefactor.sizePolicy().hasHeightForWidth())
        self.label_mda_activefactor.setSizePolicy(sizePolicy3)
        self.label_mda_activefactor.setMinimumSize(QSize(105, 20))
        self.label_mda_activefactor.setMaximumSize(QSize(105, 20))
        self.label_mda_activefactor.setAutoFillBackground(False)
        self.dateEdit_mda_last_date = QDateEdit(self.grb_mda_management)
        self.dateEdit_mda_last_date.setObjectName(u"dateEdit_mda_last_date")
        self.dateEdit_mda_last_date.setGeometry(QRect(470, 30, 100, 20))
        self.dateEdit_mda_last_date.setMaximumSize(QSize(100, 20))
        self.dateEdit_mda_last_date.setStyleSheet(u"")
        self.dateEdit_mda_last_date.setCalendarPopup(True)
        self.label_mda_last_date = QLabel(self.grb_mda_management)
        self.label_mda_last_date.setObjectName(u"label_mda_last_date")
        self.label_mda_last_date.setGeometry(QRect(320, 30, 145, 20))
        self.label_mda_last_date.setMinimumSize(QSize(145, 20))
        self.label_mda_last_date.setMaximumSize(QSize(145, 20))
        self.dsb_mda_activefactor = QDoubleSpinBox(self.grb_mda_management)
        self.dsb_mda_activefactor.setObjectName(u"dsb_mda_activefactor")
        self.dsb_mda_activefactor.setGeometry(QRect(160, 70, 100, 20))
        self.dsb_mda_activefactor.setMinimumSize(QSize(100, 20))
        self.dsb_mda_activefactor.setMaximumSize(QSize(100, 20))
        self.dsb_mda_activefactor.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.dsb_mda_activefactor.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dsb_mda_activefactor.setDecimals(4)
        self.dsb_mda_activefactor.setMaximum(999999990000.000000000000000)
        self.dsb_mda_activefactor.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.dsb_mda_passivefactor = QDoubleSpinBox(self.grb_mda_management)
        self.dsb_mda_passivefactor.setObjectName(u"dsb_mda_passivefactor")
        self.dsb_mda_passivefactor.setGeometry(QRect(470, 70, 100, 20))
        self.dsb_mda_passivefactor.setMinimumSize(QSize(100, 20))
        self.dsb_mda_passivefactor.setMaximumSize(QSize(100, 20))
        self.dsb_mda_passivefactor.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.dsb_mda_passivefactor.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dsb_mda_passivefactor.setDecimals(4)
        self.dsb_mda_passivefactor.setMaximum(999999990000.000000000000000)
        self.dsb_mda_passivefactor.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.dateEdit_mda_creationdate = QDateEdit(self.grb_mda_management)
        self.dateEdit_mda_creationdate.setObjectName(u"dateEdit_mda_creationdate")
        self.dateEdit_mda_creationdate.setGeometry(QRect(160, 110, 100, 20))
        sizePolicy.setHeightForWidth(self.dateEdit_mda_creationdate.sizePolicy().hasHeightForWidth())
        self.dateEdit_mda_creationdate.setSizePolicy(sizePolicy)
        self.dateEdit_mda_creationdate.setMaximumSize(QSize(100, 20))
        self.dateEdit_mda_creationdate.setStyleSheet(u"")
        self.dateEdit_mda_creationdate.setCalendarPopup(True)
        self.label_mda_creationdate = QLabel(self.grb_mda_management)
        self.label_mda_creationdate.setObjectName(u"label_mda_creationdate")
        self.label_mda_creationdate.setGeometry(QRect(15, 110, 130, 20))
        self.label_mda_creationdate.setMinimumSize(QSize(130, 20))
        self.label_mda_creationdate.setMaximumSize(QSize(130, 20))

        self.vly_frm_currencies.addWidget(self.grb_mda_management)

        self.vly_frm_currencies.setStretch(0, 1)
        self.vly_frm_currencies.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frm_currencies)

        self.frm_bar_currencies = QFrame(self.frm_form_currencies)
        self.frm_bar_currencies.setObjectName(u"frm_bar_currencies")
        sizePolicy.setHeightForWidth(self.frm_bar_currencies.sizePolicy().hasHeightForWidth())
        self.frm_bar_currencies.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.btn_add_currencies.sizePolicy().hasHeightForWidth())
        self.btn_add_currencies.setSizePolicy(sizePolicy)
        self.btn_add_currencies.setMinimumSize(QSize(118, 48))
        self.btn_add_currencies.setMaximumSize(QSize(118, 48))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(True)
        font5.setItalic(False)
        self.btn_add_currencies.setFont(font5)
        self.btn_add_currencies.setStyleSheet(u"")
        icon46 = QIcon()
        icon46.addFile(u":/icons/assets/icons/001-Bar-Incluir", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_add_currencies.setIcon(icon46)
        self.btn_add_currencies.setIconSize(QSize(22, 22))

        self.hly_frm_bar_currencies.addWidget(self.btn_add_currencies)

        self.btn_save_currencies = QPushButton(self.frm_bar_currencies)
        self.btn_save_currencies.setObjectName(u"btn_save_currencies")
        self.btn_save_currencies.setMinimumSize(QSize(118, 48))
        self.btn_save_currencies.setMaximumSize(QSize(118, 48))
        self.btn_save_currencies.setFont(font5)
        self.btn_save_currencies.setStyleSheet(u"")
        icon47 = QIcon()
        icon47.addFile(u":/icons/assets/icons/001-Bar-Guardar", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save_currencies.setIcon(icon47)
        self.btn_save_currencies.setIconSize(QSize(22, 22))

        self.hly_frm_bar_currencies.addWidget(self.btn_save_currencies)

        self.btn_edit_currencies = QPushButton(self.frm_bar_currencies)
        self.btn_edit_currencies.setObjectName(u"btn_edit_currencies")
        sizePolicy.setHeightForWidth(self.btn_edit_currencies.sizePolicy().hasHeightForWidth())
        self.btn_edit_currencies.setSizePolicy(sizePolicy)
        self.btn_edit_currencies.setMinimumSize(QSize(118, 48))
        self.btn_edit_currencies.setMaximumSize(QSize(118, 48))
        self.btn_edit_currencies.setFont(font5)
        self.btn_edit_currencies.setStyleSheet(u"")
        icon48 = QIcon()
        icon48.addFile(u":/icons/assets/icons/001-Bar-Editar", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_edit_currencies.setIcon(icon48)
        self.btn_edit_currencies.setIconSize(QSize(22, 22))

        self.hly_frm_bar_currencies.addWidget(self.btn_edit_currencies)

        self.btn_cancel_currencies = QPushButton(self.frm_bar_currencies)
        self.btn_cancel_currencies.setObjectName(u"btn_cancel_currencies")
        self.btn_cancel_currencies.setMinimumSize(QSize(118, 48))
        self.btn_cancel_currencies.setMaximumSize(QSize(118, 48))
        self.btn_cancel_currencies.setFont(font5)
        self.btn_cancel_currencies.setStyleSheet(u"")
        icon49 = QIcon()
        icon49.addFile(u":/icons/assets/icons/001-Bar-Cancelar", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cancel_currencies.setIcon(icon49)
        self.btn_cancel_currencies.setIconSize(QSize(22, 22))

        self.hly_frm_bar_currencies.addWidget(self.btn_cancel_currencies)

        self.btn_delete_currencies = QPushButton(self.frm_bar_currencies)
        self.btn_delete_currencies.setObjectName(u"btn_delete_currencies")
        sizePolicy.setHeightForWidth(self.btn_delete_currencies.sizePolicy().hasHeightForWidth())
        self.btn_delete_currencies.setSizePolicy(sizePolicy)
        self.btn_delete_currencies.setMinimumSize(QSize(118, 48))
        self.btn_delete_currencies.setMaximumSize(QSize(118, 48))
        self.btn_delete_currencies.setStyleSheet(u"")
        icon50 = QIcon()
        icon50.addFile(u":/icons/assets/icons/001-Bar-Borrar", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_currencies.setIcon(icon50)
        self.btn_delete_currencies.setIconSize(QSize(22, 22))

        self.hly_frm_bar_currencies.addWidget(self.btn_delete_currencies)


        self.verticalLayout.addWidget(self.frm_bar_currencies)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)

        self.hly_frm_currencies.addWidget(self.frm_form_currencies)

        self.qsw_forms.addWidget(self.page_frm_currencies)
        self.page_frm_employees = QWidget()
        self.page_frm_employees.setObjectName(u"page_frm_employees")
        sizePolicy1.setHeightForWidth(self.page_frm_employees.sizePolicy().hasHeightForWidth())
        self.page_frm_employees.setSizePolicy(sizePolicy1)
        self.page_frm_employees.setMinimumSize(QSize(825, 544))
        self.page_frm_employees.setMaximumSize(QSize(1920, 1080))
        self.page_frm_employees.setStyleSheet(u"")
        self.hly_page_frm_employees = QHBoxLayout(self.page_frm_employees)
        self.hly_page_frm_employees.setSpacing(0)
        self.hly_page_frm_employees.setObjectName(u"hly_page_frm_employees")
        self.hly_page_frm_employees.setContentsMargins(0, 0, 0, 0)
        self.frm_form_employees = QFrame(self.page_frm_employees)
        self.frm_form_employees.setObjectName(u"frm_form_employees")
        sizePolicy1.setHeightForWidth(self.frm_form_employees.sizePolicy().hasHeightForWidth())
        self.frm_form_employees.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.frm_employees.sizePolicy().hasHeightForWidth())
        self.frm_employees.setSizePolicy(sizePolicy1)
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
"    \n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";  \n"
"    padding: 0px 5px;       \n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* C"
                        "olor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\"; \n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255); /* Color de realce de tu tema */\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
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
"    background-color: rgb(255"
                        ", 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco para el cuerpo */\n"
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
"    c"
                        "olor: #808080 !important;\n"
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
        self.label_emy_code = QLabel(self.grb_employees)
        self.label_emy_code.setObjectName(u"label_emy_code")
        self.label_emy_code.setGeometry(QRect(10, 30, 61, 20))
        self.label_emy_code.setMaximumSize(QSize(100, 20))
        self.label_emy_code.setAutoFillBackground(False)
        self.lineEdit_emy_code = QLineEdit(self.grb_employees)
        self.lineEdit_emy_code.setObjectName(u"lineEdit_emy_code")
        self.lineEdit_emy_code.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_emy_code.setMaximumSize(QSize(100, 20))
        self.label_emy_description = QLabel(self.grb_employees)
        self.label_emy_description.setObjectName(u"label_emy_description")
        self.label_emy_description.setGeometry(QRect(10, 60, 101, 20))
        self.label_emy_description.setMaximumSize(QSize(101, 20))
        self.lineEdit_emy_description = QLineEdit(self.grb_employees)
        self.lineEdit_emy_description.setObjectName(u"lineEdit_emy_description")
        self.lineEdit_emy_description.setGeometry(QRect(120, 60, 400, 20))
        self.lineEdit_emy_description.setMinimumSize(QSize(400, 20))
        self.lineEdit_emy_description.setMaximumSize(QSize(400, 20))
        self.lineEdit_emy_description.setStyleSheet(u"")
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
        sizePolicy1.setHeightForWidth(self.cmb_emy_status.sizePolicy().hasHeightForWidth())
        self.cmb_emy_status.setSizePolicy(sizePolicy1)
        self.cmb_emy_status.setMinimumSize(QSize(80, 20))
        self.cmb_emy_status.setMaximumSize(QSize(80, 20))
        self.cmb_emy_status.setStyleSheet(u"")

        self.vly__employees.addWidget(self.grb_employees)

        self.grb_address_phones_employees = QGroupBox(self.frm_employees)
        self.grb_address_phones_employees.setObjectName(u"grb_address_phones_employees")
        self.grb_address_phones_employees.setMinimumSize(QSize(0, 0))
        self.grb_address_phones_employees.setStyleSheet(u"")
        self.label_emy_phone = QLabel(self.grb_address_phones_employees)
        self.label_emy_phone.setObjectName(u"label_emy_phone")
        self.label_emy_phone.setGeometry(QRect(11, 30, 101, 20))
        self.label_emy_phone.setMaximumSize(QSize(150, 20))
        self.label_emy_role = QLabel(self.grb_address_phones_employees)
        self.label_emy_role.setObjectName(u"label_emy_role")
        self.label_emy_role.setGeometry(QRect(370, 30, 40, 20))
        self.label_emy_role.setMaximumSize(QSize(150, 20))
        self.lineEdit_emy_phone = QLineEdit(self.grb_address_phones_employees)
        self.lineEdit_emy_phone.setObjectName(u"lineEdit_emy_phone")
        self.lineEdit_emy_phone.setGeometry(QRect(120, 30, 165, 20))
        self.lineEdit_emy_phone.setMinimumSize(QSize(165, 0))
        self.lineEdit_emy_phone.setMaximumSize(QSize(165, 20))
        self.lineEdit_emy_role = QLineEdit(self.grb_address_phones_employees)
        self.lineEdit_emy_role.setObjectName(u"lineEdit_emy_role")
        self.lineEdit_emy_role.setGeometry(QRect(419, 30, 165, 20))
        self.lineEdit_emy_role.setMinimumSize(QSize(165, 0))
        self.lineEdit_emy_role.setMaximumSize(QSize(165, 20))
        self.label_emy_emailemployees = QLabel(self.grb_address_phones_employees)
        self.label_emy_emailemployees.setObjectName(u"label_emy_emailemployees")
        self.label_emy_emailemployees.setGeometry(QRect(11, 60, 101, 20))
        self.label_emy_emailemployees.setMaximumSize(QSize(150, 20))
        self.lineEdit_emy_emailemployees = QLineEdit(self.grb_address_phones_employees)
        self.lineEdit_emy_emailemployees.setObjectName(u"lineEdit_emy_emailemployees")
        self.lineEdit_emy_emailemployees.setGeometry(QRect(120, 60, 260, 20))
        self.lineEdit_emy_emailemployees.setMinimumSize(QSize(260, 0))
        self.lineEdit_emy_emailemployees.setMaximumSize(QSize(260, 20))

        self.vly__employees.addWidget(self.grb_address_phones_employees)

        self.grb_contacts__employees = QGroupBox(self.frm_employees)
        self.grb_contacts__employees.setObjectName(u"grb_contacts__employees")
        self.grb_contacts__employees.setMinimumSize(QSize(0, 0))
        self.grb_contacts__employees.setStyleSheet(u"")
        self.label_emy_client = QLabel(self.grb_contacts__employees)
        self.label_emy_client.setObjectName(u"label_emy_client")
        self.label_emy_client.setGeometry(QRect(10, 30, 110, 20))
        self.label_emy_client.setMinimumSize(QSize(110, 20))
        self.label_emy_client.setMaximumSize(QSize(110, 20))
        self.lineEdit_emy_id_client = QLineEdit(self.grb_contacts__employees)
        self.lineEdit_emy_id_client.setObjectName(u"lineEdit_emy_id_client")
        self.lineEdit_emy_id_client.setGeometry(QRect(120, 30, 400, 20))
        self.lineEdit_emy_id_client.setMinimumSize(QSize(400, 0))
        self.lineEdit_emy_id_client.setMaximumSize(QSize(400, 20))
        self.lineEdit_emy_id_client.setStyleSheet(u"")
        self.lineEdit_emy_id_client.setReadOnly(True)
        self.label_emy_password = QLabel(self.grb_contacts__employees)
        self.label_emy_password.setObjectName(u"label_emy_password")
        self.label_emy_password.setGeometry(QRect(386, 60, 80, 20))
        self.label_emy_password.setMinimumSize(QSize(80, 0))
        self.label_emy_password.setMaximumSize(QSize(80, 20))
        self.lineEdit_emy_password = QLineEdit(self.grb_contacts__employees)
        self.lineEdit_emy_password.setObjectName(u"lineEdit_emy_password")
        self.lineEdit_emy_password.setGeometry(QRect(470, 60, 100, 20))
        self.lineEdit_emy_password.setMaximumSize(QSize(100, 20))
        self.lineEdit_emy_position = QLineEdit(self.grb_contacts__employees)
        self.lineEdit_emy_position.setObjectName(u"lineEdit_emy_position")
        self.lineEdit_emy_position.setGeometry(QRect(120, 60, 165, 20))
        self.lineEdit_emy_position.setMinimumSize(QSize(165, 0))
        self.lineEdit_emy_position.setMaximumSize(QSize(165, 20))
        self.label_emy_position = QLabel(self.grb_contacts__employees)
        self.label_emy_position.setObjectName(u"label_emy_position")
        self.label_emy_position.setGeometry(QRect(10, 60, 110, 20))
        self.label_emy_position.setMinimumSize(QSize(110, 0))
        self.label_emy_position.setMaximumSize(QSize(110, 20))
        self.dateEdit_emy_creationdate = QDateEdit(self.grb_contacts__employees)
        self.dateEdit_emy_creationdate.setObjectName(u"dateEdit_emy_creationdate")
        self.dateEdit_emy_creationdate.setGeometry(QRect(142, 90, 100, 20))
        self.dateEdit_emy_creationdate.setMaximumSize(QSize(100, 20))
        self.dateEdit_emy_creationdate.setStyleSheet(u"")
        self.dateEdit_emy_creationdate.setCalendarPopup(True)
        self.label_emy_creationdate = QLabel(self.grb_contacts__employees)
        self.label_emy_creationdate.setObjectName(u"label_emy_creationdate")
        self.label_emy_creationdate.setGeometry(QRect(10, 90, 130, 20))
        self.label_emy_creationdate.setMaximumSize(QSize(130, 20))
        self.btn_search_emy_client = QPushButton(self.grb_contacts__employees)
        self.btn_search_emy_client.setObjectName(u"btn_search_emy_client")
        self.btn_search_emy_client.setGeometry(QRect(525, 30, 24, 24))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.btn_search_emy_client.sizePolicy().hasHeightForWidth())
        self.btn_search_emy_client.setSizePolicy(sizePolicy4)
        self.btn_search_emy_client.setMinimumSize(QSize(24, 24))
        self.btn_search_emy_client.setMaximumSize(QSize(24, 24))
        font6 = QFont()
        font6.setFamilies([u"Consolas"])
        font6.setBold(True)
        font6.setItalic(False)
        self.btn_search_emy_client.setFont(font6)
        self.btn_search_emy_client.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        icon51 = QIcon()
        icon51.addFile(u":/icons/assets/icons/fi-sr-search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_search_emy_client.setIcon(icon51)
        self.btn_search_emy_client.setIconSize(QSize(18, 18))

        self.vly__employees.addWidget(self.grb_contacts__employees)


        self.vly_frm_form_employees.addWidget(self.frm_employees)

        self.frm_bar_employees = QFrame(self.frm_form_employees)
        self.frm_bar_employees.setObjectName(u"frm_bar_employees")
        sizePolicy.setHeightForWidth(self.frm_bar_employees.sizePolicy().hasHeightForWidth())
        self.frm_bar_employees.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.btn_add_employees.sizePolicy().hasHeightForWidth())
        self.btn_add_employees.setSizePolicy(sizePolicy)
        self.btn_add_employees.setMinimumSize(QSize(118, 48))
        self.btn_add_employees.setMaximumSize(QSize(118, 48))
        self.btn_add_employees.setFont(font5)
        self.btn_add_employees.setStyleSheet(u"")
        self.btn_add_employees.setIcon(icon46)
        self.btn_add_employees.setIconSize(QSize(22, 22))

        self.hly_frm_bar_employees.addWidget(self.btn_add_employees)

        self.btn_save_employees = QPushButton(self.frm_bar_employees)
        self.btn_save_employees.setObjectName(u"btn_save_employees")
        self.btn_save_employees.setMinimumSize(QSize(118, 48))
        self.btn_save_employees.setMaximumSize(QSize(118, 48))
        self.btn_save_employees.setFont(font5)
        self.btn_save_employees.setStyleSheet(u"")
        self.btn_save_employees.setIcon(icon47)
        self.btn_save_employees.setIconSize(QSize(22, 22))

        self.hly_frm_bar_employees.addWidget(self.btn_save_employees)

        self.btn_edit_employees = QPushButton(self.frm_bar_employees)
        self.btn_edit_employees.setObjectName(u"btn_edit_employees")
        sizePolicy.setHeightForWidth(self.btn_edit_employees.sizePolicy().hasHeightForWidth())
        self.btn_edit_employees.setSizePolicy(sizePolicy)
        self.btn_edit_employees.setMinimumSize(QSize(118, 48))
        self.btn_edit_employees.setMaximumSize(QSize(118, 48))
        self.btn_edit_employees.setFont(font5)
        self.btn_edit_employees.setStyleSheet(u"")
        self.btn_edit_employees.setIcon(icon48)
        self.btn_edit_employees.setIconSize(QSize(22, 22))

        self.hly_frm_bar_employees.addWidget(self.btn_edit_employees)

        self.btn_cancel_employees = QPushButton(self.frm_bar_employees)
        self.btn_cancel_employees.setObjectName(u"btn_cancel_employees")
        self.btn_cancel_employees.setMinimumSize(QSize(118, 48))
        self.btn_cancel_employees.setMaximumSize(QSize(118, 48))
        self.btn_cancel_employees.setFont(font5)
        self.btn_cancel_employees.setStyleSheet(u"")
        self.btn_cancel_employees.setIcon(icon49)
        self.btn_cancel_employees.setIconSize(QSize(22, 22))

        self.hly_frm_bar_employees.addWidget(self.btn_cancel_employees)

        self.btn_delete_employees = QPushButton(self.frm_bar_employees)
        self.btn_delete_employees.setObjectName(u"btn_delete_employees")
        sizePolicy.setHeightForWidth(self.btn_delete_employees.sizePolicy().hasHeightForWidth())
        self.btn_delete_employees.setSizePolicy(sizePolicy)
        self.btn_delete_employees.setMinimumSize(QSize(118, 48))
        self.btn_delete_employees.setMaximumSize(QSize(118, 48))
        self.btn_delete_employees.setStyleSheet(u"")
        self.btn_delete_employees.setIcon(icon50)
        self.btn_delete_employees.setIconSize(QSize(22, 22))

        self.hly_frm_bar_employees.addWidget(self.btn_delete_employees)


        self.vly_frm_form_employees.addWidget(self.frm_bar_employees)

        self.vly_frm_form_employees.setStretch(0, 4)

        self.hly_page_frm_employees.addWidget(self.frm_form_employees)

        self.qsw_forms.addWidget(self.page_frm_employees)
        self.page_frm_device_types = QWidget()
        self.page_frm_device_types.setObjectName(u"page_frm_device_types")
        sizePolicy1.setHeightForWidth(self.page_frm_device_types.sizePolicy().hasHeightForWidth())
        self.page_frm_device_types.setSizePolicy(sizePolicy1)
        self.page_frm_device_types.setMinimumSize(QSize(825, 544))
        self.page_frm_device_types.setMaximumSize(QSize(1920, 1080))
        self.page_frm_device_types.setStyleSheet(u"")
        self.hly_page_frm_device_types = QHBoxLayout(self.page_frm_device_types)
        self.hly_page_frm_device_types.setSpacing(0)
        self.hly_page_frm_device_types.setObjectName(u"hly_page_frm_device_types")
        self.hly_page_frm_device_types.setContentsMargins(0, 0, 0, 0)
        self.frm_form_device_types = QFrame(self.page_frm_device_types)
        self.frm_form_device_types.setObjectName(u"frm_form_device_types")
        sizePolicy1.setHeightForWidth(self.frm_form_device_types.sizePolicy().hasHeightForWidth())
        self.frm_form_device_types.setSizePolicy(sizePolicy1)
        self.frm_form_device_types.setMinimumSize(QSize(625, 0))
        self.frm_form_device_types.setMaximumSize(QSize(1920, 1080))
        self.frm_form_device_types.setFont(font3)
        self.frm_form_device_types.setStyleSheet(u"")
        self.frm_form_device_types.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_device_types.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_device_types = QVBoxLayout(self.frm_form_device_types)
        self.vly_frm_form_device_types.setSpacing(2)
        self.vly_frm_form_device_types.setObjectName(u"vly_frm_form_device_types")
        self.vly_frm_form_device_types.setContentsMargins(4, 4, 4, 4)
        self.frm_device_types = QFrame(self.frm_form_device_types)
        self.frm_device_types.setObjectName(u"frm_device_types")
        sizePolicy1.setHeightForWidth(self.frm_device_types.sizePolicy().hasHeightForWidth())
        self.frm_device_types.setSizePolicy(sizePolicy1)
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
"    \n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";  \n"
"    padding: 0px 5px;       \n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* C"
                        "olor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\"; \n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255); /* Color de realce de tu tema */\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
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
"    background-color: rgb(255"
                        ", 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco para el cuerpo */\n"
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
"    c"
                        "olor: #808080 !important;\n"
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
        self.label_dty_code = QLabel(self.grb_device_types)
        self.label_dty_code.setObjectName(u"label_dty_code")
        self.label_dty_code.setGeometry(QRect(10, 30, 61, 20))
        self.label_dty_code.setMaximumSize(QSize(100, 20))
        self.label_dty_code.setAutoFillBackground(False)
        self.lineEdit_dty_code = QLineEdit(self.grb_device_types)
        self.lineEdit_dty_code.setObjectName(u"lineEdit_dty_code")
        self.lineEdit_dty_code.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_dty_code.setMaximumSize(QSize(100, 20))
        self.label_dty_description = QLabel(self.grb_device_types)
        self.label_dty_description.setObjectName(u"label_dty_description")
        self.label_dty_description.setGeometry(QRect(10, 60, 101, 20))
        self.label_dty_description.setMaximumSize(QSize(150, 20))
        self.lineEdit_dty_description = QLineEdit(self.grb_device_types)
        self.lineEdit_dty_description.setObjectName(u"lineEdit_dty_description")
        self.lineEdit_dty_description.setGeometry(QRect(120, 60, 400, 20))
        self.lineEdit_dty_description.setMinimumSize(QSize(400, 20))
        self.lineEdit_dty_description.setMaximumSize(QSize(400, 20))
        self.lineEdit_dty_description.setStyleSheet(u"")
        self.label_dty_status = QLabel(self.grb_device_types)
        self.label_dty_status.setObjectName(u"label_dty_status")
        self.label_dty_status.setGeometry(QRect(433, 30, 61, 20))
        self.label_dty_status.setMaximumSize(QSize(100, 20))
        self.cmb_dty_status = QComboBox(self.grb_device_types)
        self.cmb_dty_status.addItem("")
        self.cmb_dty_status.addItem("")
        self.cmb_dty_status.setObjectName(u"cmb_dty_status")
        self.cmb_dty_status.setGeometry(QRect(498, 30, 80, 20))
        sizePolicy1.setHeightForWidth(self.cmb_dty_status.sizePolicy().hasHeightForWidth())
        self.cmb_dty_status.setSizePolicy(sizePolicy1)
        self.cmb_dty_status.setMinimumSize(QSize(80, 20))
        self.cmb_dty_status.setMaximumSize(QSize(80, 24))
        self.cmb_dty_status.setStyleSheet(u"")
        self.label_dty_creationdate = QLabel(self.grb_device_types)
        self.label_dty_creationdate.setObjectName(u"label_dty_creationdate")
        self.label_dty_creationdate.setGeometry(QRect(10, 160, 130, 20))
        self.label_dty_creationdate.setMaximumSize(QSize(130, 20))
        self.dateEdit_dty_creationdate = QDateEdit(self.grb_device_types)
        self.dateEdit_dty_creationdate.setObjectName(u"dateEdit_dty_creationdate")
        self.dateEdit_dty_creationdate.setGeometry(QRect(145, 160, 100, 20))
        self.dateEdit_dty_creationdate.setMaximumSize(QSize(100, 20))
        self.dateEdit_dty_creationdate.setStyleSheet(u"")
        self.dateEdit_dty_creationdate.setCalendarPopup(True)
        self.label_dty_descripciontec = QLabel(self.grb_device_types)
        self.label_dty_descripciontec.setObjectName(u"label_dty_descripciontec")
        self.label_dty_descripciontec.setGeometry(QRect(10, 90, 100, 41))
        self.label_dty_descripciontec.setMinimumSize(QSize(100, 0))
        self.label_dty_descripciontec.setMaximumSize(QSize(100, 60))
        self.label_dty_descripciontec.setScaledContents(False)
        self.textEdit_dty_descriptiontech = QTextEdit(self.grb_device_types)
        self.textEdit_dty_descriptiontech.setObjectName(u"textEdit_dty_descriptiontech")
        self.textEdit_dty_descriptiontech.setGeometry(QRect(120, 90, 400, 60))
        self.textEdit_dty_descriptiontech.setMinimumSize(QSize(400, 60))
        self.textEdit_dty_descriptiontech.setMaximumSize(QSize(400, 60))
        self.textEdit_dty_descriptiontech.setStyleSheet(u"")

        self.vly_device_types.addWidget(self.grb_device_types)


        self.vly_frm_form_device_types.addWidget(self.frm_device_types)

        self.frm_bar_device_types = QFrame(self.frm_form_device_types)
        self.frm_bar_device_types.setObjectName(u"frm_bar_device_types")
        sizePolicy.setHeightForWidth(self.frm_bar_device_types.sizePolicy().hasHeightForWidth())
        self.frm_bar_device_types.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.btn_add_device_types.sizePolicy().hasHeightForWidth())
        self.btn_add_device_types.setSizePolicy(sizePolicy)
        self.btn_add_device_types.setMinimumSize(QSize(118, 48))
        self.btn_add_device_types.setMaximumSize(QSize(118, 48))
        self.btn_add_device_types.setFont(font5)
        self.btn_add_device_types.setStyleSheet(u"")
        self.btn_add_device_types.setIcon(icon46)
        self.btn_add_device_types.setIconSize(QSize(22, 22))

        self.hly_frm_bar_device_types.addWidget(self.btn_add_device_types)

        self.btn_save_device_types = QPushButton(self.frm_bar_device_types)
        self.btn_save_device_types.setObjectName(u"btn_save_device_types")
        self.btn_save_device_types.setMinimumSize(QSize(118, 48))
        self.btn_save_device_types.setMaximumSize(QSize(118, 48))
        self.btn_save_device_types.setFont(font5)
        self.btn_save_device_types.setStyleSheet(u"")
        self.btn_save_device_types.setIcon(icon47)
        self.btn_save_device_types.setIconSize(QSize(22, 22))

        self.hly_frm_bar_device_types.addWidget(self.btn_save_device_types)

        self.btn_edit_device_types = QPushButton(self.frm_bar_device_types)
        self.btn_edit_device_types.setObjectName(u"btn_edit_device_types")
        sizePolicy.setHeightForWidth(self.btn_edit_device_types.sizePolicy().hasHeightForWidth())
        self.btn_edit_device_types.setSizePolicy(sizePolicy)
        self.btn_edit_device_types.setMinimumSize(QSize(118, 48))
        self.btn_edit_device_types.setMaximumSize(QSize(118, 48))
        self.btn_edit_device_types.setFont(font5)
        self.btn_edit_device_types.setStyleSheet(u"")
        self.btn_edit_device_types.setIcon(icon48)
        self.btn_edit_device_types.setIconSize(QSize(22, 22))

        self.hly_frm_bar_device_types.addWidget(self.btn_edit_device_types)

        self.btn_cancel_device_types = QPushButton(self.frm_bar_device_types)
        self.btn_cancel_device_types.setObjectName(u"btn_cancel_device_types")
        self.btn_cancel_device_types.setMinimumSize(QSize(118, 48))
        self.btn_cancel_device_types.setMaximumSize(QSize(118, 48))
        self.btn_cancel_device_types.setFont(font5)
        self.btn_cancel_device_types.setStyleSheet(u"")
        self.btn_cancel_device_types.setIcon(icon49)
        self.btn_cancel_device_types.setIconSize(QSize(22, 22))

        self.hly_frm_bar_device_types.addWidget(self.btn_cancel_device_types)

        self.btn_delete_device_types = QPushButton(self.frm_bar_device_types)
        self.btn_delete_device_types.setObjectName(u"btn_delete_device_types")
        sizePolicy.setHeightForWidth(self.btn_delete_device_types.sizePolicy().hasHeightForWidth())
        self.btn_delete_device_types.setSizePolicy(sizePolicy)
        self.btn_delete_device_types.setMinimumSize(QSize(118, 48))
        self.btn_delete_device_types.setMaximumSize(QSize(118, 48))
        self.btn_delete_device_types.setStyleSheet(u"")
        self.btn_delete_device_types.setIcon(icon50)
        self.btn_delete_device_types.setIconSize(QSize(22, 22))

        self.hly_frm_bar_device_types.addWidget(self.btn_delete_device_types)


        self.vly_frm_form_device_types.addWidget(self.frm_bar_device_types)

        self.vly_frm_form_device_types.setStretch(0, 4)

        self.hly_page_frm_device_types.addWidget(self.frm_form_device_types)

        self.qsw_forms.addWidget(self.page_frm_device_types)
        self.page_frm_actions_categories = QWidget()
        self.page_frm_actions_categories.setObjectName(u"page_frm_actions_categories")
        sizePolicy1.setHeightForWidth(self.page_frm_actions_categories.sizePolicy().hasHeightForWidth())
        self.page_frm_actions_categories.setSizePolicy(sizePolicy1)
        self.page_frm_actions_categories.setMinimumSize(QSize(625, 544))
        self.page_frm_actions_categories.setMaximumSize(QSize(1920, 1080))
        self.page_frm_actions_categories.setStyleSheet(u"")
        self.hly_frm_action_categories = QHBoxLayout(self.page_frm_actions_categories)
        self.hly_frm_action_categories.setSpacing(0)
        self.hly_frm_action_categories.setObjectName(u"hly_frm_action_categories")
        self.hly_frm_action_categories.setContentsMargins(0, 0, 0, 0)
        self.frm_form_actions_categories = QFrame(self.page_frm_actions_categories)
        self.frm_form_actions_categories.setObjectName(u"frm_form_actions_categories")
        sizePolicy1.setHeightForWidth(self.frm_form_actions_categories.sizePolicy().hasHeightForWidth())
        self.frm_form_actions_categories.setSizePolicy(sizePolicy1)
        self.frm_form_actions_categories.setMinimumSize(QSize(825, 0))
        self.frm_form_actions_categories.setMaximumSize(QSize(1920, 1080))
        self.frm_form_actions_categories.setFont(font3)
        self.frm_form_actions_categories.setStyleSheet(u"")
        self.frm_form_actions_categories.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_actions_categories.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_action_categories = QVBoxLayout(self.frm_form_actions_categories)
        self.vly_frm_form_action_categories.setSpacing(3)
        self.vly_frm_form_action_categories.setObjectName(u"vly_frm_form_action_categories")
        self.vly_frm_form_action_categories.setContentsMargins(4, 4, 4, 4)
        self.frm_actions_categories = QFrame(self.frm_form_actions_categories)
        self.frm_actions_categories.setObjectName(u"frm_actions_categories")
        sizePolicy1.setHeightForWidth(self.frm_actions_categories.sizePolicy().hasHeightForWidth())
        self.frm_actions_categories.setSizePolicy(sizePolicy1)
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
"    \n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";  \n"
"    padding: 0px 5px;       \n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* C"
                        "olor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\"; \n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255); /* Color de realce de tu tema */\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
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
"    background-color: rgb(255"
                        ", 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco para el cuerpo */\n"
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
"    c"
                        "olor: #808080 !important;\n"
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
        self.label_cat_code = QLabel(self.grb_actions_categories)
        self.label_cat_code.setObjectName(u"label_cat_code")
        self.label_cat_code.setGeometry(QRect(10, 30, 61, 20))
        self.label_cat_code.setMaximumSize(QSize(100, 20))
        self.label_cat_code.setAutoFillBackground(False)
        self.lineEdit_cat_code = QLineEdit(self.grb_actions_categories)
        self.lineEdit_cat_code.setObjectName(u"lineEdit_cat_code")
        self.lineEdit_cat_code.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_cat_code.setMaximumSize(QSize(100, 20))
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
        self.cmb_cat_status = QComboBox(self.grb_actions_categories)
        self.cmb_cat_status.addItem("")
        self.cmb_cat_status.addItem("")
        self.cmb_cat_status.setObjectName(u"cmb_cat_status")
        self.cmb_cat_status.setGeometry(QRect(436, 30, 80, 20))
        sizePolicy1.setHeightForWidth(self.cmb_cat_status.sizePolicy().hasHeightForWidth())
        self.cmb_cat_status.setSizePolicy(sizePolicy1)
        self.cmb_cat_status.setMinimumSize(QSize(80, 20))
        self.cmb_cat_status.setMaximumSize(QSize(80, 20))
        self.cmb_cat_status.setStyleSheet(u"")
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
        sizePolicy.setHeightForWidth(self.frm_bar_action_categories.sizePolicy().hasHeightForWidth())
        self.frm_bar_action_categories.setSizePolicy(sizePolicy)
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
        self.btn_add_actions_categories.setFont(font5)
        self.btn_add_actions_categories.setStyleSheet(u"")
        self.btn_add_actions_categories.setIcon(icon46)
        self.btn_add_actions_categories.setIconSize(QSize(22, 22))

        self.hyl_frm_bar_action_categories.addWidget(self.btn_add_actions_categories)

        self.btn_save_actions_categories = QPushButton(self.frm_bar_action_categories)
        self.btn_save_actions_categories.setObjectName(u"btn_save_actions_categories")
        self.btn_save_actions_categories.setMinimumSize(QSize(118, 48))
        self.btn_save_actions_categories.setMaximumSize(QSize(118, 48))
        self.btn_save_actions_categories.setFont(font5)
        self.btn_save_actions_categories.setStyleSheet(u"")
        self.btn_save_actions_categories.setIcon(icon47)
        self.btn_save_actions_categories.setIconSize(QSize(22, 22))

        self.hyl_frm_bar_action_categories.addWidget(self.btn_save_actions_categories)

        self.btn_edit_actions_categories = QPushButton(self.frm_bar_action_categories)
        self.btn_edit_actions_categories.setObjectName(u"btn_edit_actions_categories")
        self.btn_edit_actions_categories.setMinimumSize(QSize(118, 48))
        self.btn_edit_actions_categories.setMaximumSize(QSize(118, 48))
        self.btn_edit_actions_categories.setFont(font5)
        self.btn_edit_actions_categories.setStyleSheet(u"")
        self.btn_edit_actions_categories.setIcon(icon48)
        self.btn_edit_actions_categories.setIconSize(QSize(22, 22))

        self.hyl_frm_bar_action_categories.addWidget(self.btn_edit_actions_categories)

        self.btn_cancel_actions_categories = QPushButton(self.frm_bar_action_categories)
        self.btn_cancel_actions_categories.setObjectName(u"btn_cancel_actions_categories")
        self.btn_cancel_actions_categories.setMinimumSize(QSize(118, 48))
        self.btn_cancel_actions_categories.setMaximumSize(QSize(118, 48))
        self.btn_cancel_actions_categories.setFont(font5)
        self.btn_cancel_actions_categories.setStyleSheet(u"")
        self.btn_cancel_actions_categories.setIcon(icon49)
        self.btn_cancel_actions_categories.setIconSize(QSize(22, 22))

        self.hyl_frm_bar_action_categories.addWidget(self.btn_cancel_actions_categories)

        self.btn_delete_actions_categories = QPushButton(self.frm_bar_action_categories)
        self.btn_delete_actions_categories.setObjectName(u"btn_delete_actions_categories")
        self.btn_delete_actions_categories.setMinimumSize(QSize(118, 48))
        self.btn_delete_actions_categories.setMaximumSize(QSize(118, 48))
        self.btn_delete_actions_categories.setFont(font5)
        self.btn_delete_actions_categories.setStyleSheet(u"")
        self.btn_delete_actions_categories.setIcon(icon50)
        self.btn_delete_actions_categories.setIconSize(QSize(22, 22))

        self.hyl_frm_bar_action_categories.addWidget(self.btn_delete_actions_categories)


        self.vly_frm_form_action_categories.addWidget(self.frm_bar_action_categories)

        self.vly_frm_form_action_categories.setStretch(0, 4)
        self.vly_frm_form_action_categories.setStretch(1, 1)

        self.hly_frm_action_categories.addWidget(self.frm_form_actions_categories, 0, Qt.AlignmentFlag.AlignLeft)

        self.qsw_forms.addWidget(self.page_frm_actions_categories)
        self.page_frm_it_assets = QWidget()
        self.page_frm_it_assets.setObjectName(u"page_frm_it_assets")
        sizePolicy1.setHeightForWidth(self.page_frm_it_assets.sizePolicy().hasHeightForWidth())
        self.page_frm_it_assets.setSizePolicy(sizePolicy1)
        self.page_frm_it_assets.setMinimumSize(QSize(825, 544))
        self.page_frm_it_assets.setMaximumSize(QSize(1920, 1080))
        self.page_frm_it_assets.setStyleSheet(u"")
        self.hly_page_frm_it_assets = QHBoxLayout(self.page_frm_it_assets)
        self.hly_page_frm_it_assets.setSpacing(0)
        self.hly_page_frm_it_assets.setObjectName(u"hly_page_frm_it_assets")
        self.hly_page_frm_it_assets.setContentsMargins(0, 0, 0, 0)
        self.frm_form_it_assets = QFrame(self.page_frm_it_assets)
        self.frm_form_it_assets.setObjectName(u"frm_form_it_assets")
        sizePolicy1.setHeightForWidth(self.frm_form_it_assets.sizePolicy().hasHeightForWidth())
        self.frm_form_it_assets.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.frm_it_assets.sizePolicy().hasHeightForWidth())
        self.frm_it_assets.setSizePolicy(sizePolicy1)
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
"    \n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";  \n"
"    padding: 0px 5px;       \n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* C"
                        "olor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\"; \n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255); /* Color de realce de tu tema */\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
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
"    background-color: rgb(255"
                        ", 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco para el cuerpo */\n"
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
"    c"
                        "olor: #808080 !important;\n"
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
        self.label_ita_code = QLabel(self.grb_it_assets)
        self.label_ita_code.setObjectName(u"label_ita_code")
        self.label_ita_code.setGeometry(QRect(10, 30, 61, 20))
        self.label_ita_code.setMaximumSize(QSize(100, 20))
        self.label_ita_code.setAutoFillBackground(False)
        self.lineEdit_ita_code = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_code.setObjectName(u"lineEdit_ita_code")
        self.lineEdit_ita_code.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_ita_code.setMaximumSize(QSize(100, 20))
        self.label_ita_description = QLabel(self.grb_it_assets)
        self.label_ita_description.setObjectName(u"label_ita_description")
        self.label_ita_description.setGeometry(QRect(10, 60, 101, 20))
        self.label_ita_description.setMaximumSize(QSize(150, 20))
        self.lineEdit_ita_description = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_description.setObjectName(u"lineEdit_ita_description")
        self.lineEdit_ita_description.setGeometry(QRect(102, 60, 400, 20))
        self.lineEdit_ita_description.setMinimumSize(QSize(400, 20))
        self.lineEdit_ita_description.setMaximumSize(QSize(400, 20))
        self.lineEdit_ita_description.setStyleSheet(u"")
        self.label_ita_brand = QLabel(self.grb_it_assets)
        self.label_ita_brand.setObjectName(u"label_ita_brand")
        self.label_ita_brand.setGeometry(QRect(10, 90, 61, 20))
        self.label_ita_brand.setMinimumSize(QSize(61, 0))
        self.label_ita_brand.setMaximumSize(QSize(61, 20))
        self.label_ita_status = QLabel(self.grb_it_assets)
        self.label_ita_status.setObjectName(u"label_ita_status")
        self.label_ita_status.setGeometry(QRect(433, 30, 61, 20))
        self.label_ita_status.setMaximumSize(QSize(100, 20))
        self.lineEdit_ita_brand = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_brand.setObjectName(u"lineEdit_ita_brand")
        self.lineEdit_ita_brand.setGeometry(QRect(78, 90, 100, 20))
        self.lineEdit_ita_brand.setMaximumSize(QSize(100, 20))
        self.cmb_ita_status = QComboBox(self.grb_it_assets)
        self.cmb_ita_status.addItem("")
        self.cmb_ita_status.addItem("")
        self.cmb_ita_status.setObjectName(u"cmb_ita_status")
        self.cmb_ita_status.setGeometry(QRect(498, 30, 80, 20))
        sizePolicy1.setHeightForWidth(self.cmb_ita_status.sizePolicy().hasHeightForWidth())
        self.cmb_ita_status.setSizePolicy(sizePolicy1)
        self.cmb_ita_status.setMinimumSize(QSize(80, 20))
        self.cmb_ita_status.setMaximumSize(QSize(80, 20))
        self.cmb_ita_status.setStyleSheet(u"")
        self.cmb_ita_classification = QComboBox(self.grb_it_assets)
        self.cmb_ita_classification.addItem("")
        self.cmb_ita_classification.addItem("")
        self.cmb_ita_classification.addItem("")
        self.cmb_ita_classification.addItem("")
        self.cmb_ita_classification.addItem("")
        self.cmb_ita_classification.addItem("")
        self.cmb_ita_classification.addItem("")
        self.cmb_ita_classification.addItem("")
        self.cmb_ita_classification.setObjectName(u"cmb_ita_classification")
        self.cmb_ita_classification.setGeometry(QRect(325, 90, 240, 20))
        sizePolicy1.setHeightForWidth(self.cmb_ita_classification.sizePolicy().hasHeightForWidth())
        self.cmb_ita_classification.setSizePolicy(sizePolicy1)
        self.cmb_ita_classification.setMinimumSize(QSize(240, 20))
        self.cmb_ita_classification.setMaximumSize(QSize(200, 20))
        self.cmb_ita_classification.setStyleSheet(u"")
        self.label_ita_classification = QLabel(self.grb_it_assets)
        self.label_ita_classification.setObjectName(u"label_ita_classification")
        self.label_ita_classification.setGeometry(QRect(217, 90, 100, 20))
        self.label_ita_classification.setMinimumSize(QSize(100, 20))
        self.label_ita_classification.setMaximumSize(QSize(100, 20))
        self.label_ita_fechavreacion = QLabel(self.grb_it_assets)
        self.label_ita_fechavreacion.setObjectName(u"label_ita_fechavreacion")
        self.label_ita_fechavreacion.setGeometry(QRect(10, 310, 130, 20))
        self.label_ita_fechavreacion.setMinimumSize(QSize(130, 20))
        self.label_ita_fechavreacion.setMaximumSize(QSize(130, 20))
        self.dateEdit_ita_creationdate = QDateEdit(self.grb_it_assets)
        self.dateEdit_ita_creationdate.setObjectName(u"dateEdit_ita_creationdate")
        self.dateEdit_ita_creationdate.setGeometry(QRect(143, 310, 100, 20))
        self.dateEdit_ita_creationdate.setMaximumSize(QSize(100, 20))
        self.dateEdit_ita_creationdate.setStyleSheet(u"")
        self.dateEdit_ita_creationdate.setCalendarPopup(True)
        self.textEdit_ita_technical_description = QTextEdit(self.grb_it_assets)
        self.textEdit_ita_technical_description.setObjectName(u"textEdit_ita_technical_description")
        self.textEdit_ita_technical_description.setGeometry(QRect(102, 120, 440, 60))
        self.textEdit_ita_technical_description.setMinimumSize(QSize(440, 60))
        self.textEdit_ita_technical_description.setMaximumSize(QSize(440, 60))
        self.textEdit_ita_technical_description.setStyleSheet(u"")
        self.label_ita_technical_description = QLabel(self.grb_it_assets)
        self.label_ita_technical_description.setObjectName(u"label_ita_technical_description")
        self.label_ita_technical_description.setGeometry(QRect(10, 120, 80, 40))
        self.label_ita_technical_description.setMinimumSize(QSize(80, 40))
        self.label_ita_technical_description.setMaximumSize(QSize(80, 40))
        self.label_ita_technical_description.setScaledContents(False)
        self.label_ita_role = QLabel(self.grb_it_assets)
        self.label_ita_role.setObjectName(u"label_ita_role")
        self.label_ita_role.setGeometry(QRect(390, 190, 25, 20))
        self.label_ita_role.setMinimumSize(QSize(25, 20))
        self.label_ita_role.setMaximumSize(QSize(25, 20))
        self.lineEdit_ita_role = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_role.setObjectName(u"lineEdit_ita_role")
        self.lineEdit_ita_role.setGeometry(QRect(420, 190, 160, 20))
        self.lineEdit_ita_role.setMinimumSize(QSize(160, 20))
        self.lineEdit_ita_role.setMaximumSize(QSize(160, 20))
        self.label_ita_functional_units = QLabel(self.grb_it_assets)
        self.label_ita_functional_units.setObjectName(u"label_ita_functional_units")
        self.label_ita_functional_units.setGeometry(QRect(10, 190, 110, 20))
        self.label_ita_functional_units.setMinimumSize(QSize(110, 0))
        self.label_ita_functional_units.setMaximumSize(QSize(110, 20))
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
        self.lineEdit_ita_ipadrees.setGeometry(QRect(439, 220, 140, 20))
        self.lineEdit_ita_ipadrees.setMinimumSize(QSize(140, 20))
        self.lineEdit_ita_ipadrees.setMaximumSize(QSize(140, 20))
        self.label_ita_ipadrees = QLabel(self.grb_it_assets)
        self.label_ita_ipadrees.setObjectName(u"label_ita_ipadrees")
        self.label_ita_ipadrees.setGeometry(QRect(360, 220, 75, 20))
        self.label_ita_ipadrees.setMinimumSize(QSize(75, 20))
        self.label_ita_ipadrees.setMaximumSize(QSize(75, 20))
        self.lineEdit_ita_idRDP2 = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_idRDP2.setObjectName(u"lineEdit_ita_idRDP2")
        self.lineEdit_ita_idRDP2.setGeometry(QRect(439, 250, 140, 20))
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
        self.label_ita_idRDP2.setGeometry(QRect(376, 250, 60, 20))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(60)
        sizePolicy5.setVerticalStretch(20)
        sizePolicy5.setHeightForWidth(self.label_ita_idRDP2.sizePolicy().hasHeightForWidth())
        self.label_ita_idRDP2.setSizePolicy(sizePolicy5)
        self.label_ita_idRDP2.setMinimumSize(QSize(60, 20))
        self.label_ita_idRDP2.setMaximumSize(QSize(100, 20))
        self.label_ita_id_employees = QLabel(self.grb_it_assets)
        self.label_ita_id_employees.setObjectName(u"label_ita_id_employees")
        self.label_ita_id_employees.setGeometry(QRect(10, 280, 120, 20))
        self.label_ita_id_employees.setMinimumSize(QSize(120, 0))
        self.label_ita_id_employees.setMaximumSize(QSize(120, 20))
        self.lineEdit_ita_iprdp = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_iprdp.setObjectName(u"lineEdit_ita_iprdp")
        self.lineEdit_ita_iprdp.setGeometry(QRect(438, 280, 140, 20))
        self.lineEdit_ita_iprdp.setMinimumSize(QSize(140, 20))
        self.lineEdit_ita_iprdp.setMaximumSize(QSize(140, 20))
        self.label_ita_iprdp = QLabel(self.grb_it_assets)
        self.label_ita_iprdp.setObjectName(u"label_ita_iprdp")
        self.label_ita_iprdp.setGeometry(QRect(390, 280, 45, 20))
        self.label_ita_iprdp.setMinimumSize(QSize(45, 20))
        self.label_ita_iprdp.setMaximumSize(QSize(45, 20))
        self.textEdit_ita_technical_notes = QTextEdit(self.grb_it_assets)
        self.textEdit_ita_technical_notes.setObjectName(u"textEdit_ita_technical_notes")
        self.textEdit_ita_technical_notes.setGeometry(QRect(102, 350, 440, 60))
        self.textEdit_ita_technical_notes.setMinimumSize(QSize(440, 60))
        self.textEdit_ita_technical_notes.setMaximumSize(QSize(440, 60))
        self.textEdit_ita_technical_notes.setStyleSheet(u"")
        self.label_ita_technical_notes = QLabel(self.grb_it_assets)
        self.label_ita_technical_notes.setObjectName(u"label_ita_technical_notes")
        self.label_ita_technical_notes.setGeometry(QRect(10, 350, 80, 40))
        self.label_ita_technical_notes.setMinimumSize(QSize(80, 40))
        self.label_ita_technical_notes.setMaximumSize(QSize(80, 40))
        self.label_ita_technical_notes.setScaledContents(False)
        self.lineEdit_ita_id_functional_units = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_id_functional_units.setObjectName(u"lineEdit_ita_id_functional_units")
        self.lineEdit_ita_id_functional_units.setGeometry(QRect(122, 190, 200, 20))
        self.lineEdit_ita_id_functional_units.setMinimumSize(QSize(200, 20))
        self.lineEdit_ita_id_functional_units.setMaximumSize(QSize(200, 20))
        self.lineEdit_ita_id_functional_units.setReadOnly(True)
        self.btn_buscar_ita_functional_units = QPushButton(self.grb_it_assets)
        self.btn_buscar_ita_functional_units.setObjectName(u"btn_buscar_ita_functional_units")
        self.btn_buscar_ita_functional_units.setGeometry(QRect(335, 187, 24, 24))
        sizePolicy4.setHeightForWidth(self.btn_buscar_ita_functional_units.sizePolicy().hasHeightForWidth())
        self.btn_buscar_ita_functional_units.setSizePolicy(sizePolicy4)
        self.btn_buscar_ita_functional_units.setMinimumSize(QSize(24, 24))
        self.btn_buscar_ita_functional_units.setMaximumSize(QSize(24, 24))
        self.btn_buscar_ita_functional_units.setFont(font6)
        self.btn_buscar_ita_functional_units.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_buscar_ita_functional_units.setIcon(icon51)
        self.btn_buscar_ita_functional_units.setIconSize(QSize(18, 18))
        self.lineEdit_ita_id_employees = QLineEdit(self.grb_it_assets)
        self.lineEdit_ita_id_employees.setObjectName(u"lineEdit_ita_id_employees")
        self.lineEdit_ita_id_employees.setGeometry(QRect(130, 280, 200, 20))
        self.lineEdit_ita_id_employees.setMinimumSize(QSize(200, 20))
        self.lineEdit_ita_id_employees.setMaximumSize(QSize(200, 20))
        self.lineEdit_ita_id_employees.setReadOnly(True)
        self.btn_search_ita_id_employees = QPushButton(self.grb_it_assets)
        self.btn_search_ita_id_employees.setObjectName(u"btn_search_ita_id_employees")
        self.btn_search_ita_id_employees.setGeometry(QRect(335, 278, 24, 24))
        sizePolicy4.setHeightForWidth(self.btn_search_ita_id_employees.sizePolicy().hasHeightForWidth())
        self.btn_search_ita_id_employees.setSizePolicy(sizePolicy4)
        self.btn_search_ita_id_employees.setMinimumSize(QSize(24, 24))
        self.btn_search_ita_id_employees.setMaximumSize(QSize(24, 24))
        self.btn_search_ita_id_employees.setFont(font6)
        self.btn_search_ita_id_employees.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_search_ita_id_employees.setIcon(icon51)
        self.btn_search_ita_id_employees.setIconSize(QSize(18, 18))

        self.vly_it_assets.addWidget(self.grb_it_assets)


        self.verticalLayout_5.addWidget(self.frm_it_assets)

        self.frm_bar_it_assets = QFrame(self.frm_form_it_assets)
        self.frm_bar_it_assets.setObjectName(u"frm_bar_it_assets")
        sizePolicy.setHeightForWidth(self.frm_bar_it_assets.sizePolicy().hasHeightForWidth())
        self.frm_bar_it_assets.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.btn_add_it_assets.sizePolicy().hasHeightForWidth())
        self.btn_add_it_assets.setSizePolicy(sizePolicy)
        self.btn_add_it_assets.setMinimumSize(QSize(118, 48))
        self.btn_add_it_assets.setMaximumSize(QSize(118, 48))
        self.btn_add_it_assets.setFont(font5)
        self.btn_add_it_assets.setStyleSheet(u"")
        self.btn_add_it_assets.setIcon(icon46)
        self.btn_add_it_assets.setIconSize(QSize(22, 22))

        self.hly_frm_bar_it_assets.addWidget(self.btn_add_it_assets)

        self.btn_save_it_assets = QPushButton(self.frm_bar_it_assets)
        self.btn_save_it_assets.setObjectName(u"btn_save_it_assets")
        self.btn_save_it_assets.setMinimumSize(QSize(118, 48))
        self.btn_save_it_assets.setMaximumSize(QSize(118, 48))
        self.btn_save_it_assets.setFont(font5)
        self.btn_save_it_assets.setStyleSheet(u"")
        self.btn_save_it_assets.setIcon(icon47)
        self.btn_save_it_assets.setIconSize(QSize(22, 22))

        self.hly_frm_bar_it_assets.addWidget(self.btn_save_it_assets)

        self.btn_edit_it_assets = QPushButton(self.frm_bar_it_assets)
        self.btn_edit_it_assets.setObjectName(u"btn_edit_it_assets")
        sizePolicy.setHeightForWidth(self.btn_edit_it_assets.sizePolicy().hasHeightForWidth())
        self.btn_edit_it_assets.setSizePolicy(sizePolicy)
        self.btn_edit_it_assets.setMinimumSize(QSize(118, 48))
        self.btn_edit_it_assets.setMaximumSize(QSize(118, 48))
        self.btn_edit_it_assets.setFont(font5)
        self.btn_edit_it_assets.setStyleSheet(u"")
        self.btn_edit_it_assets.setIcon(icon48)
        self.btn_edit_it_assets.setIconSize(QSize(22, 22))

        self.hly_frm_bar_it_assets.addWidget(self.btn_edit_it_assets)

        self.btn_cancel_it_assets = QPushButton(self.frm_bar_it_assets)
        self.btn_cancel_it_assets.setObjectName(u"btn_cancel_it_assets")
        self.btn_cancel_it_assets.setMinimumSize(QSize(118, 48))
        self.btn_cancel_it_assets.setMaximumSize(QSize(118, 48))
        self.btn_cancel_it_assets.setFont(font5)
        self.btn_cancel_it_assets.setStyleSheet(u"")
        self.btn_cancel_it_assets.setIcon(icon49)
        self.btn_cancel_it_assets.setIconSize(QSize(22, 22))

        self.hly_frm_bar_it_assets.addWidget(self.btn_cancel_it_assets)

        self.btn_delete_it_assets = QPushButton(self.frm_bar_it_assets)
        self.btn_delete_it_assets.setObjectName(u"btn_delete_it_assets")
        sizePolicy.setHeightForWidth(self.btn_delete_it_assets.sizePolicy().hasHeightForWidth())
        self.btn_delete_it_assets.setSizePolicy(sizePolicy)
        self.btn_delete_it_assets.setMinimumSize(QSize(118, 48))
        self.btn_delete_it_assets.setMaximumSize(QSize(118, 48))
        self.btn_delete_it_assets.setStyleSheet(u"")
        self.btn_delete_it_assets.setIcon(icon50)
        self.btn_delete_it_assets.setIconSize(QSize(22, 22))

        self.hly_frm_bar_it_assets.addWidget(self.btn_delete_it_assets)


        self.verticalLayout_5.addWidget(self.frm_bar_it_assets)

        self.verticalLayout_5.setStretch(0, 4)
        self.verticalLayout_5.setStretch(1, 1)

        self.hly_page_frm_it_assets.addWidget(self.frm_form_it_assets)

        self.qsw_forms.addWidget(self.page_frm_it_assets)
        self.page_frm_users = QWidget()
        self.page_frm_users.setObjectName(u"page_frm_users")
        sizePolicy1.setHeightForWidth(self.page_frm_users.sizePolicy().hasHeightForWidth())
        self.page_frm_users.setSizePolicy(sizePolicy1)
        self.page_frm_users.setMinimumSize(QSize(825, 544))
        self.page_frm_users.setMaximumSize(QSize(1920, 1080))
        self.page_frm_users.setStyleSheet(u"")
        self.hly_page_frm_users = QHBoxLayout(self.page_frm_users)
        self.hly_page_frm_users.setSpacing(0)
        self.hly_page_frm_users.setObjectName(u"hly_page_frm_users")
        self.hly_page_frm_users.setContentsMargins(0, 0, 0, 0)
        self.frm_form_users = QFrame(self.page_frm_users)
        self.frm_form_users.setObjectName(u"frm_form_users")
        sizePolicy1.setHeightForWidth(self.frm_form_users.sizePolicy().hasHeightForWidth())
        self.frm_form_users.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.frm_users.sizePolicy().hasHeightForWidth())
        self.frm_users.setSizePolicy(sizePolicy1)
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
"    \n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";  \n"
"    padding: 0px 5px;       \n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* C"
                        "olor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\"; \n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255); /* Color de realce de tu tema */\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
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
"    background-color: rgb(255"
                        ", 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco para el cuerpo */\n"
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
"    c"
                        "olor: #808080 !important;\n"
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
        self.label_usr_code = QLabel(self.grb_users)
        self.label_usr_code.setObjectName(u"label_usr_code")
        self.label_usr_code.setGeometry(QRect(10, 30, 61, 20))
        self.label_usr_code.setMaximumSize(QSize(100, 20))
        self.label_usr_code.setAutoFillBackground(False)
        self.lineEdit_usr_code = QLineEdit(self.grb_users)
        self.lineEdit_usr_code.setObjectName(u"lineEdit_usr_code")
        self.lineEdit_usr_code.setGeometry(QRect(80, 30, 100, 20))
        self.lineEdit_usr_code.setMaximumSize(QSize(100, 20))
        self.label_usr_description = QLabel(self.grb_users)
        self.label_usr_description.setObjectName(u"label_usr_description")
        self.label_usr_description.setGeometry(QRect(10, 60, 90, 20))
        self.label_usr_description.setMaximumSize(QSize(90, 20))
        self.lineEdit_usr_description = QLineEdit(self.grb_users)
        self.lineEdit_usr_description.setObjectName(u"lineEdit_usr_description")
        self.lineEdit_usr_description.setGeometry(QRect(99, 60, 400, 20))
        self.lineEdit_usr_description.setMinimumSize(QSize(400, 20))
        self.lineEdit_usr_description.setMaximumSize(QSize(400, 20))
        self.lineEdit_usr_description.setStyleSheet(u"")
        self.label_usr_phone = QLabel(self.grb_users)
        self.label_usr_phone.setObjectName(u"label_usr_phone")
        self.label_usr_phone.setGeometry(QRect(10, 90, 70, 20))
        self.label_usr_phone.setMinimumSize(QSize(70, 20))
        self.label_usr_phone.setMaximumSize(QSize(70, 20))
        self.label_usr_status = QLabel(self.grb_users)
        self.label_usr_status.setObjectName(u"label_usr_status")
        self.label_usr_status.setGeometry(QRect(445, 30, 61, 20))
        self.label_usr_status.setMaximumSize(QSize(100, 20))
        self.lineEdit_usr_phone = QLineEdit(self.grb_users)
        self.lineEdit_usr_phone.setObjectName(u"lineEdit_usr_phone")
        self.lineEdit_usr_phone.setGeometry(QRect(80, 90, 100, 20))
        self.lineEdit_usr_phone.setMaximumSize(QSize(100, 20))
        self.cmb_usr_status = QComboBox(self.grb_users)
        self.cmb_usr_status.addItem("")
        self.cmb_usr_status.addItem("")
        self.cmb_usr_status.setObjectName(u"cmb_usr_status")
        self.cmb_usr_status.setGeometry(QRect(512, 30, 80, 20))
        sizePolicy1.setHeightForWidth(self.cmb_usr_status.sizePolicy().hasHeightForWidth())
        self.cmb_usr_status.setSizePolicy(sizePolicy1)
        self.cmb_usr_status.setMinimumSize(QSize(80, 20))
        self.cmb_usr_status.setMaximumSize(QSize(80, 20))
        self.cmb_usr_status.setStyleSheet(u"")
        self.label_usr_job_titles = QLabel(self.grb_users)
        self.label_usr_job_titles.setObjectName(u"label_usr_job_titles")
        self.label_usr_job_titles.setGeometry(QRect(9, 120, 40, 20))
        self.label_usr_job_titles.setMinimumSize(QSize(40, 20))
        self.label_usr_job_titles.setMaximumSize(QSize(40, 20))
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
        self.label_usr_role = QLabel(self.grb_users)
        self.label_usr_role.setObjectName(u"label_usr_role")
        self.label_usr_role.setGeometry(QRect(10, 150, 25, 20))
        self.label_usr_role.setMinimumSize(QSize(25, 20))
        self.label_usr_role.setMaximumSize(QSize(25, 20))
        self.lineEdit_usr_role = QLineEdit(self.grb_users)
        self.lineEdit_usr_role.setObjectName(u"lineEdit_usr_role")
        self.lineEdit_usr_role.setGeometry(QRect(60, 150, 400, 20))
        self.lineEdit_usr_role.setMaximumSize(QSize(400, 20))
        self.label_usr_email = QLabel(self.grb_users)
        self.label_usr_email.setObjectName(u"label_usr_email")
        self.label_usr_email.setGeometry(QRect(244, 90, 50, 20))
        self.label_usr_email.setMinimumSize(QSize(50, 20))
        self.label_usr_email.setMaximumSize(QSize(50, 20))
        self.lineEdit_usr_email = QLineEdit(self.grb_users)
        self.lineEdit_usr_email.setObjectName(u"lineEdit_usr_email")
        self.lineEdit_usr_email.setGeometry(QRect(297, 90, 200, 20))
        self.lineEdit_usr_email.setMaximumSize(QSize(200, 20))
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
        self.lineEdit_usr_id_job_titles = QLineEdit(self.grb_users)
        self.lineEdit_usr_id_job_titles.setObjectName(u"lineEdit_usr_id_job_titles")
        self.lineEdit_usr_id_job_titles.setGeometry(QRect(60, 120, 400, 20))
        self.lineEdit_usr_id_job_titles.setMinimumSize(QSize(400, 20))
        self.lineEdit_usr_id_job_titles.setMaximumSize(QSize(400, 20))
        self.lineEdit_usr_id_job_titles.setStyleSheet(u"")
        self.lineEdit_usr_id_job_titles.setReadOnly(True)
        self.btn_search_usr_job_titles = QPushButton(self.grb_users)
        self.btn_search_usr_job_titles.setObjectName(u"btn_search_usr_job_titles")
        self.btn_search_usr_job_titles.setGeometry(QRect(465, 120, 24, 24))
        sizePolicy4.setHeightForWidth(self.btn_search_usr_job_titles.sizePolicy().hasHeightForWidth())
        self.btn_search_usr_job_titles.setSizePolicy(sizePolicy4)
        self.btn_search_usr_job_titles.setMinimumSize(QSize(24, 24))
        self.btn_search_usr_job_titles.setMaximumSize(QSize(24, 24))
        self.btn_search_usr_job_titles.setFont(font6)
        self.btn_search_usr_job_titles.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_search_usr_job_titles.setIcon(icon51)
        self.btn_search_usr_job_titles.setIconSize(QSize(18, 18))

        self.vly_users.addWidget(self.grb_users)


        self.vly_frm_form_users.addWidget(self.frm_users)

        self.frm_bar_users = QFrame(self.frm_form_users)
        self.frm_bar_users.setObjectName(u"frm_bar_users")
        sizePolicy.setHeightForWidth(self.frm_bar_users.sizePolicy().hasHeightForWidth())
        self.frm_bar_users.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.btn_add_users.sizePolicy().hasHeightForWidth())
        self.btn_add_users.setSizePolicy(sizePolicy)
        self.btn_add_users.setMinimumSize(QSize(118, 48))
        self.btn_add_users.setMaximumSize(QSize(118, 48))
        self.btn_add_users.setFont(font5)
        self.btn_add_users.setStyleSheet(u"")
        self.btn_add_users.setIcon(icon46)
        self.btn_add_users.setIconSize(QSize(22, 22))

        self.hly_frm_bar_users.addWidget(self.btn_add_users)

        self.btn_save_users = QPushButton(self.frm_bar_users)
        self.btn_save_users.setObjectName(u"btn_save_users")
        self.btn_save_users.setMinimumSize(QSize(118, 48))
        self.btn_save_users.setMaximumSize(QSize(118, 48))
        self.btn_save_users.setFont(font5)
        self.btn_save_users.setStyleSheet(u"")
        self.btn_save_users.setIcon(icon47)
        self.btn_save_users.setIconSize(QSize(22, 22))

        self.hly_frm_bar_users.addWidget(self.btn_save_users)

        self.btn_edit_users = QPushButton(self.frm_bar_users)
        self.btn_edit_users.setObjectName(u"btn_edit_users")
        sizePolicy.setHeightForWidth(self.btn_edit_users.sizePolicy().hasHeightForWidth())
        self.btn_edit_users.setSizePolicy(sizePolicy)
        self.btn_edit_users.setMinimumSize(QSize(118, 48))
        self.btn_edit_users.setMaximumSize(QSize(118, 48))
        self.btn_edit_users.setFont(font5)
        self.btn_edit_users.setStyleSheet(u"")
        self.btn_edit_users.setIcon(icon48)
        self.btn_edit_users.setIconSize(QSize(22, 22))

        self.hly_frm_bar_users.addWidget(self.btn_edit_users)

        self.btn_cancel_users = QPushButton(self.frm_bar_users)
        self.btn_cancel_users.setObjectName(u"btn_cancel_users")
        self.btn_cancel_users.setMinimumSize(QSize(118, 48))
        self.btn_cancel_users.setMaximumSize(QSize(118, 48))
        self.btn_cancel_users.setFont(font5)
        self.btn_cancel_users.setStyleSheet(u"")
        self.btn_cancel_users.setIcon(icon49)
        self.btn_cancel_users.setIconSize(QSize(22, 22))

        self.hly_frm_bar_users.addWidget(self.btn_cancel_users)

        self.btn_delete_users = QPushButton(self.frm_bar_users)
        self.btn_delete_users.setObjectName(u"btn_delete_users")
        sizePolicy.setHeightForWidth(self.btn_delete_users.sizePolicy().hasHeightForWidth())
        self.btn_delete_users.setSizePolicy(sizePolicy)
        self.btn_delete_users.setMinimumSize(QSize(118, 48))
        self.btn_delete_users.setMaximumSize(QSize(118, 48))
        self.btn_delete_users.setStyleSheet(u"")
        self.btn_delete_users.setIcon(icon50)
        self.btn_delete_users.setIconSize(QSize(22, 22))

        self.hly_frm_bar_users.addWidget(self.btn_delete_users)


        self.vly_frm_form_users.addWidget(self.frm_bar_users)

        self.vly_frm_form_users.setStretch(0, 4)
        self.vly_frm_form_users.setStretch(1, 1)

        self.hly_page_frm_users.addWidget(self.frm_form_users)

        self.qsw_forms.addWidget(self.page_frm_users)
        self.page_frm_sessions = QWidget()
        self.page_frm_sessions.setObjectName(u"page_frm_sessions")
        sizePolicy1.setHeightForWidth(self.page_frm_sessions.sizePolicy().hasHeightForWidth())
        self.page_frm_sessions.setSizePolicy(sizePolicy1)
        self.page_frm_sessions.setMinimumSize(QSize(825, 544))
        self.page_frm_sessions.setMaximumSize(QSize(1920, 1080))
        self.page_frm_sessions.setStyleSheet(u"")
        self.hly_page_frm_sessions = QHBoxLayout(self.page_frm_sessions)
        self.hly_page_frm_sessions.setSpacing(0)
        self.hly_page_frm_sessions.setObjectName(u"hly_page_frm_sessions")
        self.hly_page_frm_sessions.setContentsMargins(0, 0, 0, 0)
        self.frm_form_sessions = QFrame(self.page_frm_sessions)
        self.frm_form_sessions.setObjectName(u"frm_form_sessions")
        sizePolicy1.setHeightForWidth(self.frm_form_sessions.sizePolicy().hasHeightForWidth())
        self.frm_form_sessions.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.frm_sessions.sizePolicy().hasHeightForWidth())
        self.frm_sessions.setSizePolicy(sizePolicy1)
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
"    \n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";  \n"
"    padding: 0px 5px;       \n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* C"
                        "olor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\"; \n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255); /* Color de realce de tu tema */\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
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
"    background-color: rgb(255"
                        ", 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco para el cuerpo */\n"
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
"    c"
                        "olor: #808080 !important;\n"
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
        self.label_ses_number = QLabel(self.grb_sessions)
        self.label_ses_number.setObjectName(u"label_ses_number")
        self.label_ses_number.setGeometry(QRect(10, 25, 50, 20))
        self.label_ses_number.setMinimumSize(QSize(50, 20))
        self.label_ses_number.setMaximumSize(QSize(50, 20))
        self.label_ses_number.setAutoFillBackground(False)
        self.lineEdit_ses_number = QLineEdit(self.grb_sessions)
        self.lineEdit_ses_number.setObjectName(u"lineEdit_ses_number")
        self.lineEdit_ses_number.setGeometry(QRect(67, 25, 100, 20))
        self.lineEdit_ses_number.setMaximumSize(QSize(100, 20))
        self.label_ses_clt_description = QLabel(self.grb_sessions)
        self.label_ses_clt_description.setObjectName(u"label_ses_clt_description")
        self.label_ses_clt_description.setGeometry(QRect(10, 50, 80, 20))
        self.label_ses_clt_description.setMinimumSize(QSize(80, 0))
        self.label_ses_clt_description.setMaximumSize(QSize(80, 20))
        self.label_ses_clt_fiscal_id = QLabel(self.grb_sessions)
        self.label_ses_clt_fiscal_id.setObjectName(u"label_ses_clt_fiscal_id")
        self.label_ses_clt_fiscal_id.setGeometry(QRect(10, 80, 80, 20))
        self.label_ses_clt_fiscal_id.setMinimumSize(QSize(80, 0))
        self.label_ses_clt_fiscal_id.setMaximumSize(QSize(80, 20))
        self.label_ses_status = QLabel(self.grb_sessions)
        self.label_ses_status.setObjectName(u"label_ses_status")
        self.label_ses_status.setGeometry(QRect(466, 155, 50, 20))
        self.label_ses_status.setMaximumSize(QSize(50, 20))
        self.lineEdit_ses_clt_fiscal_id = QLineEdit(self.grb_sessions)
        self.lineEdit_ses_clt_fiscal_id.setObjectName(u"lineEdit_ses_clt_fiscal_id")
        self.lineEdit_ses_clt_fiscal_id.setGeometry(QRect(95, 80, 100, 20))
        self.lineEdit_ses_clt_fiscal_id.setMaximumSize(QSize(100, 20))
        self.lineEdit_ses_clt_fiscal_id.setReadOnly(True)
        self.cmb_ses_status = QComboBox(self.grb_sessions)
        self.cmb_ses_status.addItem("")
        self.cmb_ses_status.addItem("")
        self.cmb_ses_status.addItem("")
        self.cmb_ses_status.addItem("")
        self.cmb_ses_status.setObjectName(u"cmb_ses_status")
        self.cmb_ses_status.setGeometry(QRect(519, 155, 80, 20))
        sizePolicy1.setHeightForWidth(self.cmb_ses_status.sizePolicy().hasHeightForWidth())
        self.cmb_ses_status.setSizePolicy(sizePolicy1)
        self.cmb_ses_status.setMinimumSize(QSize(80, 20))
        self.cmb_ses_status.setMaximumSize(QSize(80, 20))
        self.cmb_ses_status.setStyleSheet(u"")
        self.label_ses__date_of_issue = QLabel(self.grb_sessions)
        self.label_ses__date_of_issue.setObjectName(u"label_ses__date_of_issue")
        self.label_ses__date_of_issue.setGeometry(QRect(387, 25, 110, 20))
        self.label_ses__date_of_issue.setMinimumSize(QSize(110, 20))
        self.label_ses__date_of_issue.setMaximumSize(QSize(110, 20))
        self.dateEdit_ses_date_of_issue = QDateEdit(self.grb_sessions)
        self.dateEdit_ses_date_of_issue.setObjectName(u"dateEdit_ses_date_of_issue")
        self.dateEdit_ses_date_of_issue.setGeometry(QRect(504, 25, 100, 20))
        self.dateEdit_ses_date_of_issue.setMinimumSize(QSize(100, 20))
        self.dateEdit_ses_date_of_issue.setMaximumSize(QSize(100, 20))
        self.dateEdit_ses_date_of_issue.setStyleSheet(u"")
        self.dateEdit_ses_date_of_issue.setMaximumDateTime(QDateTime(QDate(2501, 1, 28), QTime(23, 59, 59)))
        self.dateEdit_ses_date_of_issue.setMinimumDateTime(QDateTime(QDate(1752, 12, 1), QTime(0, 0, 0)))
        self.dateEdit_ses_date_of_issue.setMinimumDate(QDate(1752, 12, 1))
        self.dateEdit_ses_date_of_issue.setMaximumTime(QTime(23, 59, 59))
        self.dateEdit_ses_date_of_issue.setMinimumTime(QTime(0, 0, 0))
        self.dateEdit_ses_date_of_issue.setCalendarPopup(True)
        self.textEdit_ses_fiscaladdress = QTextEdit(self.grb_sessions)
        self.textEdit_ses_fiscaladdress.setObjectName(u"textEdit_ses_fiscaladdress")
        self.textEdit_ses_fiscaladdress.setGeometry(QRect(95, 105, 400, 45))
        sizePolicy1.setHeightForWidth(self.textEdit_ses_fiscaladdress.sizePolicy().hasHeightForWidth())
        self.textEdit_ses_fiscaladdress.setSizePolicy(sizePolicy1)
        self.textEdit_ses_fiscaladdress.setMinimumSize(QSize(400, 45))
        self.textEdit_ses_fiscaladdress.setMaximumSize(QSize(400, 45))
        self.textEdit_ses_fiscaladdress.setAutoFillBackground(True)
        self.textEdit_ses_fiscaladdress.setStyleSheet(u"")
        self.label_ses_direccionf = QLabel(self.grb_sessions)
        self.label_ses_direccionf.setObjectName(u"label_ses_direccionf")
        self.label_ses_direccionf.setGeometry(QRect(10, 105, 70, 40))
        sizePolicy.setHeightForWidth(self.label_ses_direccionf.sizePolicy().hasHeightForWidth())
        self.label_ses_direccionf.setSizePolicy(sizePolicy)
        self.label_ses_direccionf.setMinimumSize(QSize(70, 40))
        self.label_ses_direccionf.setMaximumSize(QSize(70, 40))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setHintingPreference(QFont.PreferNoHinting)
        self.label_ses_direccionf.setFont(font7)
        self.label_ses_direccionf.setStyleSheet(u"QLabel {\n"
"    line-height: 12px;\n"
"}")
        self.label_ses_direccionf.setScaledContents(False)
        self.label_ses_direccionf.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lineEdit_ses_clt_phone = QLineEdit(self.grb_sessions)
        self.lineEdit_ses_clt_phone.setObjectName(u"lineEdit_ses_clt_phone")
        self.lineEdit_ses_clt_phone.setGeometry(QRect(95, 155, 150, 20))
        self.lineEdit_ses_clt_phone.setMinimumSize(QSize(150, 0))
        self.lineEdit_ses_clt_phone.setMaximumSize(QSize(150, 20))
        self.lineEdit_ses_clt_phone.setAutoFillBackground(False)
        self.label_ses_clt_phone = QLabel(self.grb_sessions)
        self.label_ses_clt_phone.setObjectName(u"label_ses_clt_phone")
        self.label_ses_clt_phone.setGeometry(QRect(10, 155, 60, 20))
        self.label_ses_clt_phone.setMinimumSize(QSize(60, 20))
        self.label_ses_clt_phone.setMaximumSize(QSize(60, 20))
        self.lineEdit_ses_clt_mobile = QLineEdit(self.grb_sessions)
        self.lineEdit_ses_clt_mobile.setObjectName(u"lineEdit_ses_clt_mobile")
        self.lineEdit_ses_clt_mobile.setGeometry(QRect(300, 155, 150, 20))
        self.lineEdit_ses_clt_mobile.setMinimumSize(QSize(150, 20))
        self.lineEdit_ses_clt_mobile.setMaximumSize(QSize(150, 20))
        self.lineEdit_ses_clt_mobile.setAutoFillBackground(False)
        self.label_ses_clt_mobile = QLabel(self.grb_sessions)
        self.label_ses_clt_mobile.setObjectName(u"label_ses_clt_mobile")
        self.label_ses_clt_mobile.setGeometry(QRect(260, 155, 40, 20))
        self.label_ses_clt_mobile.setMinimumSize(QSize(40, 20))
        self.label_ses_clt_mobile.setMaximumSize(QSize(40, 20))
        self.lineEdit_ses_clt_description = QLineEdit(self.grb_sessions)
        self.lineEdit_ses_clt_description.setObjectName(u"lineEdit_ses_clt_description")
        self.lineEdit_ses_clt_description.setGeometry(QRect(95, 50, 400, 20))
        self.lineEdit_ses_clt_description.setMinimumSize(QSize(400, 20))
        self.lineEdit_ses_clt_description.setMaximumSize(QSize(400, 20))
        self.lineEdit_ses_clt_description.setReadOnly(True)
        self.btn_search_ses_client = QPushButton(self.grb_sessions)
        self.btn_search_ses_client.setObjectName(u"btn_search_ses_client")
        self.btn_search_ses_client.setGeometry(QRect(500, 50, 24, 24))
        sizePolicy4.setHeightForWidth(self.btn_search_ses_client.sizePolicy().hasHeightForWidth())
        self.btn_search_ses_client.setSizePolicy(sizePolicy4)
        self.btn_search_ses_client.setMinimumSize(QSize(24, 24))
        self.btn_search_ses_client.setMaximumSize(QSize(24, 24))
        self.btn_search_ses_client.setFont(font6)
        self.btn_search_ses_client.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_search_ses_client.setIcon(icon51)
        self.btn_search_ses_client.setIconSize(QSize(18, 18))
        self.label_ses_clt_code = QLabel(self.grb_sessions)
        self.label_ses_clt_code.setObjectName(u"label_ses_clt_code")
        self.label_ses_clt_code.setGeometry(QRect(440, 80, 50, 20))
        self.label_ses_clt_code.setMinimumSize(QSize(50, 20))
        self.label_ses_clt_code.setMaximumSize(QSize(50, 20))
        self.lineEdit_ses_clt_code = QLineEdit(self.grb_sessions)
        self.lineEdit_ses_clt_code.setObjectName(u"lineEdit_ses_clt_code")
        self.lineEdit_ses_clt_code.setGeometry(QRect(500, 80, 100, 20))
        self.lineEdit_ses_clt_code.setMaximumSize(QSize(100, 20))
        self.lineEdit_ses_clt_code.setReadOnly(True)
        self.lineEdit_ses_clt_employees = QLineEdit(self.grb_sessions)
        self.lineEdit_ses_clt_employees.setObjectName(u"lineEdit_ses_clt_employees")
        self.lineEdit_ses_clt_employees.setGeometry(QRect(95, 180, 400, 20))
        self.lineEdit_ses_clt_employees.setMinimumSize(QSize(400, 20))
        self.lineEdit_ses_clt_employees.setMaximumSize(QSize(400, 20))
        self.lineEdit_ses_clt_employees.setReadOnly(True)
        self.label_ses_employees_id = QLabel(self.grb_sessions)
        self.label_ses_employees_id.setObjectName(u"label_ses_employees_id")
        self.label_ses_employees_id.setGeometry(QRect(10, 180, 50, 20))
        self.label_ses_employees_id.setMinimumSize(QSize(50, 20))
        self.label_ses_employees_id.setMaximumSize(QSize(50, 20))
        self.label_ses_employees_id.setAutoFillBackground(False)
        self.btn_search_ses_employees = QPushButton(self.grb_sessions)
        self.btn_search_ses_employees.setObjectName(u"btn_search_ses_employees")
        self.btn_search_ses_employees.setGeometry(QRect(500, 180, 24, 24))
        sizePolicy4.setHeightForWidth(self.btn_search_ses_employees.sizePolicy().hasHeightForWidth())
        self.btn_search_ses_employees.setSizePolicy(sizePolicy4)
        self.btn_search_ses_employees.setMinimumSize(QSize(24, 24))
        self.btn_search_ses_employees.setMaximumSize(QSize(24, 24))
        self.btn_search_ses_employees.setFont(font6)
        self.btn_search_ses_employees.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_search_ses_employees.setIcon(icon51)
        self.btn_search_ses_employees.setIconSize(QSize(18, 18))

        self.vly_frm_sessions.addWidget(self.grb_sessions)

        self.grb_ark_sessions_details = QGroupBox(self.frm_sessions)
        self.grb_ark_sessions_details.setObjectName(u"grb_ark_sessions_details")
        self.grb_ark_sessions_details.setMinimumSize(QSize(0, 0))
        self.grb_ark_sessions_details.setMaximumSize(QSize(16777215, 16777215))
        self.grb_ark_sessions_details.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)
        self.grb_ark_sessions_details.setFlat(True)
        self.grb_ark_sessions_details.setCheckable(False)
        self.label__ses_end_time = QLabel(self.grb_ark_sessions_details)
        self.label__ses_end_time.setObjectName(u"label__ses_end_time")
        self.label__ses_end_time.setGeometry(QRect(473, 30, 25, 20))
        self.label__ses_end_time.setMinimumSize(QSize(25, 20))
        self.label__ses_end_time.setMaximumSize(QSize(25, 20))
        self.label__ses_start_time = QLabel(self.grb_ark_sessions_details)
        self.label__ses_start_time.setObjectName(u"label__ses_start_time")
        self.label__ses_start_time.setGeometry(QRect(264, 30, 70, 20))
        self.label__ses_start_time.setMinimumSize(QSize(70, 0))
        self.label__ses_start_time.setMaximumSize(QSize(70, 20))
        self.timeEdit_ses_start_time = QTimeEdit(self.grb_ark_sessions_details)
        self.timeEdit_ses_start_time.setObjectName(u"timeEdit_ses_start_time")
        self.timeEdit_ses_start_time.setGeometry(QRect(335, 30, 90, 20))
        self.timeEdit_ses_start_time.setMinimumSize(QSize(90, 20))
        self.timeEdit_ses_start_time.setMaximumSize(QSize(90, 20))
        self.timeEdit_ses_start_time.setStyleSheet(u"")
        self.timeEdit_ses_start_time.setTime(QTime(0, 0, 0))
        self.dateEdit_ses_sessionsdate = QDateEdit(self.grb_ark_sessions_details)
        self.dateEdit_ses_sessionsdate.setObjectName(u"dateEdit_ses_sessionsdate")
        self.dateEdit_ses_sessionsdate.setGeometry(QRect(115, 30, 100, 20))
        self.dateEdit_ses_sessionsdate.setMinimumSize(QSize(100, 20))
        self.dateEdit_ses_sessionsdate.setMaximumSize(QSize(100, 20))
        self.dateEdit_ses_sessionsdate.setStyleSheet(u"")
        self.dateEdit_ses_sessionsdate.setMaximumDateTime(QDateTime(QDate(2501, 1, 30), QTime(23, 59, 59)))
        self.dateEdit_ses_sessionsdate.setMinimumDateTime(QDateTime(QDate(1752, 12, 1), QTime(0, 0, 0)))
        self.dateEdit_ses_sessionsdate.setMinimumDate(QDate(1752, 12, 1))
        self.dateEdit_ses_sessionsdate.setMaximumTime(QTime(23, 59, 59))
        self.dateEdit_ses_sessionsdate.setMinimumTime(QTime(0, 0, 0))
        self.dateEdit_ses_sessionsdate.setCalendarPopup(True)
        self.label_ses_sessionsdate = QLabel(self.grb_ark_sessions_details)
        self.label_ses_sessionsdate.setObjectName(u"label_ses_sessionsdate")
        self.label_ses_sessionsdate.setGeometry(QRect(10, 30, 100, 20))
        self.label_ses_sessionsdate.setMinimumSize(QSize(100, 20))
        self.label_ses_sessionsdate.setMaximumSize(QSize(100, 20))
        self.timeEdit_ses_end_time = QTimeEdit(self.grb_ark_sessions_details)
        self.timeEdit_ses_end_time.setObjectName(u"timeEdit_ses_end_time")
        self.timeEdit_ses_end_time.setGeometry(QRect(504, 30, 90, 20))
        self.timeEdit_ses_end_time.setMinimumSize(QSize(90, 20))
        self.timeEdit_ses_end_time.setMaximumSize(QSize(90, 20))
        self.timeEdit_ses_end_time.setStyleSheet(u"")
        self.textEdit_dts_activity_performed = QTextEdit(self.grb_ark_sessions_details)
        self.textEdit_dts_activity_performed.setObjectName(u"textEdit_dts_activity_performed")
        self.textEdit_dts_activity_performed.setGeometry(QRect(110, 60, 450, 110))
        sizePolicy1.setHeightForWidth(self.textEdit_dts_activity_performed.sizePolicy().hasHeightForWidth())
        self.textEdit_dts_activity_performed.setSizePolicy(sizePolicy1)
        self.textEdit_dts_activity_performed.setMinimumSize(QSize(450, 110))
        self.textEdit_dts_activity_performed.setMaximumSize(QSize(450, 110))
        self.textEdit_dts_activity_performed.setStyleSheet(u"f")
        self.label_dts_activity_performed = QLabel(self.grb_ark_sessions_details)
        self.label_dts_activity_performed.setObjectName(u"label_dts_activity_performed")
        self.label_dts_activity_performed.setGeometry(QRect(10, 60, 70, 40))
        sizePolicy.setHeightForWidth(self.label_dts_activity_performed.sizePolicy().hasHeightForWidth())
        self.label_dts_activity_performed.setSizePolicy(sizePolicy)
        self.label_dts_activity_performed.setMinimumSize(QSize(70, 40))
        self.label_dts_activity_performed.setMaximumSize(QSize(70, 40))
        self.label_dts_activity_performed.setFont(font7)
        self.label_dts_activity_performed.setStyleSheet(u"QLabel {\n"
"    line-height: 12px;\n"
"}")
        self.label_dts_activity_performed.setScaledContents(False)
        self.label_dts_activity_performed.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lineEdit_ses_total_time = QLineEdit(self.grb_ark_sessions_details)
        self.lineEdit_ses_total_time.setObjectName(u"lineEdit_ses_total_time")
        self.lineEdit_ses_total_time.setGeometry(QRect(130, 178, 100, 20))
        self.lineEdit_ses_total_time.setMaximumSize(QSize(100, 20))
        self.label_ses_total_time = QLabel(self.grb_ark_sessions_details)
        self.label_ses_total_time.setObjectName(u"label_ses_total_time")
        self.label_ses_total_time.setGeometry(QRect(10, 178, 115, 20))
        self.label_ses_total_time.setMinimumSize(QSize(115, 0))
        self.label_ses_total_time.setMaximumSize(QSize(110, 20))
        self.label_dts_result = QLabel(self.grb_ark_sessions_details)
        self.label_dts_result.setObjectName(u"label_dts_result")
        self.label_dts_result.setGeometry(QRect(270, 178, 70, 20))
        self.label_dts_result.setMinimumSize(QSize(70, 20))
        self.label_dts_result.setMaximumSize(QSize(70, 20))
        self.lineEdit_dts_result = QLineEdit(self.grb_ark_sessions_details)
        self.lineEdit_dts_result.setObjectName(u"lineEdit_dts_result")
        self.lineEdit_dts_result.setGeometry(QRect(347, 178, 100, 20))
        self.lineEdit_dts_result.setMaximumSize(QSize(100, 20))

        self.vly_frm_sessions.addWidget(self.grb_ark_sessions_details)

        self.vly_frm_sessions.setStretch(0, 1)
        self.vly_frm_sessions.setStretch(1, 1)

        self.vly_frm_form_sessions.addWidget(self.frm_sessions)

        self.frm_bar_sessions = QFrame(self.frm_form_sessions)
        self.frm_bar_sessions.setObjectName(u"frm_bar_sessions")
        sizePolicy.setHeightForWidth(self.frm_bar_sessions.sizePolicy().hasHeightForWidth())
        self.frm_bar_sessions.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.btn_add_sessions.sizePolicy().hasHeightForWidth())
        self.btn_add_sessions.setSizePolicy(sizePolicy)
        self.btn_add_sessions.setMinimumSize(QSize(118, 48))
        self.btn_add_sessions.setMaximumSize(QSize(118, 48))
        self.btn_add_sessions.setFont(font5)
        self.btn_add_sessions.setStyleSheet(u"")
        self.btn_add_sessions.setIcon(icon46)
        self.btn_add_sessions.setIconSize(QSize(22, 22))

        self.hly_frm_bar_sessions.addWidget(self.btn_add_sessions)

        self.btn_save_sessions = QPushButton(self.frm_bar_sessions)
        self.btn_save_sessions.setObjectName(u"btn_save_sessions")
        self.btn_save_sessions.setMinimumSize(QSize(118, 48))
        self.btn_save_sessions.setMaximumSize(QSize(118, 48))
        self.btn_save_sessions.setFont(font5)
        self.btn_save_sessions.setStyleSheet(u"")
        self.btn_save_sessions.setIcon(icon47)
        self.btn_save_sessions.setIconSize(QSize(22, 22))

        self.hly_frm_bar_sessions.addWidget(self.btn_save_sessions)

        self.btn_edit_sessions = QPushButton(self.frm_bar_sessions)
        self.btn_edit_sessions.setObjectName(u"btn_edit_sessions")
        sizePolicy.setHeightForWidth(self.btn_edit_sessions.sizePolicy().hasHeightForWidth())
        self.btn_edit_sessions.setSizePolicy(sizePolicy)
        self.btn_edit_sessions.setMinimumSize(QSize(118, 48))
        self.btn_edit_sessions.setMaximumSize(QSize(118, 48))
        self.btn_edit_sessions.setFont(font5)
        self.btn_edit_sessions.setStyleSheet(u"")
        self.btn_edit_sessions.setIcon(icon48)
        self.btn_edit_sessions.setIconSize(QSize(22, 22))

        self.hly_frm_bar_sessions.addWidget(self.btn_edit_sessions)

        self.btn_cancel_sessions = QPushButton(self.frm_bar_sessions)
        self.btn_cancel_sessions.setObjectName(u"btn_cancel_sessions")
        self.btn_cancel_sessions.setMinimumSize(QSize(118, 48))
        self.btn_cancel_sessions.setMaximumSize(QSize(118, 48))
        self.btn_cancel_sessions.setFont(font5)
        self.btn_cancel_sessions.setStyleSheet(u"")
        self.btn_cancel_sessions.setIcon(icon49)
        self.btn_cancel_sessions.setIconSize(QSize(22, 22))

        self.hly_frm_bar_sessions.addWidget(self.btn_cancel_sessions)

        self.btn_delete_sessions = QPushButton(self.frm_bar_sessions)
        self.btn_delete_sessions.setObjectName(u"btn_delete_sessions")
        sizePolicy.setHeightForWidth(self.btn_delete_sessions.sizePolicy().hasHeightForWidth())
        self.btn_delete_sessions.setSizePolicy(sizePolicy)
        self.btn_delete_sessions.setMinimumSize(QSize(118, 48))
        self.btn_delete_sessions.setMaximumSize(QSize(118, 48))
        self.btn_delete_sessions.setStyleSheet(u"")
        self.btn_delete_sessions.setIcon(icon50)
        self.btn_delete_sessions.setIconSize(QSize(22, 22))

        self.hly_frm_bar_sessions.addWidget(self.btn_delete_sessions)


        self.vly_frm_form_sessions.addWidget(self.frm_bar_sessions)

        self.vly_frm_form_sessions.setStretch(0, 4)
        self.vly_frm_form_sessions.setStretch(1, 1)

        self.hly_page_frm_sessions.addWidget(self.frm_form_sessions)

        self.qsw_forms.addWidget(self.page_frm_sessions)
        self.page_frm_requests = QWidget()
        self.page_frm_requests.setObjectName(u"page_frm_requests")
        sizePolicy1.setHeightForWidth(self.page_frm_requests.sizePolicy().hasHeightForWidth())
        self.page_frm_requests.setSizePolicy(sizePolicy1)
        self.page_frm_requests.setMinimumSize(QSize(825, 544))
        self.page_frm_requests.setMaximumSize(QSize(1920, 1080))
        self.page_frm_requests.setStyleSheet(u"")
        self.hly_page_frm_requests = QHBoxLayout(self.page_frm_requests)
        self.hly_page_frm_requests.setSpacing(0)
        self.hly_page_frm_requests.setObjectName(u"hly_page_frm_requests")
        self.hly_page_frm_requests.setContentsMargins(0, 0, 0, 0)
        self.frm_form_requests = QFrame(self.page_frm_requests)
        self.frm_form_requests.setObjectName(u"frm_form_requests")
        sizePolicy1.setHeightForWidth(self.frm_form_requests.sizePolicy().hasHeightForWidth())
        self.frm_form_requests.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.frm_requests.sizePolicy().hasHeightForWidth())
        self.frm_requests.setSizePolicy(sizePolicy1)
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
"    \n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";  \n"
"    padding: 0px 5px;       \n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* C"
                        "olor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\"; \n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255); /* Color de realce de tu tema */\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
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
"    background-color: rgb(255"
                        ", 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco para el cuerpo */\n"
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
"    c"
                        "olor: #808080 !important;\n"
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
        self.label_req_code = QLabel(self.grb_requests)
        self.label_req_code.setObjectName(u"label_req_code")
        self.label_req_code.setGeometry(QRect(10, 30, 50, 20))
        self.label_req_code.setMaximumSize(QSize(80, 20))
        self.label_req_code.setAutoFillBackground(False)
        self.lineEdit_req_code = QLineEdit(self.grb_requests)
        self.lineEdit_req_code.setObjectName(u"lineEdit_req_code")
        self.lineEdit_req_code.setGeometry(QRect(66, 30, 100, 20))
        self.lineEdit_req_code.setMaximumSize(QSize(100, 20))
        self.label_req_description = QLabel(self.grb_requests)
        self.label_req_description.setObjectName(u"label_req_description")
        self.label_req_description.setGeometry(QRect(10, 60, 90, 20))
        self.label_req_description.setMinimumSize(QSize(90, 20))
        self.label_req_description.setMaximumSize(QSize(90, 20))
        self.lineEdit_req_description = QLineEdit(self.grb_requests)
        self.lineEdit_req_description.setObjectName(u"lineEdit_req_description")
        self.lineEdit_req_description.setGeometry(QRect(101, 60, 400, 20))
        self.lineEdit_req_description.setMinimumSize(QSize(400, 20))
        self.lineEdit_req_description.setMaximumSize(QSize(400, 20))
        self.lineEdit_req_description.setStyleSheet(u"")
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
        sizePolicy1.setHeightForWidth(self.cmb_req_status.sizePolicy().hasHeightForWidth())
        self.cmb_req_status.setSizePolicy(sizePolicy1)
        self.cmb_req_status.setMinimumSize(QSize(80, 20))
        self.cmb_req_status.setMaximumSize(QSize(80, 20))
        self.cmb_req_status.setStyleSheet(u"")
        self.label_req_creationdate = QLabel(self.grb_requests)
        self.label_req_creationdate.setObjectName(u"label_req_creationdate")
        self.label_req_creationdate.setGeometry(QRect(10, 180, 130, 20))
        self.label_req_creationdate.setMinimumSize(QSize(130, 20))
        self.label_req_creationdate.setMaximumSize(QSize(130, 20))
        self.dateEdit_req_creationdate = QDateEdit(self.grb_requests)
        self.dateEdit_req_creationdate.setObjectName(u"dateEdit_req_creationdate")
        self.dateEdit_req_creationdate.setGeometry(QRect(140, 180, 100, 20))
        self.dateEdit_req_creationdate.setMaximumSize(QSize(100, 20))
        self.dateEdit_req_creationdate.setStyleSheet(u"")
        self.dateEdit_req_creationdate.setCalendarPopup(True)
        self.textEdit_req_descriptiontec = QTextEdit(self.grb_requests)
        self.textEdit_req_descriptiontec.setObjectName(u"textEdit_req_descriptiontec")
        self.textEdit_req_descriptiontec.setGeometry(QRect(101, 85, 400, 60))
        self.textEdit_req_descriptiontec.setMinimumSize(QSize(400, 60))
        self.textEdit_req_descriptiontec.setMaximumSize(QSize(400, 60))
        self.textEdit_req_descriptiontec.setStyleSheet(u"")
        self.label_req_descriptiontec = QLabel(self.grb_requests)
        self.label_req_descriptiontec.setObjectName(u"label_req_descriptiontec")
        self.label_req_descriptiontec.setGeometry(QRect(10, 90, 80, 41))
        self.label_req_descriptiontec.setMinimumSize(QSize(80, 0))
        self.label_req_descriptiontec.setMaximumSize(QSize(100, 60))
        self.label_req_descriptiontec.setScaledContents(False)
        self.label_req_client_id = QLabel(self.grb_requests)
        self.label_req_client_id.setObjectName(u"label_req_client_id")
        self.label_req_client_id.setGeometry(QRect(10, 150, 80, 20))
        self.label_req_client_id.setMinimumSize(QSize(80, 20))
        self.label_req_client_id.setMaximumSize(QSize(80, 20))
        self.label_req_client_id.setAutoFillBackground(False)
        self.lineEdit_req_client_id = QLineEdit(self.grb_requests)
        self.lineEdit_req_client_id.setObjectName(u"lineEdit_req_client_id")
        self.lineEdit_req_client_id.setGeometry(QRect(100, 150, 400, 20))
        self.lineEdit_req_client_id.setMinimumSize(QSize(400, 20))
        self.lineEdit_req_client_id.setMaximumSize(QSize(400, 20))
        self.lineEdit_req_client_id.setStyleSheet(u"")
        self.lineEdit_req_client_id.setReadOnly(True)
        self.btn_search_req_client = QPushButton(self.grb_requests)
        self.btn_search_req_client.setObjectName(u"btn_search_req_client")
        self.btn_search_req_client.setGeometry(QRect(510, 149, 24, 24))
        sizePolicy4.setHeightForWidth(self.btn_search_req_client.sizePolicy().hasHeightForWidth())
        self.btn_search_req_client.setSizePolicy(sizePolicy4)
        self.btn_search_req_client.setMinimumSize(QSize(24, 24))
        self.btn_search_req_client.setMaximumSize(QSize(24, 24))
        self.btn_search_req_client.setFont(font6)
        self.btn_search_req_client.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_search_req_client.setIcon(icon51)
        self.btn_search_req_client.setIconSize(QSize(18, 18))

        self.vly_requests.addWidget(self.grb_requests)


        self.vly_frm_form_requests.addWidget(self.frm_requests)

        self.frm_bar_requests = QFrame(self.frm_form_requests)
        self.frm_bar_requests.setObjectName(u"frm_bar_requests")
        sizePolicy.setHeightForWidth(self.frm_bar_requests.sizePolicy().hasHeightForWidth())
        self.frm_bar_requests.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.btn_add_requests.sizePolicy().hasHeightForWidth())
        self.btn_add_requests.setSizePolicy(sizePolicy)
        self.btn_add_requests.setMinimumSize(QSize(118, 48))
        self.btn_add_requests.setMaximumSize(QSize(118, 48))
        self.btn_add_requests.setFont(font5)
        self.btn_add_requests.setStyleSheet(u"")
        self.btn_add_requests.setIcon(icon46)
        self.btn_add_requests.setIconSize(QSize(22, 22))

        self.hly_frm_bar_requests.addWidget(self.btn_add_requests)

        self.btn_save_requests = QPushButton(self.frm_bar_requests)
        self.btn_save_requests.setObjectName(u"btn_save_requests")
        self.btn_save_requests.setMinimumSize(QSize(118, 48))
        self.btn_save_requests.setMaximumSize(QSize(118, 48))
        self.btn_save_requests.setFont(font5)
        self.btn_save_requests.setStyleSheet(u"")
        self.btn_save_requests.setIcon(icon47)
        self.btn_save_requests.setIconSize(QSize(22, 22))

        self.hly_frm_bar_requests.addWidget(self.btn_save_requests)

        self.btn_edit_requests = QPushButton(self.frm_bar_requests)
        self.btn_edit_requests.setObjectName(u"btn_edit_requests")
        sizePolicy.setHeightForWidth(self.btn_edit_requests.sizePolicy().hasHeightForWidth())
        self.btn_edit_requests.setSizePolicy(sizePolicy)
        self.btn_edit_requests.setMinimumSize(QSize(118, 48))
        self.btn_edit_requests.setMaximumSize(QSize(118, 48))
        self.btn_edit_requests.setFont(font5)
        self.btn_edit_requests.setStyleSheet(u"")
        self.btn_edit_requests.setIcon(icon48)
        self.btn_edit_requests.setIconSize(QSize(22, 22))

        self.hly_frm_bar_requests.addWidget(self.btn_edit_requests)

        self.btn_cancel_requests = QPushButton(self.frm_bar_requests)
        self.btn_cancel_requests.setObjectName(u"btn_cancel_requests")
        self.btn_cancel_requests.setMinimumSize(QSize(118, 48))
        self.btn_cancel_requests.setMaximumSize(QSize(118, 48))
        self.btn_cancel_requests.setFont(font5)
        self.btn_cancel_requests.setStyleSheet(u"")
        self.btn_cancel_requests.setIcon(icon49)
        self.btn_cancel_requests.setIconSize(QSize(22, 22))

        self.hly_frm_bar_requests.addWidget(self.btn_cancel_requests)

        self.btn_delete_requests = QPushButton(self.frm_bar_requests)
        self.btn_delete_requests.setObjectName(u"btn_delete_requests")
        sizePolicy.setHeightForWidth(self.btn_delete_requests.sizePolicy().hasHeightForWidth())
        self.btn_delete_requests.setSizePolicy(sizePolicy)
        self.btn_delete_requests.setMinimumSize(QSize(118, 48))
        self.btn_delete_requests.setMaximumSize(QSize(118, 48))
        self.btn_delete_requests.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_delete_requests.setStyleSheet(u"")
        self.btn_delete_requests.setIcon(icon50)
        self.btn_delete_requests.setIconSize(QSize(22, 22))

        self.hly_frm_bar_requests.addWidget(self.btn_delete_requests)


        self.vly_frm_form_requests.addWidget(self.frm_bar_requests)

        self.vly_frm_form_requests.setStretch(0, 4)
        self.vly_frm_form_requests.setStretch(1, 1)

        self.hly_page_frm_requests.addWidget(self.frm_form_requests)

        self.qsw_forms.addWidget(self.page_frm_requests)
        self.page_frm_job_titles = QWidget()
        self.page_frm_job_titles.setObjectName(u"page_frm_job_titles")
        sizePolicy1.setHeightForWidth(self.page_frm_job_titles.sizePolicy().hasHeightForWidth())
        self.page_frm_job_titles.setSizePolicy(sizePolicy1)
        self.page_frm_job_titles.setMinimumSize(QSize(825, 544))
        self.page_frm_job_titles.setMaximumSize(QSize(1920, 1080))
        self.page_frm_job_titles.setStyleSheet(u"")
        self.hly_page_frm_job_titles = QHBoxLayout(self.page_frm_job_titles)
        self.hly_page_frm_job_titles.setSpacing(0)
        self.hly_page_frm_job_titles.setObjectName(u"hly_page_frm_job_titles")
        self.hly_page_frm_job_titles.setContentsMargins(0, 0, 0, 0)
        self.frm_form_job_titles = QFrame(self.page_frm_job_titles)
        self.frm_form_job_titles.setObjectName(u"frm_form_job_titles")
        sizePolicy1.setHeightForWidth(self.frm_form_job_titles.sizePolicy().hasHeightForWidth())
        self.frm_form_job_titles.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.frm_job_titles.sizePolicy().hasHeightForWidth())
        self.frm_job_titles.setSizePolicy(sizePolicy1)
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
"    \n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";  \n"
"    padding: 0px 5px;       \n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* C"
                        "olor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\"; \n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255); /* Color de realce de tu tema */\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
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
"    background-color: rgb(255"
                        ", 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco para el cuerpo */\n"
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
"    c"
                        "olor: #808080 !important;\n"
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
        self.label_job_code = QLabel(self.grb_job_titles)
        self.label_job_code.setObjectName(u"label_job_code")
        self.label_job_code.setGeometry(QRect(10, 30, 61, 20))
        self.label_job_code.setMaximumSize(QSize(100, 20))
        self.label_job_code.setAutoFillBackground(False)
        self.lineEdit_job_code = QLineEdit(self.grb_job_titles)
        self.lineEdit_job_code.setObjectName(u"lineEdit_job_code")
        self.lineEdit_job_code.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_job_code.setMaximumSize(QSize(100, 20))
        self.label_job_description = QLabel(self.grb_job_titles)
        self.label_job_description.setObjectName(u"label_job_description")
        self.label_job_description.setGeometry(QRect(10, 60, 90, 20))
        sizePolicy.setHeightForWidth(self.label_job_description.sizePolicy().hasHeightForWidth())
        self.label_job_description.setSizePolicy(sizePolicy)
        self.label_job_description.setMinimumSize(QSize(80, 20))
        self.label_job_description.setMaximumSize(QSize(100, 20))
        self.lineEdit_job_description = QLineEdit(self.grb_job_titles)
        self.lineEdit_job_description.setObjectName(u"lineEdit_job_description")
        self.lineEdit_job_description.setGeometry(QRect(101, 60, 400, 20))
        self.lineEdit_job_description.setMinimumSize(QSize(400, 20))
        self.lineEdit_job_description.setMaximumSize(QSize(400, 20))
        self.lineEdit_job_description.setStyleSheet(u"")
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
        sizePolicy1.setHeightForWidth(self.cmb_job_status.sizePolicy().hasHeightForWidth())
        self.cmb_job_status.setSizePolicy(sizePolicy1)
        self.cmb_job_status.setMinimumSize(QSize(80, 20))
        self.cmb_job_status.setMaximumSize(QSize(80, 20))
        self.cmb_job_status.setStyleSheet(u"")
        self.label_job_creationdate = QLabel(self.grb_job_titles)
        self.label_job_creationdate.setObjectName(u"label_job_creationdate")
        self.label_job_creationdate.setGeometry(QRect(10, 160, 120, 20))
        self.label_job_creationdate.setMinimumSize(QSize(120, 20))
        self.label_job_creationdate.setMaximumSize(QSize(120, 23))
        self.dateEdit_job_creationdate = QDateEdit(self.grb_job_titles)
        self.dateEdit_job_creationdate.setObjectName(u"dateEdit_job_creationdate")
        self.dateEdit_job_creationdate.setGeometry(QRect(133, 160, 100, 20))
        self.dateEdit_job_creationdate.setMaximumSize(QSize(100, 20))
        self.dateEdit_job_creationdate.setStyleSheet(u"")
        self.dateEdit_job_creationdate.setCalendarPopup(True)
        self.textEdit_job_descriptiontec = QTextEdit(self.grb_job_titles)
        self.textEdit_job_descriptiontec.setObjectName(u"textEdit_job_descriptiontec")
        self.textEdit_job_descriptiontec.setGeometry(QRect(101, 90, 400, 60))
        self.textEdit_job_descriptiontec.setMinimumSize(QSize(400, 60))
        self.textEdit_job_descriptiontec.setMaximumSize(QSize(400, 60))
        self.textEdit_job_descriptiontec.setStyleSheet(u"")
        self.label_job_descriptiontec = QLabel(self.grb_job_titles)
        self.label_job_descriptiontec.setObjectName(u"label_job_descriptiontec")
        self.label_job_descriptiontec.setGeometry(QRect(10, 95, 80, 41))
        self.label_job_descriptiontec.setMinimumSize(QSize(80, 0))
        self.label_job_descriptiontec.setMaximumSize(QSize(100, 60))
        self.label_job_descriptiontec.setScaledContents(False)

        self.vly_job_titles.addWidget(self.grb_job_titles)


        self.vly_frm_form_job_titles.addWidget(self.frm_job_titles)

        self.frm_bar_job_titles = QFrame(self.frm_form_job_titles)
        self.frm_bar_job_titles.setObjectName(u"frm_bar_job_titles")
        sizePolicy.setHeightForWidth(self.frm_bar_job_titles.sizePolicy().hasHeightForWidth())
        self.frm_bar_job_titles.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.btn_add_job_titles.sizePolicy().hasHeightForWidth())
        self.btn_add_job_titles.setSizePolicy(sizePolicy)
        self.btn_add_job_titles.setMinimumSize(QSize(118, 48))
        self.btn_add_job_titles.setMaximumSize(QSize(118, 48))
        self.btn_add_job_titles.setFont(font5)
        self.btn_add_job_titles.setStyleSheet(u"")
        self.btn_add_job_titles.setIcon(icon46)
        self.btn_add_job_titles.setIconSize(QSize(22, 22))

        self.hly_frm_bar_job_titles.addWidget(self.btn_add_job_titles)

        self.btn_save_job_titles = QPushButton(self.frm_bar_job_titles)
        self.btn_save_job_titles.setObjectName(u"btn_save_job_titles")
        self.btn_save_job_titles.setMinimumSize(QSize(118, 48))
        self.btn_save_job_titles.setMaximumSize(QSize(118, 48))
        self.btn_save_job_titles.setFont(font5)
        self.btn_save_job_titles.setStyleSheet(u"")
        self.btn_save_job_titles.setIcon(icon47)
        self.btn_save_job_titles.setIconSize(QSize(22, 22))

        self.hly_frm_bar_job_titles.addWidget(self.btn_save_job_titles)

        self.btn_edit_job_titles = QPushButton(self.frm_bar_job_titles)
        self.btn_edit_job_titles.setObjectName(u"btn_edit_job_titles")
        sizePolicy.setHeightForWidth(self.btn_edit_job_titles.sizePolicy().hasHeightForWidth())
        self.btn_edit_job_titles.setSizePolicy(sizePolicy)
        self.btn_edit_job_titles.setMinimumSize(QSize(118, 48))
        self.btn_edit_job_titles.setMaximumSize(QSize(118, 48))
        self.btn_edit_job_titles.setFont(font5)
        self.btn_edit_job_titles.setStyleSheet(u"")
        self.btn_edit_job_titles.setIcon(icon48)
        self.btn_edit_job_titles.setIconSize(QSize(22, 22))

        self.hly_frm_bar_job_titles.addWidget(self.btn_edit_job_titles)

        self.btn_cancel_job_titles = QPushButton(self.frm_bar_job_titles)
        self.btn_cancel_job_titles.setObjectName(u"btn_cancel_job_titles")
        self.btn_cancel_job_titles.setMinimumSize(QSize(118, 48))
        self.btn_cancel_job_titles.setMaximumSize(QSize(118, 48))
        self.btn_cancel_job_titles.setFont(font5)
        self.btn_cancel_job_titles.setStyleSheet(u"")
        self.btn_cancel_job_titles.setIcon(icon49)
        self.btn_cancel_job_titles.setIconSize(QSize(22, 22))

        self.hly_frm_bar_job_titles.addWidget(self.btn_cancel_job_titles)

        self.btn_delete_job_titles = QPushButton(self.frm_bar_job_titles)
        self.btn_delete_job_titles.setObjectName(u"btn_delete_job_titles")
        sizePolicy.setHeightForWidth(self.btn_delete_job_titles.sizePolicy().hasHeightForWidth())
        self.btn_delete_job_titles.setSizePolicy(sizePolicy)
        self.btn_delete_job_titles.setMinimumSize(QSize(118, 48))
        self.btn_delete_job_titles.setMaximumSize(QSize(118, 48))
        self.btn_delete_job_titles.setStyleSheet(u"")
        self.btn_delete_job_titles.setIcon(icon50)
        self.btn_delete_job_titles.setIconSize(QSize(22, 22))

        self.hly_frm_bar_job_titles.addWidget(self.btn_delete_job_titles)


        self.vly_frm_form_job_titles.addWidget(self.frm_bar_job_titles)

        self.vly_frm_form_job_titles.setStretch(0, 4)
        self.vly_frm_form_job_titles.setStretch(1, 1)

        self.hly_page_frm_job_titles.addWidget(self.frm_form_job_titles)

        self.qsw_forms.addWidget(self.page_frm_job_titles)
        self.page_frm_functional_units = QWidget()
        self.page_frm_functional_units.setObjectName(u"page_frm_functional_units")
        sizePolicy1.setHeightForWidth(self.page_frm_functional_units.sizePolicy().hasHeightForWidth())
        self.page_frm_functional_units.setSizePolicy(sizePolicy1)
        self.page_frm_functional_units.setMinimumSize(QSize(825, 544))
        self.page_frm_functional_units.setMaximumSize(QSize(1920, 1080))
        self.page_frm_functional_units.setStyleSheet(u"")
        self.hly_page_frm_functional_units = QHBoxLayout(self.page_frm_functional_units)
        self.hly_page_frm_functional_units.setSpacing(0)
        self.hly_page_frm_functional_units.setObjectName(u"hly_page_frm_functional_units")
        self.hly_page_frm_functional_units.setContentsMargins(0, 0, 0, 0)
        self.frm_form_functional_units = QFrame(self.page_frm_functional_units)
        self.frm_form_functional_units.setObjectName(u"frm_form_functional_units")
        sizePolicy1.setHeightForWidth(self.frm_form_functional_units.sizePolicy().hasHeightForWidth())
        self.frm_form_functional_units.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.frm_functional_units.sizePolicy().hasHeightForWidth())
        self.frm_functional_units.setSizePolicy(sizePolicy1)
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
"    \n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";  \n"
"    padding: 0px 5px;       \n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* C"
                        "olor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\"; \n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255); /* Color de realce de tu tema */\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
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
"    background-color: rgb(255"
                        ", 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco para el cuerpo */\n"
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
"    c"
                        "olor: #808080 !important;\n"
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
        self.label_fun_code = QLabel(self.grb_functional_units)
        self.label_fun_code.setObjectName(u"label_fun_code")
        self.label_fun_code.setGeometry(QRect(10, 30, 61, 20))
        self.label_fun_code.setMaximumSize(QSize(100, 20))
        self.label_fun_code.setAutoFillBackground(False)
        self.lineEdit_fun_code = QLineEdit(self.grb_functional_units)
        self.lineEdit_fun_code.setObjectName(u"lineEdit_fun_code")
        self.lineEdit_fun_code.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_fun_code.setMaximumSize(QSize(100, 20))
        self.label_fun_description = QLabel(self.grb_functional_units)
        self.label_fun_description.setObjectName(u"label_fun_description")
        self.label_fun_description.setGeometry(QRect(10, 70, 101, 20))
        self.label_fun_description.setMaximumSize(QSize(150, 20))
        self.lineEdit_fun_description = QLineEdit(self.grb_functional_units)
        self.lineEdit_fun_description.setObjectName(u"lineEdit_fun_description")
        self.lineEdit_fun_description.setGeometry(QRect(120, 70, 400, 20))
        self.lineEdit_fun_description.setMinimumSize(QSize(400, 20))
        self.lineEdit_fun_description.setMaximumSize(QSize(400, 20))
        self.lineEdit_fun_description.setStyleSheet(u"")
        self.label_fun_status = QLabel(self.grb_functional_units)
        self.label_fun_status.setObjectName(u"label_fun_status")
        self.label_fun_status.setGeometry(QRect(434, 30, 61, 20))
        self.label_fun_status.setMaximumSize(QSize(100, 20))
        self.cmb_fun_status = QComboBox(self.grb_functional_units)
        self.cmb_fun_status.addItem("")
        self.cmb_fun_status.addItem("")
        self.cmb_fun_status.setObjectName(u"cmb_fun_status")
        self.cmb_fun_status.setGeometry(QRect(498, 30, 80, 20))
        sizePolicy1.setHeightForWidth(self.cmb_fun_status.sizePolicy().hasHeightForWidth())
        self.cmb_fun_status.setSizePolicy(sizePolicy1)
        self.cmb_fun_status.setMinimumSize(QSize(80, 20))
        self.cmb_fun_status.setMaximumSize(QSize(80, 20))
        self.cmb_fun_status.setStyleSheet(u"")
        self.label_fun_create_date = QLabel(self.grb_functional_units)
        self.label_fun_create_date.setObjectName(u"label_fun_create_date")
        self.label_fun_create_date.setGeometry(QRect(12, 180, 130, 20))
        self.label_fun_create_date.setMinimumSize(QSize(130, 20))
        self.label_fun_create_date.setMaximumSize(QSize(130, 20))
        self.dateEdit_fun_create_date = QDateEdit(self.grb_functional_units)
        self.dateEdit_fun_create_date.setObjectName(u"dateEdit_fun_create_date")
        self.dateEdit_fun_create_date.setGeometry(QRect(142, 180, 100, 20))
        self.dateEdit_fun_create_date.setMaximumSize(QSize(100, 20))
        self.dateEdit_fun_create_date.setStyleSheet(u"")
        self.dateEdit_fun_create_date.setCalendarPopup(True)
        self.label_fun_descriptiontec = QLabel(self.grb_functional_units)
        self.label_fun_descriptiontec.setObjectName(u"label_fun_descriptiontec")
        self.label_fun_descriptiontec.setGeometry(QRect(10, 100, 100, 41))
        self.label_fun_descriptiontec.setMinimumSize(QSize(100, 0))
        self.label_fun_descriptiontec.setMaximumSize(QSize(100, 60))
        self.label_fun_descriptiontec.setScaledContents(False)
        self.textEdit_fun_descriptiontec = QTextEdit(self.grb_functional_units)
        self.textEdit_fun_descriptiontec.setObjectName(u"textEdit_fun_descriptiontec")
        self.textEdit_fun_descriptiontec.setGeometry(QRect(120, 100, 400, 60))
        self.textEdit_fun_descriptiontec.setMinimumSize(QSize(400, 60))
        self.textEdit_fun_descriptiontec.setMaximumSize(QSize(400, 60))
        self.textEdit_fun_descriptiontec.setStyleSheet(u"")

        self.vly_functional_units.addWidget(self.grb_functional_units)


        self.vly_frm_form_functional_units.addWidget(self.frm_functional_units)

        self.frm_bar_functional_units = QFrame(self.frm_form_functional_units)
        self.frm_bar_functional_units.setObjectName(u"frm_bar_functional_units")
        sizePolicy.setHeightForWidth(self.frm_bar_functional_units.sizePolicy().hasHeightForWidth())
        self.frm_bar_functional_units.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.btn_add_functional_units.sizePolicy().hasHeightForWidth())
        self.btn_add_functional_units.setSizePolicy(sizePolicy)
        self.btn_add_functional_units.setMinimumSize(QSize(118, 48))
        self.btn_add_functional_units.setMaximumSize(QSize(118, 48))
        self.btn_add_functional_units.setFont(font5)
        self.btn_add_functional_units.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_add_functional_units.setStyleSheet(u"")
        self.btn_add_functional_units.setIcon(icon46)
        self.btn_add_functional_units.setIconSize(QSize(22, 22))

        self.hly_frm_bar_functional_units.addWidget(self.btn_add_functional_units)

        self.btn_save_functional_units = QPushButton(self.frm_bar_functional_units)
        self.btn_save_functional_units.setObjectName(u"btn_save_functional_units")
        self.btn_save_functional_units.setMinimumSize(QSize(118, 48))
        self.btn_save_functional_units.setMaximumSize(QSize(118, 48))
        self.btn_save_functional_units.setFont(font5)
        self.btn_save_functional_units.setStyleSheet(u"")
        self.btn_save_functional_units.setIcon(icon47)
        self.btn_save_functional_units.setIconSize(QSize(22, 22))

        self.hly_frm_bar_functional_units.addWidget(self.btn_save_functional_units)

        self.btn_edit_functional_units = QPushButton(self.frm_bar_functional_units)
        self.btn_edit_functional_units.setObjectName(u"btn_edit_functional_units")
        sizePolicy.setHeightForWidth(self.btn_edit_functional_units.sizePolicy().hasHeightForWidth())
        self.btn_edit_functional_units.setSizePolicy(sizePolicy)
        self.btn_edit_functional_units.setMinimumSize(QSize(118, 48))
        self.btn_edit_functional_units.setMaximumSize(QSize(118, 48))
        self.btn_edit_functional_units.setFont(font5)
        self.btn_edit_functional_units.setStyleSheet(u"")
        self.btn_edit_functional_units.setIcon(icon48)
        self.btn_edit_functional_units.setIconSize(QSize(22, 22))

        self.hly_frm_bar_functional_units.addWidget(self.btn_edit_functional_units)

        self.btn_cancel_functional_units = QPushButton(self.frm_bar_functional_units)
        self.btn_cancel_functional_units.setObjectName(u"btn_cancel_functional_units")
        self.btn_cancel_functional_units.setMinimumSize(QSize(118, 48))
        self.btn_cancel_functional_units.setMaximumSize(QSize(118, 48))
        self.btn_cancel_functional_units.setFont(font5)
        self.btn_cancel_functional_units.setStyleSheet(u"")
        self.btn_cancel_functional_units.setIcon(icon49)
        self.btn_cancel_functional_units.setIconSize(QSize(22, 22))

        self.hly_frm_bar_functional_units.addWidget(self.btn_cancel_functional_units)

        self.btn_delete_functional_units = QPushButton(self.frm_bar_functional_units)
        self.btn_delete_functional_units.setObjectName(u"btn_delete_functional_units")
        sizePolicy.setHeightForWidth(self.btn_delete_functional_units.sizePolicy().hasHeightForWidth())
        self.btn_delete_functional_units.setSizePolicy(sizePolicy)
        self.btn_delete_functional_units.setMinimumSize(QSize(118, 48))
        self.btn_delete_functional_units.setMaximumSize(QSize(118, 48))
        self.btn_delete_functional_units.setStyleSheet(u"")
        self.btn_delete_functional_units.setIcon(icon50)
        self.btn_delete_functional_units.setIconSize(QSize(22, 22))

        self.hly_frm_bar_functional_units.addWidget(self.btn_delete_functional_units)


        self.vly_frm_form_functional_units.addWidget(self.frm_bar_functional_units)

        self.vly_frm_form_functional_units.setStretch(0, 4)
        self.vly_frm_form_functional_units.setStretch(1, 1)

        self.hly_page_frm_functional_units.addWidget(self.frm_form_functional_units)

        self.qsw_forms.addWidget(self.page_frm_functional_units)
        self.page_frm_a_company = QWidget()
        self.page_frm_a_company.setObjectName(u"page_frm_a_company")
        sizePolicy1.setHeightForWidth(self.page_frm_a_company.sizePolicy().hasHeightForWidth())
        self.page_frm_a_company.setSizePolicy(sizePolicy1)
        self.page_frm_a_company.setMinimumSize(QSize(825, 544))
        self.page_frm_a_company.setMaximumSize(QSize(1980, 1080))
        self.page_frm_a_company.setStyleSheet(u"")
        self.hly_page_frm_aaa_company = QHBoxLayout(self.page_frm_a_company)
        self.hly_page_frm_aaa_company.setSpacing(0)
        self.hly_page_frm_aaa_company.setObjectName(u"hly_page_frm_aaa_company")
        self.hly_page_frm_aaa_company.setContentsMargins(0, 0, 0, 0)
        self.frm_form_a_company = QFrame(self.page_frm_a_company)
        self.frm_form_a_company.setObjectName(u"frm_form_a_company")
        sizePolicy1.setHeightForWidth(self.frm_form_a_company.sizePolicy().hasHeightForWidth())
        self.frm_form_a_company.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.frm_a_company.sizePolicy().hasHeightForWidth())
        self.frm_a_company.setSizePolicy(sizePolicy1)
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
"    \n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";  \n"
"    padding: 0px 5px;       \n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* C"
                        "olor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\"; \n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255); /* Color de realce de tu tema */\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
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
"    background-color: rgb(255"
                        ", 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco para el cuerpo */\n"
"}\n"
"/* Estilo para el calendario del QDateEdit */\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255);\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"/* Encabezado (Mes y A\u00f1o) */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"/* Botones de navegaci\u00f3n (Flechas) */\n"
"QCalendarWidget QToolButton {\n"
"    background-color: transparent;\n"
"    color: #000000;\n"
"    font: bold "
                        "10pt \"Segoe UI\";\n"
"}\n"
"\n"
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
        self.grb_general_information = QGroupBox(self.frm_a_company)
        self.grb_general_information.setObjectName(u"grb_general_information")
        self.grb_general_information.setMinimumSize(QSize(0, 0))
        self.grb_general_information.setMaximumSize(QSize(16777215, 544))
        self.grb_general_information.setStyleSheet(u"")
        self.label_emp_codigo = QLabel(self.grb_general_information)
        self.label_emp_codigo.setObjectName(u"label_emp_codigo")
        self.label_emp_codigo.setGeometry(QRect(10, 30, 61, 20))
        self.label_emp_codigo.setMaximumSize(QSize(100, 20))
        self.label_emp_codigo.setAutoFillBackground(False)
        self.lineEdit_emp_code = QLineEdit(self.grb_general_information)
        self.lineEdit_emp_code.setObjectName(u"lineEdit_emp_code")
        self.lineEdit_emp_code.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_emp_code.setMaximumSize(QSize(100, 20))
        self.label_emp_description = QLabel(self.grb_general_information)
        self.label_emp_description.setObjectName(u"label_emp_description")
        self.label_emp_description.setGeometry(QRect(10, 60, 101, 20))
        self.label_emp_description.setMaximumSize(QSize(150, 20))
        self.lineEdit_emp_description = QLineEdit(self.grb_general_information)
        self.lineEdit_emp_description.setObjectName(u"lineEdit_emp_description")
        self.lineEdit_emp_description.setGeometry(QRect(120, 60, 400, 20))
        self.lineEdit_emp_description.setMinimumSize(QSize(400, 20))
        self.lineEdit_emp_description.setMaximumSize(QSize(400, 20))
        self.lineEdit_emp_description.setStyleSheet(u"")
        self.label_emp_tax_id = QLabel(self.grb_general_information)
        self.label_emp_tax_id.setObjectName(u"label_emp_tax_id")
        self.label_emp_tax_id.setGeometry(QRect(10, 90, 115, 20))
        self.label_emp_tax_id.setMinimumSize(QSize(115, 0))
        self.label_emp_tax_id.setMaximumSize(QSize(110, 20))
        self.label_emp_status = QLabel(self.grb_general_information)
        self.label_emp_status.setObjectName(u"label_emp_status")
        self.label_emp_status.setGeometry(QRect(457, 30, 50, 20))
        self.label_emp_status.setMinimumSize(QSize(50, 20))
        self.label_emp_status.setMaximumSize(QSize(50, 20))
        self.lineEdit_emp_tax_id = QLineEdit(self.grb_general_information)
        self.lineEdit_emp_tax_id.setObjectName(u"lineEdit_emp_tax_id")
        self.lineEdit_emp_tax_id.setGeometry(QRect(133, 90, 100, 20))
        self.lineEdit_emp_tax_id.setMaximumSize(QSize(100, 20))
        self.cmb_emp_ststus = QComboBox(self.grb_general_information)
        self.cmb_emp_ststus.addItem("")
        self.cmb_emp_ststus.addItem("")
        self.cmb_emp_ststus.setObjectName(u"cmb_emp_ststus")
        self.cmb_emp_ststus.setGeometry(QRect(512, 30, 80, 20))
        sizePolicy1.setHeightForWidth(self.cmb_emp_ststus.sizePolicy().hasHeightForWidth())
        self.cmb_emp_ststus.setSizePolicy(sizePolicy1)
        self.cmb_emp_ststus.setMinimumSize(QSize(80, 20))
        self.cmb_emp_ststus.setMaximumSize(QSize(80, 20))
        self.cmb_emp_ststus.setStyleSheet(u"")
        self.cmb_emp_tipo_taxpayer = QComboBox(self.grb_general_information)
        self.cmb_emp_tipo_taxpayer.addItem("")
        self.cmb_emp_tipo_taxpayer.addItem("")
        self.cmb_emp_tipo_taxpayer.setObjectName(u"cmb_emp_tipo_taxpayer")
        self.cmb_emp_tipo_taxpayer.setGeometry(QRect(512, 90, 100, 20))
        sizePolicy1.setHeightForWidth(self.cmb_emp_tipo_taxpayer.sizePolicy().hasHeightForWidth())
        self.cmb_emp_tipo_taxpayer.setSizePolicy(sizePolicy1)
        self.cmb_emp_tipo_taxpayer.setMaximumSize(QSize(100, 20))
        self.cmb_emp_tipo_taxpayer.setStyleSheet(u"")
        self.label_emp_tipo_taxpayer = QLabel(self.grb_general_information)
        self.label_emp_tipo_taxpayer.setObjectName(u"label_emp_tipo_taxpayer")
        self.label_emp_tipo_taxpayer.setGeometry(QRect(387, 90, 120, 20))
        self.label_emp_tipo_taxpayer.setMinimumSize(QSize(120, 20))
        self.label_emp_tipo_taxpayer.setMaximumSize(QSize(120, 20))

        self.vly_frm_a_company.addWidget(self.grb_general_information)

        self.grb_phone_address = QGroupBox(self.frm_a_company)
        self.grb_phone_address.setObjectName(u"grb_phone_address")
        self.grb_phone_address.setMinimumSize(QSize(0, 0))
        self.grb_phone_address.setStyleSheet(u"")
        self.textEdit_emp_tax_address = QTextEdit(self.grb_phone_address)
        self.textEdit_emp_tax_address.setObjectName(u"textEdit_emp_tax_address")
        self.textEdit_emp_tax_address.setGeometry(QRect(87, 22, 200, 60))
        self.textEdit_emp_tax_address.setMinimumSize(QSize(200, 60))
        self.textEdit_emp_tax_address.setMaximumSize(QSize(200, 60))
        self.textEdit_emp_tax_address.setStyleSheet(u"")
        self.label_emp_tax_address = QLabel(self.grb_phone_address)
        self.label_emp_tax_address.setObjectName(u"label_emp_tax_address")
        self.label_emp_tax_address.setGeometry(QRect(10, 22, 71, 41))
        self.label_emp_tax_address.setScaledContents(False)
        self.label_emp_local_address = QLabel(self.grb_phone_address)
        self.label_emp_local_address.setObjectName(u"label_emp_local_address")
        self.label_emp_local_address.setGeometry(QRect(310, 22, 71, 41))
        self.textEdit_emp_local_address = QTextEdit(self.grb_phone_address)
        self.textEdit_emp_local_address.setObjectName(u"textEdit_emp_local_address")
        self.textEdit_emp_local_address.setGeometry(QRect(386, 22, 200, 60))
        self.textEdit_emp_local_address.setMinimumSize(QSize(200, 60))
        self.textEdit_emp_local_address.setMaximumSize(QSize(200, 60))
        self.textEdit_emp_local_address.setStyleSheet(u"")
        self.label_emp_phone = QLabel(self.grb_phone_address)
        self.label_emp_phone.setObjectName(u"label_emp_phone")
        self.label_emp_phone.setGeometry(QRect(10, 88, 101, 20))
        self.label_emp_phone.setMaximumSize(QSize(150, 20))
        self.label_emp_mobile = QLabel(self.grb_phone_address)
        self.label_emp_mobile.setObjectName(u"label_emp_mobile")
        self.label_emp_mobile.setGeometry(QRect(310, 88, 101, 20))
        self.label_emp_mobile.setMaximumSize(QSize(150, 20))
        self.lineEdit_emp_phone = QLineEdit(self.grb_phone_address)
        self.lineEdit_emp_phone.setObjectName(u"lineEdit_emp_phone")
        self.lineEdit_emp_phone.setGeometry(QRect(119, 88, 165, 20))
        self.lineEdit_emp_phone.setMinimumSize(QSize(165, 0))
        self.lineEdit_emp_phone.setMaximumSize(QSize(165, 20))
        self.lineEdit_emp_mobile = QLineEdit(self.grb_phone_address)
        self.lineEdit_emp_mobile.setObjectName(u"lineEdit_emp_mobile")
        self.lineEdit_emp_mobile.setGeometry(QRect(419, 88, 165, 20))
        self.lineEdit_emp_mobile.setMinimumSize(QSize(165, 0))
        self.lineEdit_emp_mobile.setMaximumSize(QSize(165, 20))
        self.label_emp_company_email = QLabel(self.grb_phone_address)
        self.label_emp_company_email.setObjectName(u"label_emp_company_email")
        self.label_emp_company_email.setGeometry(QRect(10, 115, 101, 20))
        self.label_emp_company_email.setMaximumSize(QSize(150, 20))
        self.lineEdit_emp_company_email = QLineEdit(self.grb_phone_address)
        self.lineEdit_emp_company_email.setObjectName(u"lineEdit_emp_company_email")
        self.lineEdit_emp_company_email.setGeometry(QRect(119, 115, 260, 20))
        self.lineEdit_emp_company_email.setMinimumSize(QSize(260, 0))
        self.lineEdit_emp_company_email.setMaximumSize(QSize(260, 20))

        self.vly_frm_a_company.addWidget(self.grb_phone_address)

        self.grb_contact = QGroupBox(self.frm_a_company)
        self.grb_contact.setObjectName(u"grb_contact")
        self.grb_contact.setMinimumSize(QSize(0, 0))
        self.grb_contact.setStyleSheet(u"")
        self.label_emp_legal_representative = QLabel(self.grb_contact)
        self.label_emp_legal_representative.setObjectName(u"label_emp_legal_representative")
        self.label_emp_legal_representative.setGeometry(QRect(10, 20, 150, 20))
        self.label_emp_legal_representative.setMinimumSize(QSize(150, 20))
        self.label_emp_legal_representative.setMaximumSize(QSize(150, 20))
        self.lineEdit_emp_legal_representative = QLineEdit(self.grb_contact)
        self.lineEdit_emp_legal_representative.setObjectName(u"lineEdit_emp_legal_representative")
        self.lineEdit_emp_legal_representative.setGeometry(QRect(162, 20, 260, 20))
        self.lineEdit_emp_legal_representative.setMinimumSize(QSize(260, 0))
        self.lineEdit_emp_legal_representative.setMaximumSize(QSize(260, 20))
        self.lineEdit_emp_legal_representative.setStyleSheet(u"")
        self.label_emp_legal_representative_id = QLabel(self.grb_contact)
        self.label_emp_legal_representative_id.setObjectName(u"label_emp_legal_representative_id")
        self.label_emp_legal_representative_id.setGeometry(QRect(430, 20, 50, 20))
        self.label_emp_legal_representative_id.setMinimumSize(QSize(50, 0))
        self.label_emp_legal_representative_id.setMaximumSize(QSize(50, 20))
        self.lineEdit_emp_legal_representative_id = QLineEdit(self.grb_contact)
        self.lineEdit_emp_legal_representative_id.setObjectName(u"lineEdit_emp_legal_representative_id")
        self.lineEdit_emp_legal_representative_id.setGeometry(QRect(485, 20, 100, 20))
        self.lineEdit_emp_legal_representative_id.setMaximumSize(QSize(100, 20))
        self.lineEdit_emp_contact_phone = QLineEdit(self.grb_contact)
        self.lineEdit_emp_contact_phone.setObjectName(u"lineEdit_emp_contact_phone")
        self.lineEdit_emp_contact_phone.setGeometry(QRect(162, 50, 165, 20))
        self.lineEdit_emp_contact_phone.setMinimumSize(QSize(165, 0))
        self.lineEdit_emp_contact_phone.setMaximumSize(QSize(165, 20))
        self.label_emp_contact_phone = QLabel(self.grb_contact)
        self.label_emp_contact_phone.setObjectName(u"label_emp_contact_phone")
        self.label_emp_contact_phone.setGeometry(QRect(10, 50, 150, 20))
        self.label_emp_contact_phone.setMinimumSize(QSize(150, 0))
        self.label_emp_contact_phone.setMaximumSize(QSize(150, 20))
        self.lineEdit_emp_contact_email = QLineEdit(self.grb_contact)
        self.lineEdit_emp_contact_email.setObjectName(u"lineEdit_emp_contact_email")
        self.lineEdit_emp_contact_email.setGeometry(QRect(162, 80, 260, 20))
        self.lineEdit_emp_contact_email.setMinimumSize(QSize(260, 0))
        self.lineEdit_emp_contact_email.setMaximumSize(QSize(260, 20))
        self.label_emp_contact_email = QLabel(self.grb_contact)
        self.label_emp_contact_email.setObjectName(u"label_emp_contact_email")
        self.label_emp_contact_email.setGeometry(QRect(10, 80, 101, 20))
        self.label_emp_contact_email.setMaximumSize(QSize(150, 20))
        self.dateEdit_creation_date = QDateEdit(self.grb_contact)
        self.dateEdit_creation_date.setObjectName(u"dateEdit_creation_date")
        self.dateEdit_creation_date.setGeometry(QRect(512, 110, 100, 20))
        self.dateEdit_creation_date.setMaximumSize(QSize(100, 20))
        self.dateEdit_creation_date.setStyleSheet(u"")
        self.dateEdit_creation_date.setCalendarPopup(True)
        self.label_emp_creation_date = QLabel(self.grb_contact)
        self.label_emp_creation_date.setObjectName(u"label_emp_creation_date")
        self.label_emp_creation_date.setGeometry(QRect(391, 110, 120, 20))
        self.label_emp_creation_date.setMaximumSize(QSize(130, 20))

        self.vly_frm_a_company.addWidget(self.grb_contact)


        self.vly_frm_form_clients_2.addWidget(self.frm_a_company)

        self.frm_bar_a_company = QFrame(self.frm_form_a_company)
        self.frm_bar_a_company.setObjectName(u"frm_bar_a_company")
        sizePolicy.setHeightForWidth(self.frm_bar_a_company.sizePolicy().hasHeightForWidth())
        self.frm_bar_a_company.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.btn_add_a_company.sizePolicy().hasHeightForWidth())
        self.btn_add_a_company.setSizePolicy(sizePolicy)
        self.btn_add_a_company.setMinimumSize(QSize(118, 48))
        self.btn_add_a_company.setMaximumSize(QSize(118, 48))
        self.btn_add_a_company.setFont(font5)
        self.btn_add_a_company.setStyleSheet(u"")
        self.btn_add_a_company.setIcon(icon46)
        self.btn_add_a_company.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients_2.addWidget(self.btn_add_a_company)

        self.btn_save_a_company = QPushButton(self.frm_bar_a_company)
        self.btn_save_a_company.setObjectName(u"btn_save_a_company")
        self.btn_save_a_company.setMinimumSize(QSize(118, 48))
        self.btn_save_a_company.setMaximumSize(QSize(118, 48))
        self.btn_save_a_company.setFont(font5)
        self.btn_save_a_company.setStyleSheet(u"")
        self.btn_save_a_company.setIcon(icon47)
        self.btn_save_a_company.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients_2.addWidget(self.btn_save_a_company)

        self.btn_edit_a_company = QPushButton(self.frm_bar_a_company)
        self.btn_edit_a_company.setObjectName(u"btn_edit_a_company")
        sizePolicy.setHeightForWidth(self.btn_edit_a_company.sizePolicy().hasHeightForWidth())
        self.btn_edit_a_company.setSizePolicy(sizePolicy)
        self.btn_edit_a_company.setMinimumSize(QSize(118, 48))
        self.btn_edit_a_company.setMaximumSize(QSize(118, 48))
        self.btn_edit_a_company.setFont(font5)
        self.btn_edit_a_company.setStyleSheet(u"")
        self.btn_edit_a_company.setIcon(icon48)
        self.btn_edit_a_company.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients_2.addWidget(self.btn_edit_a_company)

        self.btn_cancel_a_company = QPushButton(self.frm_bar_a_company)
        self.btn_cancel_a_company.setObjectName(u"btn_cancel_a_company")
        self.btn_cancel_a_company.setMinimumSize(QSize(118, 48))
        self.btn_cancel_a_company.setMaximumSize(QSize(118, 48))
        self.btn_cancel_a_company.setFont(font5)
        self.btn_cancel_a_company.setStyleSheet(u"")
        self.btn_cancel_a_company.setIcon(icon49)
        self.btn_cancel_a_company.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients_2.addWidget(self.btn_cancel_a_company)

        self.btn_delete_a_company = QPushButton(self.frm_bar_a_company)
        self.btn_delete_a_company.setObjectName(u"btn_delete_a_company")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_delete_a_company.sizePolicy().hasHeightForWidth())
        self.btn_delete_a_company.setSizePolicy(sizePolicy6)
        self.btn_delete_a_company.setMinimumSize(QSize(118, 48))
        self.btn_delete_a_company.setMaximumSize(QSize(118, 48))
        self.btn_delete_a_company.setStyleSheet(u"")
        self.btn_delete_a_company.setIcon(icon50)
        self.btn_delete_a_company.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients_2.addWidget(self.btn_delete_a_company)


        self.vly_frm_form_clients_2.addWidget(self.frm_bar_a_company)


        self.hly_page_frm_aaa_company.addWidget(self.frm_form_a_company)

        self.qsw_forms.addWidget(self.page_frm_a_company)
        self.page_frm_zz_opcional = QWidget()
        self.page_frm_zz_opcional.setObjectName(u"page_frm_zz_opcional")
        self.page_frm_zz_opcional.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.page_frm_zz_opcional.sizePolicy().hasHeightForWidth())
        self.page_frm_zz_opcional.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.frm_form_zz_opcional.sizePolicy().hasHeightForWidth())
        self.frm_form_zz_opcional.setSizePolicy(sizePolicy1)
        self.frm_form_zz_opcional.setMinimumSize(QSize(625, 0))
        self.frm_form_zz_opcional.setMaximumSize(QSize(1920, 1080))
        self.frm_form_zz_opcional.setFont(font3)
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
        sizePolicy1.setHeightForWidth(self.page_frm_actions.sizePolicy().hasHeightForWidth())
        self.page_frm_actions.setSizePolicy(sizePolicy1)
        self.page_frm_actions.setMinimumSize(QSize(825, 544))
        self.page_frm_actions.setMaximumSize(QSize(1920, 1080))
        self.page_frm_actions.setStyleSheet(u"")
        self.hly_frm__actions = QHBoxLayout(self.page_frm_actions)
        self.hly_frm__actions.setSpacing(0)
        self.hly_frm__actions.setObjectName(u"hly_frm__actions")
        self.hly_frm__actions.setContentsMargins(0, 0, 0, 0)
        self.frm_form_action = QFrame(self.page_frm_actions)
        self.frm_form_action.setObjectName(u"frm_form_action")
        sizePolicy1.setHeightForWidth(self.frm_form_action.sizePolicy().hasHeightForWidth())
        self.frm_form_action.setSizePolicy(sizePolicy1)
        self.frm_form_action.setMinimumSize(QSize(625, 0))
        self.frm_form_action.setMaximumSize(QSize(1920, 1080))
        self.frm_form_action.setFont(font3)
        self.frm_form_action.setStyleSheet(u"")
        self.frm_form_action.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_form_action.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frm_form_action = QVBoxLayout(self.frm_form_action)
        self.vly_frm_form_action.setSpacing(3)
        self.vly_frm_form_action.setObjectName(u"vly_frm_form_action")
        self.vly_frm_form_action.setContentsMargins(4, 4, 4, 4)
        self.frm_actions = QFrame(self.frm_form_action)
        self.frm_actions.setObjectName(u"frm_actions")
        sizePolicy1.setHeightForWidth(self.frm_actions.sizePolicy().hasHeightForWidth())
        self.frm_actions.setSizePolicy(sizePolicy1)
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
"    \n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";  \n"
"    padding: 0px 5px;       \n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* C"
                        "olor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\"; \n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255); /* Color de realce de tu tema */\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
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
"    background-color: rgb(255"
                        ", 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco para el cuerpo */\n"
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
"    c"
                        "olor: #808080 !important;\n"
"    border: 2px solid #b0b0b0;\n"
"}")
        self.frm_actions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_actions.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_action = QVBoxLayout(self.frm_actions)
        self.vly_action.setSpacing(3)
        self.vly_action.setObjectName(u"vly_action")
        self.vly_action.setContentsMargins(4, 4, 4, 4)
        self.grp_actions = QGroupBox(self.frm_actions)
        self.grp_actions.setObjectName(u"grp_actions")
        self.grp_actions.setMinimumSize(QSize(0, 0))
        self.grp_actions.setMaximumSize(QSize(16777215, 544))
        self.grp_actions.setStyleSheet(u"")
        self.label_act_code = QLabel(self.grp_actions)
        self.label_act_code.setObjectName(u"label_act_code")
        self.label_act_code.setGeometry(QRect(10, 30, 61, 20))
        self.label_act_code.setMaximumSize(QSize(100, 20))
        self.label_act_code.setAutoFillBackground(False)
        self.lineEdit_act_code = QLineEdit(self.grp_actions)
        self.lineEdit_act_code.setObjectName(u"lineEdit_act_code")
        self.lineEdit_act_code.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_act_code.setMaximumSize(QSize(100, 20))
        self.label_act_description = QLabel(self.grp_actions)
        self.label_act_description.setObjectName(u"label_act_description")
        self.label_act_description.setGeometry(QRect(10, 60, 101, 20))
        self.label_act_description.setMaximumSize(QSize(150, 20))
        self.lineEdit_act_description = QLineEdit(self.grp_actions)
        self.lineEdit_act_description.setObjectName(u"lineEdit_act_description")
        self.lineEdit_act_description.setGeometry(QRect(120, 60, 400, 20))
        self.lineEdit_act_description.setMinimumSize(QSize(400, 20))
        self.lineEdit_act_description.setMaximumSize(QSize(400, 20))
        self.lineEdit_act_description.setStyleSheet(u"")
        self.label_act_id_category = QLabel(self.grp_actions)
        self.label_act_id_category.setObjectName(u"label_act_id_category")
        self.label_act_id_category.setGeometry(QRect(10, 90, 101, 20))
        self.label_act_id_category.setMinimumSize(QSize(101, 0))
        self.label_act_id_category.setMaximumSize(QSize(101, 20))
        self.label_act_status = QLabel(self.grp_actions)
        self.label_act_status.setObjectName(u"label_act_status")
        self.label_act_status.setGeometry(QRect(364, 30, 61, 20))
        self.label_act_status.setMaximumSize(QSize(100, 20))
        self.lineEdit_act_id_category = QLineEdit(self.grp_actions)
        self.lineEdit_act_id_category.setObjectName(u"lineEdit_act_id_category")
        self.lineEdit_act_id_category.setGeometry(QRect(120, 90, 400, 20))
        self.lineEdit_act_id_category.setMinimumSize(QSize(400, 20))
        self.lineEdit_act_id_category.setMaximumSize(QSize(400, 20))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setItalic(False)
        self.lineEdit_act_id_category.setFont(font8)
        self.lineEdit_act_id_category.setReadOnly(True)
        self.cmb_act_status = QComboBox(self.grp_actions)
        self.cmb_act_status.addItem("")
        self.cmb_act_status.addItem("")
        self.cmb_act_status.setObjectName(u"cmb_act_status")
        self.cmb_act_status.setGeometry(QRect(434, 30, 80, 20))
        sizePolicy1.setHeightForWidth(self.cmb_act_status.sizePolicy().hasHeightForWidth())
        self.cmb_act_status.setSizePolicy(sizePolicy1)
        self.cmb_act_status.setMinimumSize(QSize(80, 20))
        self.cmb_act_status.setMaximumSize(QSize(80, 20))
        self.cmb_act_status.setStyleSheet(u"")
        self.label_act_create_date = QLabel(self.grp_actions)
        self.label_act_create_date.setObjectName(u"label_act_create_date")
        self.label_act_create_date.setGeometry(QRect(10, 190, 130, 20))
        self.label_act_create_date.setMaximumSize(QSize(130, 20))
        self.dateEdit_act_create_date = QDateEdit(self.grp_actions)
        self.dateEdit_act_create_date.setObjectName(u"dateEdit_act_create_date")
        self.dateEdit_act_create_date.setGeometry(QRect(146, 190, 100, 20))
        self.dateEdit_act_create_date.setMaximumSize(QSize(100, 20))
        self.dateEdit_act_create_date.setStyleSheet(u"")
        self.dateEdit_act_create_date.setCalendarPopup(True)
        self.label_act_descriptiontec = QLabel(self.grp_actions)
        self.label_act_descriptiontec.setObjectName(u"label_act_descriptiontec")
        self.label_act_descriptiontec.setGeometry(QRect(10, 120, 100, 41))
        self.label_act_descriptiontec.setMinimumSize(QSize(100, 0))
        self.label_act_descriptiontec.setMaximumSize(QSize(100, 60))
        self.label_act_descriptiontec.setScaledContents(False)
        self.textEdit_act_descriptiontec = QTextEdit(self.grp_actions)
        self.textEdit_act_descriptiontec.setObjectName(u"textEdit_act_descriptiontec")
        self.textEdit_act_descriptiontec.setGeometry(QRect(120, 120, 400, 60))
        self.textEdit_act_descriptiontec.setMinimumSize(QSize(400, 60))
        self.textEdit_act_descriptiontec.setMaximumSize(QSize(400, 60))
        self.textEdit_act_descriptiontec.setStyleSheet(u"")
        self.btn_search_act_category = QPushButton(self.grp_actions)
        self.btn_search_act_category.setObjectName(u"btn_search_act_category")
        self.btn_search_act_category.setGeometry(QRect(528, 87, 24, 24))
        sizePolicy4.setHeightForWidth(self.btn_search_act_category.sizePolicy().hasHeightForWidth())
        self.btn_search_act_category.setSizePolicy(sizePolicy4)
        self.btn_search_act_category.setMinimumSize(QSize(24, 24))
        self.btn_search_act_category.setMaximumSize(QSize(24, 24))
        self.btn_search_act_category.setFont(font6)
        self.btn_search_act_category.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
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
        self.btn_search_act_category.setIcon(icon51)
        self.btn_search_act_category.setIconSize(QSize(18, 18))

        self.vly_action.addWidget(self.grp_actions)


        self.vly_frm_form_action.addWidget(self.frm_actions)

        self.frm_bar_action = QFrame(self.frm_form_action)
        self.frm_bar_action.setObjectName(u"frm_bar_action")
        sizePolicy1.setHeightForWidth(self.frm_bar_action.sizePolicy().hasHeightForWidth())
        self.frm_bar_action.setSizePolicy(sizePolicy1)
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
        self.btn_add_action.setFont(font5)
        self.btn_add_action.setStyleSheet(u"")
        self.btn_add_action.setIcon(icon46)
        self.btn_add_action.setIconSize(QSize(22, 22))

        self.hly_frm_bar_action.addWidget(self.btn_add_action)

        self.btn_save_action = QPushButton(self.frm_bar_action)
        self.btn_save_action.setObjectName(u"btn_save_action")
        self.btn_save_action.setMinimumSize(QSize(118, 48))
        self.btn_save_action.setMaximumSize(QSize(118, 48))
        self.btn_save_action.setFont(font5)
        self.btn_save_action.setStyleSheet(u"")
        self.btn_save_action.setIcon(icon47)
        self.btn_save_action.setIconSize(QSize(22, 22))

        self.hly_frm_bar_action.addWidget(self.btn_save_action)

        self.btn_edit_action = QPushButton(self.frm_bar_action)
        self.btn_edit_action.setObjectName(u"btn_edit_action")
        self.btn_edit_action.setMinimumSize(QSize(118, 48))
        self.btn_edit_action.setMaximumSize(QSize(118, 48))
        self.btn_edit_action.setFont(font5)
        self.btn_edit_action.setStyleSheet(u"")
        self.btn_edit_action.setIcon(icon48)
        self.btn_edit_action.setIconSize(QSize(22, 22))

        self.hly_frm_bar_action.addWidget(self.btn_edit_action)

        self.btn_cancel_action = QPushButton(self.frm_bar_action)
        self.btn_cancel_action.setObjectName(u"btn_cancel_action")
        self.btn_cancel_action.setMinimumSize(QSize(118, 48))
        self.btn_cancel_action.setMaximumSize(QSize(118, 48))
        self.btn_cancel_action.setFont(font5)
        self.btn_cancel_action.setStyleSheet(u"")
        self.btn_cancel_action.setIcon(icon49)
        self.btn_cancel_action.setIconSize(QSize(22, 22))

        self.hly_frm_bar_action.addWidget(self.btn_cancel_action)

        self.btn_delete_action = QPushButton(self.frm_bar_action)
        self.btn_delete_action.setObjectName(u"btn_delete_action")
        self.btn_delete_action.setMinimumSize(QSize(118, 48))
        self.btn_delete_action.setMaximumSize(QSize(118, 48))
        self.btn_delete_action.setStyleSheet(u"")
        self.btn_delete_action.setIcon(icon50)
        self.btn_delete_action.setIconSize(QSize(22, 22))

        self.hly_frm_bar_action.addWidget(self.btn_delete_action)


        self.vly_frm_form_action.addWidget(self.frm_bar_action)

        self.vly_frm_form_action.setStretch(0, 4)
        self.vly_frm_form_action.setStretch(1, 1)

        self.hly_frm__actions.addWidget(self.frm_form_action)

        self.qsw_forms.addWidget(self.page_frm_actions)
        self.page_frm_clients = QWidget()
        self.page_frm_clients.setObjectName(u"page_frm_clients")
        sizePolicy1.setHeightForWidth(self.page_frm_clients.sizePolicy().hasHeightForWidth())
        self.page_frm_clients.setSizePolicy(sizePolicy1)
        self.page_frm_clients.setMinimumSize(QSize(825, 544))
        self.page_frm_clients.setMaximumSize(QSize(1980, 1080))
        self.page_frm_clients.setStyleSheet(u"")
        self.hly_frm_clients = QHBoxLayout(self.page_frm_clients)
        self.hly_frm_clients.setSpacing(0)
        self.hly_frm_clients.setObjectName(u"hly_frm_clients")
        self.hly_frm_clients.setContentsMargins(0, 0, 0, 0)
        self.frm_form_clients = QFrame(self.page_frm_clients)
        self.frm_form_clients.setObjectName(u"frm_form_clients")
        sizePolicy1.setHeightForWidth(self.frm_form_clients.sizePolicy().hasHeightForWidth())
        self.frm_form_clients.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.frm_clients.sizePolicy().hasHeightForWidth())
        self.frm_clients.setSizePolicy(sizePolicy1)
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
"    font: 10pt \"Segoe UI\";                /* Fuente para QTextEdit */\n"
"    \n"
"}\n"
"\n"
"/* Estilo de QLineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";  \n"
"    padding: 0px 5px;       \n"
"}\n"
"\n"
"/* Estilo de QComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* C"
                        "olor del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\"; \n"
"    padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #000000;\n"
"    selection-background-color: rgb(85, 170, 255); /* Color de realce de tu tema */\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
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
"    background-color: rgb(255"
                        ", 255, 255); /* Color de fondo */\n"
"    color: #000000;                       /* Color del texto */\n"
"    border: 2px solid rgb(85, 170, 255); /* Borde */\n"
"    border-radius: 5px;                   /* Esquinas redondeadas */\n"
"    font: 10pt \"Segoe UI\";                /* Fuente para QDateEdit */\n"
"	padding-top: 0px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco para el cuerpo */\n"
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
"    c"
                        "olor: #808080 !important;\n"
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
        self.label_clt_code = QLabel(self.grb_frm_clients)
        self.label_clt_code.setObjectName(u"label_clt_code")
        self.label_clt_code.setGeometry(QRect(10, 30, 61, 20))
        self.label_clt_code.setMaximumSize(QSize(100, 20))
        self.label_clt_code.setAutoFillBackground(False)
        self.lineEdit_clt_code = QLineEdit(self.grb_frm_clients)
        self.lineEdit_clt_code.setObjectName(u"lineEdit_clt_code")
        self.lineEdit_clt_code.setGeometry(QRect(78, 30, 100, 20))
        self.lineEdit_clt_code.setMaximumSize(QSize(100, 20))
        self.label_clt_descripcion = QLabel(self.grb_frm_clients)
        self.label_clt_descripcion.setObjectName(u"label_clt_descripcion")
        self.label_clt_descripcion.setGeometry(QRect(10, 60, 101, 20))
        self.label_clt_descripcion.setMaximumSize(QSize(150, 20))
        self.lineEdit_clt_description = QLineEdit(self.grb_frm_clients)
        self.lineEdit_clt_description.setObjectName(u"lineEdit_clt_description")
        self.lineEdit_clt_description.setGeometry(QRect(120, 60, 400, 20))
        self.lineEdit_clt_description.setMinimumSize(QSize(400, 20))
        self.lineEdit_clt_description.setMaximumSize(QSize(400, 20))
        self.lineEdit_clt_description.setStyleSheet(u"")
        self.label_clt_idfiscaliscal = QLabel(self.grb_frm_clients)
        self.label_clt_idfiscaliscal.setObjectName(u"label_clt_idfiscaliscal")
        self.label_clt_idfiscaliscal.setGeometry(QRect(10, 90, 115, 20))
        self.label_clt_idfiscaliscal.setMinimumSize(QSize(115, 0))
        self.label_clt_idfiscaliscal.setMaximumSize(QSize(110, 20))
        self.label_clt_status = QLabel(self.grb_frm_clients)
        self.label_clt_status.setObjectName(u"label_clt_status")
        self.label_clt_status.setGeometry(QRect(238, 30, 61, 20))
        self.label_clt_status.setMaximumSize(QSize(100, 20))
        self.lineEdit_clt_idfiscal = QLineEdit(self.grb_frm_clients)
        self.lineEdit_clt_idfiscal.setObjectName(u"lineEdit_clt_idfiscal")
        self.lineEdit_clt_idfiscal.setGeometry(QRect(133, 90, 100, 20))
        self.lineEdit_clt_idfiscal.setMaximumSize(QSize(100, 20))
        self.cmb_clt_status = QComboBox(self.grb_frm_clients)
        self.cmb_clt_status.addItem("")
        self.cmb_clt_status.addItem("")
        self.cmb_clt_status.setObjectName(u"cmb_clt_status")
        self.cmb_clt_status.setGeometry(QRect(308, 30, 80, 20))
        sizePolicy1.setHeightForWidth(self.cmb_clt_status.sizePolicy().hasHeightForWidth())
        self.cmb_clt_status.setSizePolicy(sizePolicy1)
        self.cmb_clt_status.setMinimumSize(QSize(80, 20))
        self.cmb_clt_status.setMaximumSize(QSize(80, 20))
        self.cmb_clt_status.setStyleSheet(u"")
        self.cmb_clt_tipocontribuyente = QComboBox(self.grb_frm_clients)
        self.cmb_clt_tipocontribuyente.addItem("")
        self.cmb_clt_tipocontribuyente.addItem("")
        self.cmb_clt_tipocontribuyente.setObjectName(u"cmb_clt_tipocontribuyente")
        self.cmb_clt_tipocontribuyente.setGeometry(QRect(475, 90, 100, 20))
        sizePolicy1.setHeightForWidth(self.cmb_clt_tipocontribuyente.sizePolicy().hasHeightForWidth())
        self.cmb_clt_tipocontribuyente.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.cmb_clt_origen.sizePolicy().hasHeightForWidth())
        self.cmb_clt_origen.setSizePolicy(sizePolicy1)
        self.cmb_clt_origen.setMinimumSize(QSize(260, 20))
        self.cmb_clt_origen.setMaximumSize(QSize(260, 20))
        self.cmb_clt_origen.setStyleSheet(u"")

        self.vly_clients.addWidget(self.grb_sontactos_cliente)


        self.vly_frm_form_clients.addWidget(self.frm_clients)

        self.frm_bar_clients = QFrame(self.frm_form_clients)
        self.frm_bar_clients.setObjectName(u"frm_bar_clients")
        sizePolicy.setHeightForWidth(self.frm_bar_clients.sizePolicy().hasHeightForWidth())
        self.frm_bar_clients.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.btn_add_clients.sizePolicy().hasHeightForWidth())
        self.btn_add_clients.setSizePolicy(sizePolicy)
        self.btn_add_clients.setMinimumSize(QSize(118, 48))
        self.btn_add_clients.setMaximumSize(QSize(118, 48))
        self.btn_add_clients.setFont(font5)
        self.btn_add_clients.setStyleSheet(u"")
        self.btn_add_clients.setIcon(icon46)
        self.btn_add_clients.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients.addWidget(self.btn_add_clients)

        self.btn_save_clients = QPushButton(self.frm_bar_clients)
        self.btn_save_clients.setObjectName(u"btn_save_clients")
        self.btn_save_clients.setMinimumSize(QSize(118, 48))
        self.btn_save_clients.setMaximumSize(QSize(118, 48))
        self.btn_save_clients.setFont(font5)
        self.btn_save_clients.setStyleSheet(u"")
        self.btn_save_clients.setIcon(icon47)
        self.btn_save_clients.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients.addWidget(self.btn_save_clients)

        self.btn_edit_clients = QPushButton(self.frm_bar_clients)
        self.btn_edit_clients.setObjectName(u"btn_edit_clients")
        sizePolicy.setHeightForWidth(self.btn_edit_clients.sizePolicy().hasHeightForWidth())
        self.btn_edit_clients.setSizePolicy(sizePolicy)
        self.btn_edit_clients.setMinimumSize(QSize(118, 48))
        self.btn_edit_clients.setMaximumSize(QSize(118, 48))
        self.btn_edit_clients.setFont(font5)
        self.btn_edit_clients.setStyleSheet(u"")
        self.btn_edit_clients.setIcon(icon48)
        self.btn_edit_clients.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients.addWidget(self.btn_edit_clients)

        self.btn_cancel_clients = QPushButton(self.frm_bar_clients)
        self.btn_cancel_clients.setObjectName(u"btn_cancel_clients")
        self.btn_cancel_clients.setMinimumSize(QSize(118, 48))
        self.btn_cancel_clients.setMaximumSize(QSize(118, 48))
        self.btn_cancel_clients.setFont(font5)
        self.btn_cancel_clients.setStyleSheet(u"")
        self.btn_cancel_clients.setIcon(icon49)
        self.btn_cancel_clients.setIconSize(QSize(22, 22))

        self.hly_frm_bar_clients.addWidget(self.btn_cancel_clients)

        self.btn_delete_clients = QPushButton(self.frm_bar_clients)
        self.btn_delete_clients.setObjectName(u"btn_delete_clients")
        sizePolicy6.setHeightForWidth(self.btn_delete_clients.sizePolicy().hasHeightForWidth())
        self.btn_delete_clients.setSizePolicy(sizePolicy6)
        self.btn_delete_clients.setMinimumSize(QSize(118, 48))
        self.btn_delete_clients.setMaximumSize(QSize(118, 48))
        self.btn_delete_clients.setStyleSheet(u"")
        self.btn_delete_clients.setIcon(icon50)
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
        self.label_info_red.setPixmap(QPixmap(u":/icons/assets/icons/Red01.png"))
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
        self.label_info_so.setPixmap(QPixmap(u":/icons/assets/icons/OS02.svg"))
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
        self.label_info_regional.setPixmap(QPixmap(u":/icons/assets/icons/filesettings_102180.svg"))
        self.label_info_regional.setScaledContents(True)
        self.label_info_regional.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vly_page_inf_regional.addWidget(self.label_info_regional)

        self.sw_consolas.addWidget(self.page_inf_regional)

        self.vly_frame_consolas.addWidget(self.sw_consolas)


        self.horizontalLayout.addWidget(self.frame_consolas)


        self.verticalLayout_2.addWidget(self.frame_inferior)

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
        QWidget.setTabOrder(self.btn_menu, self.btn_info_sistema)
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
        QWidget.setTabOrder(self.btn_regresar_menu, self.btn_menu_ppal)
        QWidget.setTabOrder(self.btn_menu_ppal, self.textEdit_info_hw)
        QWidget.setTabOrder(self.textEdit_info_hw, self.btn_cambio_regional)
        QWidget.setTabOrder(self.btn_cambio_regional, self.btn_config_sql_tools)
        QWidget.setTabOrder(self.btn_config_sql_tools, self.btn_config_tools)
        QWidget.setTabOrder(self.btn_config_tools, self.textEdit_info_config)
        QWidget.setTabOrder(self.textEdit_info_config, self.textEdit_info_red)
        QWidget.setTabOrder(self.textEdit_info_red, self.textEdit_info_so)
        QWidget.setTabOrder(self.textEdit_info_so, self.textEdit_info_regional)

        self.retranslateUi(MainWindow)

        self.sw_consolas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"     Men\u00fa", None))
        self.btn_minimizar.setText("")
        self.btn_restaurar.setText("")
        self.btn_maximizar.setText("")
        self.btn_cerrar.setText("")
        self.btn_ark_reports03.setText(QCoreApplication.translate("MainWindow", u"      Clientes", None))
        self.btn_ark_reports02.setText(QCoreApplication.translate("MainWindow", u"    Categor\u00edas", None))
        self.btn_ark_reports06.setText(QCoreApplication.translate("MainWindow", u" Unidades", None))
        self.btn_ark_reports01.setText(QCoreApplication.translate("MainWindow", u"      Acciones", None))
        self.btn_ark_reports07.setText(QCoreApplication.translate("MainWindow", u"      Empleados", None))
        self.btn_ark_reports08.setText(QCoreApplication.translate("MainWindow", u"      Tipos", None))
        self.btn_ark_reports05.setText(QCoreApplication.translate("MainWindow", u"    Recursos", None))
        self.btn_ark_reports04.setText(QCoreApplication.translate("MainWindow", u"   Profesiones", None))
        self.btn_ark_reports09.setText(QCoreApplication.translate("MainWindow", u"   Solicitudes", None))
        self.btn_ark_reports10.setText(QCoreApplication.translate("MainWindow", u"   Sesiones", None))
        self.btn_ark_reports11.setText(QCoreApplication.translate("MainWindow", u"    Usuarios", None))
        self.btn_menu_repo_ppal.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa Principal", None))
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
        self.btn_ark_users.setText(QCoreApplication.translate("MainWindow", u"    Usuarios", None))
        self.btn_menu_arch_ppal.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa Principal", None))
        self.btn_archives_menu.setText(QCoreApplication.translate("MainWindow", u"      Archivos", None))
        self.btn_systems_menu.setText(QCoreApplication.translate("MainWindow", u"      Sistemas", None))
        self.btn_transactions_menu.setText(QCoreApplication.translate("MainWindow", u"  Operaciones", None))
        self.btn_reports_menu.setText(QCoreApplication.translate("MainWindow", u"      Reportes", None))
#if QT_CONFIG(shortcut)
        self.btn_reports_menu.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.zz_btn_Disponible_menu.setText(QCoreApplication.translate("MainWindow", u"      Disponible", None))
        self.btn_settings_menu.setText(QCoreApplication.translate("MainWindow", u"  Configuraci\u00f3n", None))
        self.btn_log_out.setText(QCoreApplication.translate("MainWindow", u"      Cerrar", None))
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
        self.btn_ark_requests.setText(QCoreApplication.translate("MainWindow", u"   Solicitudes", None))
        self.btn_ark_sessions.setText(QCoreApplication.translate("MainWindow", u"   Sesiones", None))
        self.btn_menu_ppal.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa Principal", None))
        self.btn_info_hardware.setText(QCoreApplication.translate("MainWindow", u"      Hardware", None))
        self.btn_info_red.setText(QCoreApplication.translate("MainWindow", u"      Red", None))
        self.btn_info_so.setText(QCoreApplication.translate("MainWindow", u"      Sistema", None))
        self.btn_info_regional.setText(QCoreApplication.translate("MainWindow", u"      Regional", None))
#if QT_CONFIG(shortcut)
        self.btn_info_regional.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_limpiar.setText(QCoreApplication.translate("MainWindow", u"      Limpiar", None))
        self.btn_menu_sys_ppal.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa Principal", None))
#if QT_CONFIG(shortcut)
        self.btn_menu_sys_ppal.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.title_arktoolspc.setText("")
#if QT_CONFIG(accessibility)
        self.label_logo_tools.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_logo_tools.setText("")
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
        self.btn_menu_cnf_ppal.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa Principal", None))
        self.label_info_config.setText("")
        self.grb_currencies.setTitle(QCoreApplication.translate("MainWindow", u"Monedas", None))
        self.cmb_mda_iso4217.setItemText(0, QCoreApplication.translate("MainWindow", u"VES", None))
        self.cmb_mda_iso4217.setItemText(1, QCoreApplication.translate("MainWindow", u"USD", None))
        self.cmb_mda_iso4217.setItemText(2, QCoreApplication.translate("MainWindow", u"EUR", None))

        self.label_mda_symbol.setText(QCoreApplication.translate("MainWindow", u"Simbolo Moneda:", None))
        self.label_mda_description.setText(QCoreApplication.translate("MainWindow", u"Denominaci\u00f3n:", None))
        self.label_mda_iso4217.setText(QCoreApplication.translate("MainWindow", u"ISO 4217:", None))
        self.label_mda_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
#if QT_CONFIG(accessibility)
        self.label_mda_code.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_mda_code.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.cmb_mda_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_mda_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.cmb_mda_symbol.setItemText(0, QCoreApplication.translate("MainWindow", u"Bs.", None))
        self.cmb_mda_symbol.setItemText(1, QCoreApplication.translate("MainWindow", u"$", None))
        self.cmb_mda_symbol.setItemText(2, QCoreApplication.translate("MainWindow", u"\u20ac", None))

        self.label_mda_operator.setText(QCoreApplication.translate("MainWindow", u"Operador:", None))
        self.cmb_mda_operator.setItemText(0, QCoreApplication.translate("MainWindow", u"Multiplicci\u00f3n", None))
        self.cmb_mda_operator.setItemText(1, QCoreApplication.translate("MainWindow", u"Divici\u00f3n", None))

        self.grb_mda_management.setTitle(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Factor", None))
        self.label_mda_update_date.setText(QCoreApplication.translate("MainWindow", u"Fecha Actualizaci\u00f3n:", None))
#if QT_CONFIG(accessibility)
        self.label_mda_passivefactor.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_mda_passivefactor.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Factor Pasivo:</p></body></html>", None))
#if QT_CONFIG(accessibility)
        self.label_mda_activefactor.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_mda_activefactor.setText(QCoreApplication.translate("MainWindow", u"Factor Activo:", None))
        self.label_mda_last_date.setText(QCoreApplication.translate("MainWindow", u"Ultima Actualizaci\u00f3n:", None))
        self.label_mda_creationdate.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
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
        self.label_emy_code.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_emy_code.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_emy_description.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n Social:", None))
        self.label_emy_idemployees.setText(QCoreApplication.translate("MainWindow", u"ID/C\u00e9dula:", None))
        self.label_emy_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_emy_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_emy_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.grb_address_phones_employees.setTitle(QCoreApplication.translate("MainWindow", u"Tel\u00e9fonos y Correo", None))
        self.label_emy_phone.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.label_emy_role.setText(QCoreApplication.translate("MainWindow", u"Rol:", None))
        self.label_emy_emailemployees.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.grb_contacts__employees.setTitle(QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.label_emy_client.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_emy_password.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_emy_position.setText(QCoreApplication.translate("MainWindow", u"Cargo:", None))
        self.label_emy_creationdate.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.btn_search_emy_client.setText("")
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
        self.label_dty_code.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_dty_code.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_dty_description.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_dty_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_dty_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_dty_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_dty_creationdate.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_dty_descripciontec.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n\n"
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
        self.label_cat_code.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_cat_code.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_cat_descripcion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Descripci\u00f3n:</p></body></html>", None))
        self.label_cat_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_cat_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_cat_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

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
        self.label_ita_code.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_ita_code.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_ita_description.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n Social:", None))
        self.label_ita_brand.setText(QCoreApplication.translate("MainWindow", u"Marca:", None))
        self.label_ita_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_ita_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_ita_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.cmb_ita_classification.setItemText(0, QCoreApplication.translate("MainWindow", u"Equipos de C\u00f3mputo Personal", None))
        self.cmb_ita_classification.setItemText(1, QCoreApplication.translate("MainWindow", u"Equipos de Servidor y Centro de Datos", None))
        self.cmb_ita_classification.setItemText(2, QCoreApplication.translate("MainWindow", u"Equipos Perif\u00e9ricos", None))
        self.cmb_ita_classification.setItemText(3, QCoreApplication.translate("MainWindow", u"Equipos de Red y Telecomunicaciones", None))
        self.cmb_ita_classification.setItemText(4, QCoreApplication.translate("MainWindow", u"Equipos M\u00f3viles", None))
        self.cmb_ita_classification.setItemText(5, QCoreApplication.translate("MainWindow", u"Equipos Audiovisuales", None))
        self.cmb_ita_classification.setItemText(6, QCoreApplication.translate("MainWindow", u"Equipos Especializados", None))
        self.cmb_ita_classification.setItemText(7, QCoreApplication.translate("MainWindow", u"Estaci\u00f3n de trabajo Administrativa", None))

        self.label_ita_classification.setText(QCoreApplication.translate("MainWindow", u"Clasificaci\u00f3n:", None))
        self.label_ita_fechavreacion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_ita_technical_description.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n\n"
"T\u00e9cnica:", None))
        self.label_ita_role.setText(QCoreApplication.translate("MainWindow", u"Rol:", None))
        self.label_ita_functional_units.setText(QCoreApplication.translate("MainWindow", u"Unidad Funcional:", None))
        self.label_ita_macadrees.setText(QCoreApplication.translate("MainWindow", u"MAC Adrees:", None))
        self.label_ita_ipadrees.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n IP:", None))
        self.label_ita_idRDP1.setText(QCoreApplication.translate("MainWindow", u"ID RDP 1:", None))
        self.label_ita_idRDP2.setText(QCoreApplication.translate("MainWindow", u"ID RDP 2:", None))
        self.label_ita_id_employees.setText(QCoreApplication.translate("MainWindow", u"Empleado Usuario:", None))
        self.label_ita_iprdp.setText(QCoreApplication.translate("MainWindow", u"IP RDP:", None))
        self.label_ita_technical_notes.setText(QCoreApplication.translate("MainWindow", u"Notas\n"
"T\u00e9cnicas:", None))
        self.btn_buscar_ita_functional_units.setText("")
        self.btn_search_ita_id_employees.setText("")
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
        self.label_usr_code.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_usr_code.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_usr_description.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_usr_phone.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.label_usr_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_usr_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_usr_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_usr_job_titles.setText(QCoreApplication.translate("MainWindow", u"Cargo:", None))
        self.label_usr_fechacreacion.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_usr_role.setText(QCoreApplication.translate("MainWindow", u"Rol:", None))
        self.label_usr_email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_usr_password_in.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_usr_password_rin.setText(QCoreApplication.translate("MainWindow", u"Re - Password:", None))
        self.btn_search_usr_job_titles.setText("")
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
        self.label_ses_number.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_ses_number.setText(QCoreApplication.translate("MainWindow", u"N\u00famero:", None))
        self.label_ses_clt_description.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n Social:", None))
        self.label_ses_clt_fiscal_id.setText(QCoreApplication.translate("MainWindow", u"ID Fiscal (RIF):", None))
        self.label_ses_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_ses_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Pendiente", None))
        self.cmb_ses_status.setItemText(1, QCoreApplication.translate("MainWindow", u"En Proceso", None))
        self.cmb_ses_status.setItemText(2, QCoreApplication.translate("MainWindow", u"Aplazada", None))
        self.cmb_ses_status.setItemText(3, QCoreApplication.translate("MainWindow", u"Terminada", None))

        self.label_ses__date_of_issue.setText(QCoreApplication.translate("MainWindow", u"Fecha de Emisi\u00f3n:", None))
        self.label_ses_direccionf.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n \n"
"Fiscal", None))
        self.label_ses_clt_phone.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.label_ses_clt_mobile.setText(QCoreApplication.translate("MainWindow", u"M\u00f3vil:", None))
        self.btn_search_ses_client.setText("")
        self.label_ses_clt_code.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
#if QT_CONFIG(accessibility)
        self.label_ses_employees_id.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_ses_employees_id.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.btn_search_ses_employees.setText("")
        self.grb_ark_sessions_details.setTitle(QCoreApplication.translate("MainWindow", u"Detalles de la sesi\u00f3n", None))
        self.label__ses_end_time.setText(QCoreApplication.translate("MainWindow", u"Fin:", None))
        self.label__ses_start_time.setText(QCoreApplication.translate("MainWindow", u"Hora Inicio:", None))
        self.label_ses_sessionsdate.setText(QCoreApplication.translate("MainWindow", u"Fecha de Sesi\u00f3n:", None))
        self.label_dts_activity_performed.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n \n"
"Actividad", None))
        self.label_ses_total_time.setText(QCoreApplication.translate("MainWindow", u"Tiempo Empleado:", None))
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
        self.label_req_code.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_req_code.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_req_description.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_req_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_req_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_req_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_req_creationdate.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_req_descriptiontec.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n\n"
"Detallada:", None))
#if QT_CONFIG(accessibility)
        self.label_req_client_id.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_req_client_id.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.btn_search_req_client.setText("")
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
        self.label_job_code.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_job_code.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_job_description.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_job_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_job_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_job_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_job_creationdate.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_job_descriptiontec.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n\n"
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
        self.label_fun_code.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_fun_code.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_fun_description.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n Social:", None))
        self.label_fun_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_fun_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_fun_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_fun_create_date.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_fun_descriptiontec.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n\n"
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
        self.grb_general_information.setTitle(QCoreApplication.translate("MainWindow", u"Datos Generales", None))
#if QT_CONFIG(accessibility)
        self.label_emp_codigo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_emp_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_emp_description.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n Social:", None))
        self.label_emp_tax_id.setText(QCoreApplication.translate("MainWindow", u"ID Fiscal (RIF):", None))
        self.label_emp_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_emp_ststus.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_emp_ststus.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.cmb_emp_tipo_taxpayer.setItemText(0, QCoreApplication.translate("MainWindow", u"Ordibario", None))
        self.cmb_emp_tipo_taxpayer.setItemText(1, QCoreApplication.translate("MainWindow", u"Especial", None))

        self.label_emp_tipo_taxpayer.setText(QCoreApplication.translate("MainWindow", u"Tipo Contribuyente:", None))
        self.grb_phone_address.setTitle(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n y Tel\u00e9fonos", None))
        self.label_emp_tax_address.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n \n"
"Fiscal", None))
        self.label_emp_local_address.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n \n"
"Local", None))
        self.label_emp_phone.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono Ppal:", None))
        self.label_emp_mobile.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono M\u00f3vil:", None))
        self.label_emp_company_email.setText(QCoreApplication.translate("MainWindow", u"Email Empresa:", None))
        self.grb_contact.setTitle(QCoreApplication.translate("MainWindow", u"Contactos", None))
        self.label_emp_legal_representative.setText(QCoreApplication.translate("MainWindow", u"Representante legal:", None))
        self.label_emp_legal_representative_id.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C\u00e9dula:</p></body></html>", None))
        self.label_emp_contact_phone.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono Contacto:", None))
        self.label_emp_contact_email.setText(QCoreApplication.translate("MainWindow", u"Email Contacto:", None))
        self.label_emp_creation_date.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
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
        self.grp_actions.setTitle(QCoreApplication.translate("MainWindow", u"Acciones", None))
#if QT_CONFIG(accessibility)
        self.label_act_code.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_act_code.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_act_description.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_act_id_category.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Categor\u00eda:</p></body></html>", None))
        self.label_act_status.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.cmb_act_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.cmb_act_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_act_create_date.setText(QCoreApplication.translate("MainWindow", u"Fecha de Creaci\u00f3n:", None))
        self.label_act_descriptiontec.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n\n"
"Detallada:", None))
        self.btn_search_act_category.setText("")
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
        self.label_clt_code.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_clt_code.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
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

