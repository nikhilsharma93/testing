# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm5.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from copy import deepcopy
from functools import partial

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1048, 1240)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255)"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.current_pipeline_list = []
        self.num_components_in_pipeline = 0

        self.mainGridLayout = QtGui.QGridLayout(self.centralwidget)
        self.mainGridLayout.setObjectName(_fromUtf8("mainGridLayout"))
        scroll_bar_style_sheet = """
        QScrollBar:horizontal {
            border: none;
            background: none;
            height: 26px;
            margin: 0px 26px 0 26px;
        }

        QScrollBar::handle:horizontal {
            background: lightgray;
            min-width: 26px;
        }

        QScrollBar::add-line:horizontal {
            background: none;
            width: 26px;
            subcontrol-position: right;
            subcontrol-origin: margin;

        }

        QScrollBar::sub-line:horizontal {
            background: none;
            width: 26px;
            subcontrol-position: top left;
            subcontrol-origin: margin;
            position: absolute;
        }

        QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
            width: 26px;
            height: 26px;
            background: none;
            image: url('./glass.png');
        }

        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background: none;
        }

        /* VERTICAL */
        QScrollBar:vertical {
            border: none;
            background: none;
            width: 12px;
            margin: 26px 0 26px 0;
        }

        QScrollBar::handle:vertical {
            background: none;
            image: url('./images/scrollbar1.png');
            min-height: 26px;
        }

        QScrollBar::add-line:vertical {
            background: none;
            height: 26px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }

        QScrollBar::sub-line:vertical {
            background: none;
            height: 26px;
            subcontrol-position: top left;
            subcontrol-origin: margin;
            position: absolute;
        }

        QScrollBar::down-arrow:vertical {
            width: 26px;
            height: 26px;
            background: none;
            image: url('./images/arrowdown.png');
        }

        QScrollBar::up-arrow:vertical {
            width: 26px;
            height: 26px;
            background: none;
            image: url('./images/arrowup.png');
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }

        """
        self.existing_components_display_scroll = QtGui.QScrollArea(self.centralwidget)
        self.existing_components_display_scroll.setStyle(QtGui.QStyleFactory.create('Windows'))
        scroll_bar = QtGui.QScrollBar()
        scroll_bar.setStyleSheet(scroll_bar_style_sheet)
        #import pdb; pdb.set_trace()
        self.existing_components_display_scroll.setMaximumSize(QtCore.QSize(300, 16777215))
        self.existing_components_display_scroll.setStyleSheet(_fromUtf8("background-color: rgb(239, 245, 255)"))
        self.existing_components_display_scroll.setVerticalScrollBar(scroll_bar)
        self.existing_components_display_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.existing_components_display_scroll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.existing_components_display_scroll.setWidgetResizable(True)
        self.existing_components_display_scroll.setObjectName(_fromUtf8("existing_components_display_scroll"))
        self.existing_components_display_contents = QtGui.QWidget()
        self.existing_components_display_contents.setGeometry(QtCore.QRect(0, 0, 285, 890))
        self.existing_components_display_contents.setObjectName(_fromUtf8("existing_components_display_contents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.existing_components_display_contents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout.setSpacing(100)

        # Initialize existing components display
        self.existing_component_setup()

        self.existing_components_display_scroll.setWidget(self.existing_components_display_contents)
        self.mainGridLayout.addWidget(self.existing_components_display_scroll, 1, 0, 1, 1)
        self.label_existing_components_name = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FontAwesome"))
        font.setPointSize(6)
        self.label_existing_components_name.setFont(font)
        self.label_existing_components_name.setObjectName(_fromUtf8("label_existing_components_name"))
        self.mainGridLayout.addWidget(self.label_existing_components_name, 0, 0, 1, 1)
        scroll_bar_copy = QtGui.QScrollBar()
        scroll_bar_copy.setStyleSheet(scroll_bar_style_sheet)

        # Setup right vertical manager
        self.verticalLayoutWidget_pipelines = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_pipelines.setGeometry(QtCore.QRect(0, 0, 900, 890))
        self.verticalLayoutWidget_pipelines.setObjectName(_fromUtf8("verticalLayoutWidget_pipelines"))
        self.verticalLayout_pipelines = QtGui.QVBoxLayout(self.verticalLayoutWidget_pipelines)
        self.verticalLayout_pipelines.setObjectName(_fromUtf8("verticalLayout_pipelines"))
        self.verticalLayoutWidget_pipelines.setStyleSheet(_fromUtf8("background-color: rgb(241, 241, 241);"))
        self.pipeline_display_tabs = QtGui.QTabWidget(self.verticalLayoutWidget_pipelines)



        self.pipeline_display_tabs.setTabShape(QtGui.QTabWidget.Rounded)
        self.pipeline_display_tabs.setObjectName(_fromUtf8("pipeline_display_tabs"))
        self.Graph = QtGui.QWidget()
        self.Graph.setObjectName(_fromUtf8("Graph"))
        graph_tab_icon = QtGui.QIcon()
        graph_tab_icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/flowchart1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Source = QtGui.QWidget()
        self.Source.setObjectName(_fromUtf8("Source"))
        source_tab_icon = QtGui.QIcon()
        source_tab_icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/code1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pipeline_display_scroll = QtGui.QScrollArea(self.Graph)
        self.pipeline_display_scroll.setGeometry(QtCore.QRect(0, 0, 900, 890))
        # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        # self.pipeline_display_scroll.setSizePolicy(sizePolicy)
        #self.pipeline_display_scroll.setMaximumSize(QtCore.QSize(300, 16777215))
        # self.pipeline_display_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.pipeline_display_scroll.setVerticalScrollBar(scroll_bar_copy)
        self.pipeline_display_scroll.setStyleSheet(_fromUtf8("background-color: rgb(241, 241, 241);"))
        self.pipeline_display_scroll.setWidgetResizable(True)
        self.pipeline_display_scroll.setObjectName(_fromUtf8("pipeline_display_scroll"))
        self.pipeline_display_contents = QtGui.QWidget()
        #self.pipeline_display_contents.setGeometry(QtCore.QRect(0, 200, 722, 890))
        self.pipeline_display_contents.setObjectName(_fromUtf8("pipeline_display_contents"))
        self.verticalLayout_pipelines_graph =  QtGui.QGridLayout(self.pipeline_display_contents)
        self.verticalLayout_pipelines_graph.setSpacing(0)
        self.verticalLayout_pipelines_graph.setContentsMargins(0, 0, 0, 0)
        intial_pipelines_graph_spacerItem = QtGui.QSpacerItem(1, 50, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_pipelines_graph.addItem(intial_pipelines_graph_spacerItem, 0, 0, 1, 1)
        #self.verticalLayout_pipelines_graph.addHorizontalStretch(1)
        #self.verticalLayout_pipelines_graph.addVerticalStretch(1)

        """
        spacerItem1a = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        spacerItem1b = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_pipelines_graph.addItem(spacerItem1a, 0, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.pipeline_display_contents)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_pipelines_graph.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.verticalLayout_pipelines_graph.addItem(spacerItem1b, 0, 2, 1, 1)

        spacerItem2a = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        spacerItem2b = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_pipelines_graph.addItem(spacerItem2a, 1, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.pipeline_display_contents)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_pipelines_graph.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.verticalLayout_pipelines_graph.addItem(spacerItem2b, 1, 2, 1, 1)
        self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))

        spacerItem3a = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_pipelines_graph.addItem(spacerItem3a, 2, 0, 1, 1)
        """


        self.pipeline_display_tabs.addTab(self.Graph, graph_tab_icon, _fromUtf8(""))
        self.pipeline_display_tabs.addTab(self.Source, source_tab_icon, _fromUtf8(""))
        self.pipeline_display_tabs.tabBar().setTabTextColor(0, QtGui.QColor(0, 0, 255))
        self.verticalLayout_pipelines.addWidget(self.pipeline_display_tabs)
        self.pipeline_display_scroll.setWidget(self.pipeline_display_contents)

        self.mainGridLayout.addWidget(self.verticalLayoutWidget_pipelines, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuComponent = QtGui.QMenu(self.menubar)
        self.menuComponent.setObjectName(_fromUtf8("menuComponent"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.icon_bar = QtGui.QToolBar(MainWindow)
        self.icon_bar.setObjectName(_fromUtf8("icon_bar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.icon_bar)
        self.action_new_file = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/folder_new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new_file.setIcon(icon)
        self.action_new_file.setObjectName(_fromUtf8("action_new_file"))
        self.action_open_file = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/Custom-Icon-Design-Pretty-Office-9-Open-file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open_file.setIcon(icon1)
        self.action_open_file.setObjectName(_fromUtf8("action_open_file"))
        self.action_exit_file = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exit_file.setIcon(icon2)
        self.action_exit_file.setObjectName(_fromUtf8("action_exit_file"))
        self.action_new_component = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/063.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new_component.setIcon(icon3)
        self.action_new_component.setObjectName(_fromUtf8("action_new_component"))
        self.action_delete_component = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("images/trash-circle-red-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_delete_component.setIcon(icon4)
        self.action_delete_component.setObjectName(_fromUtf8("action_delete_component"))
        self.action_run_pipeline = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("images/play_green.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_run_pipeline.setIcon(icon5)
        self.action_run_pipeline.setObjectName(_fromUtf8("action_run_pipeline"))
        self.action_deployer_help = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("images/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_deployer_help.setIcon(icon6)
        self.action_deployer_help.setObjectName(_fromUtf8("action_deployer_help"))
        self.action_about_deployer = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("images/information.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about_deployer.setIcon(icon7)
        self.action_about_deployer.setObjectName(_fromUtf8("action_about_deployer"))
        self.menuFile.addAction(self.action_new_file)
        self.menuFile.addAction(self.action_open_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_exit_file)
        self.menuEdit.addAction(self.action_run_pipeline)
        self.menuComponent.addAction(self.action_new_component)
        self.menuComponent.addAction(self.action_delete_component)
        self.menuHelp.addAction(self.action_deployer_help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.action_about_deployer)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuComponent.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.icon_bar.addAction(self.action_new_file)
        self.icon_bar.addAction(self.action_open_file)
        self.icon_bar.addAction(self.action_exit_file)
        self.icon_bar.addSeparator()
        self.icon_bar.addAction(self.action_new_component)
        self.icon_bar.addAction(self.action_delete_component)
        self.icon_bar.addSeparator()
        self.icon_bar.addAction(self.action_run_pipeline)
        self.icon_bar.addSeparator()
        self.icon_bar.addAction(self.action_deployer_help)
        self.icon_bar.addAction(self.action_about_deployer)

        """
        self.pipelineDisplayLayoutWidget = QtGui.QWidget(self.Graph)
        self.pipelineDisplayLayoutWidget.setGeometry(QtCore.QRect(200, 0, 400+250, 711))
        self.pipelineDisplayLayoutWidget.setObjectName(_fromUtf8("pipelineDisplayLayoutWidget"))
        self.pipelineDisplayLayout = QtGui.QVBoxLayout(self.pipelineDisplayLayoutWidget)
        self.pipelineDisplayLayout.setObjectName(_fromUtf8("pipelineDisplayLayout"))
        """
        #self.pipelineDisplayLayout.setSpacing(0)
        #self.pipelineDisplayLayout.setContentsMargins(0, 0, 0, 0)
        #self.pipelineDisplayLayout.addStretch(1)

        """
        new_pipeline_comp = QtGui.QLabel(self.pipeline_display_contents)
        new_pipeline_comp.setAlignment(QtCore.Qt.AlignCenter)
        new_pipeline_comp.setStyleSheet(_fromUtf8("QLabel {border-image: url(images/bbox.png) 0 0 0 0 stretch stretch;}"))
        new_pipeline_comp.setMinimumSize(QtCore.QSize(300, 125))
        new_pipeline_comp.setMaximumSize(QtCore.QSize(300, 125))
        font = QtGui.QFont()
        font.setPointSize(20)
        new_pipeline_comp.setFont(font)
        new_pipeline_comp.setObjectName(_fromUtf8("label"))
        self.verticalLayout_pipelines_graph.addWidget(new_pipeline_comp, QtCore.Qt.AlignHCenter)
        new_pipeline_comp.setText(_translate("MainWindow", 'haha', None))
        """

        """
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(610, 590, 3, 61))
        self.line.setStyleSheet(_fromUtf8("background-color: rgb(85, 0, 255);"))
        self.line.setLineWidth(10)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        """

        self.action_new_file_1 = QtGui.QAction(MainWindow)
        icon_1 = QtGui.QIcon()
        icon_1.addPixmap((QtGui.QPixmap(_fromUtf8("images/logo.png")).scaled(QtCore.QSize(25, 25))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new_file_1.setIcon(icon_1)
        #self.action_new_file_1.setIconSize(QtGui.QSize(15, 15))
        self.action_new_file_1.setObjectName(_fromUtf8("action_new_file_1"))
        self.icon_bar_1 = QtGui.QToolBar(MainWindow)
        self.icon_bar_1.setObjectName(_fromUtf8("icon_bar_1"))
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.icon_bar_1)
        self.icon_bar_1.addAction(self.action_new_file_1)

        self.pipeline_display_tabs.currentChanged.connect(self.tab_change)

        # Create right click menus
        self.component_rclick_menu = QtGui.QMenu(MainWindow)
        self.component_rclick_menu.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.component_rclick_menu.setObjectName(_fromUtf8("component_rclick_menu"))
        # Create Actions and add
        self.rclick_add_component_to_pipeline = QtGui.QAction(MainWindow)
        self.rclick_show_source_pipeline = QtGui.QAction(MainWindow)
        self.component_rclick_menu.addAction(self.rclick_add_component_to_pipeline)
        self.component_rclick_menu.addSeparator()
        self.component_rclick_menu.addAction(self.rclick_show_source_pipeline)
        # Create signal slot connection
        self.rclick_add_component_to_pipeline.activated.connect(self.rclick_add_component_to_pipeline_callback)
        #self.rclick_show_source_pipeline.activated.connect(self.rclick_show_source_pipeline_callback)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def rclick_add_component_to_pipeline_callback(self):
        # Get component name and draw box
        component_to_draw = self.current_pipeline_list[self.current_existing_component_idx]
        print('component_to_draw:')
        for temploop in range(5):
            if self.num_components_in_pipeline > 0:
                self.verticalLayout_pipelines_graph.removeItem(spacerItem1c)
                spacerItem1a_arrow = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
                spacerItem1b_arrow = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
                arrow_pipeline = QtGui.QLabel(self.pipeline_display_contents)
                arrow_pipeline.setStyleSheet(_fromUtf8("QLabel {border-image: url(images/arrow1.png) 0 0 0 0 stretch stretch;}"))
                #new_pipeline_comp.setStyleSheet("background-color: rgb(0, 255, 0); margin:0; padding:0; border:0;")
                arrow_pipeline.setMinimumSize(QtCore.QSize(300, 125))
                arrow_pipeline.setMaximumSize(QtCore.QSize(300, 125))
                self.verticalLayout_pipelines_graph.addItem(spacerItem1a_arrow, 2*temploop, 0, 1, 1)
                self.verticalLayout_pipelines_graph.addWidget(arrow_pipeline, 2*temploop, 1, 1, 1)
                self.verticalLayout_pipelines_graph.addItem(spacerItem1b_arrow, 2*temploop, 2, 1, 1)

            #if temploop > 0:
            #    self.verticalLayout_pipelines_graph.removeItem(spacerItem1c)
            spacerItem1a = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            spacerItem1b = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            spacerItem1c = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
            new_pipeline_comp = QtGui.QLabel(str(temploop) + component_to_draw['name'], self.pipeline_display_contents)
            new_pipeline_comp.setStyleSheet(_fromUtf8("QLabel {border-image: url(images/bbox.png) 0 0 0 0 stretch stretch;}"))
            new_pipeline_comp.setMinimumSize(QtCore.QSize(300, 125))
            new_pipeline_comp.setMaximumSize(QtCore.QSize(300, 125))
            font = QtGui.QFont()
            font.setPointSize(20)
            new_pipeline_comp.setFont(font)
            new_pipeline_comp.setAlignment(QtCore.Qt.AlignCenter)
            new_pipeline_comp.setObjectName(_fromUtf8("pushButton_3"))
            self.verticalLayout_pipelines_graph.addItem(spacerItem1a, 2*temploop+1, 0, 1, 1)
            self.verticalLayout_pipelines_graph.addWidget(new_pipeline_comp, 2*temploop+1, 1, 1, 1)
            self.verticalLayout_pipelines_graph.addItem(spacerItem1b, 2*temploop+1, 2, 1, 1)
            self.verticalLayout_pipelines_graph.addItem(spacerItem1c, 2*temploop+2, 0, 1, 1)

            self.num_components_in_pipeline += 1
        #self.verticalLayout_pipelines_graph.addItem(spacerItem1c, temploop+1, 0, 1, 1)


    def tab_change(self, i):
        if i == 1:
            self.pipeline_display_tabs.tabBar().setTabTextColor(1, QtGui.QColor(0, 0, 255))
            self.pipeline_display_tabs.tabBar().setTabTextColor(0, QtGui.QColor(0, 0, 0))
        else:
            self.pipeline_display_tabs.tabBar().setTabTextColor(0, QtGui.QColor(0, 0, 255))
            self.pipeline_display_tabs.tabBar().setTabTextColor(1, QtGui.QColor(0, 0, 0))


    def existing_component_setup(self):
        existing_component_font = QtGui.QFont()
        existing_component_font.setFamily(_fromUtf8("Nimbus Mono L"))
        existing_component_font.setPointSize(20)
        existing_component_font.setBold(True)
        existing_component_font.setWeight(75)

        for i in range(20):
            pushButton = QtGui.QPushButton(self.existing_components_display_contents)
            pushButton.setMinimumSize(QtCore.QSize(250, 150))
            pushButton.setMaximumSize(QtCore.QSize(250, 150))
            pushButton.setFont(existing_component_font)
            pushButton.setStyleSheet(_fromUtf8("border-image: url(images/Silver_button.png) 0 0 0 0 stretch stretch"))
            pushButton.setObjectName(_fromUtf8("pushButton"))
            current_name = "Preprocessing" + str(i)
            pushButton.setText(_translate("MainWindow", current_name, None))
            current_dict = {'path': i}
            pushButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            rclick_wrapper = partial(self.existing_component_rclick_menu, pushButton=pushButton, i=i, current_dict=current_dict)
            pushButton.customContextMenuRequested.connect(rclick_wrapper)
            self.current_pipeline_list.append(deepcopy(dict(name=current_name, dict=current_dict)))
            self.verticalLayout.addWidget(pushButton)

    def existing_component_rclick_menu(self, point, pushButton, i, current_dict):
        self.current_existing_component_idx = i
        self.component_rclick_menu.exec_(pushButton.mapToGlobal(point))


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_existing_components_name.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"left\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Existing Components</span></p></body></html>", None))
        self.pipeline_display_tabs.setTabText(self.pipeline_display_tabs.indexOf(self.Graph), _translate("MainWindow", "Graph", None))
        self.pipeline_display_tabs.setTabText(self.pipeline_display_tabs.indexOf(self.Source), _translate("MainWindow", "Source", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuComponent.setTitle(_translate("MainWindow", "Component", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.icon_bar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.action_new_file.setText(_translate("MainWindow", "New", None))
        self.action_open_file.setText(_translate("MainWindow", "Open", None))
        self.action_exit_file.setText(_translate("MainWindow", "Exit", None))
        self.action_new_component.setText(_translate("MainWindow", "New", None))
        self.action_delete_component.setText(_translate("MainWindow", "Delete", None))
        self.action_run_pipeline.setText(_translate("MainWindow", "Run Pipeline", None))
        self.action_deployer_help.setText(_translate("MainWindow", "Deployer Help", None))
        self.action_about_deployer.setText(_translate("MainWindow", "About Deployer", None))
        self.component_rclick_menu.setTitle(_translate("MainWindow", "RClick", None))
        self.rclick_add_component_to_pipeline.setText(_translate("MainWindow", "Add to pipeline", None))
        self.rclick_show_source_pipeline.setText(_translate("MainWindow", "Show source code", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow_op1 = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow_op1)
    MainWindow_op1.show()
    sys.exit(app.exec_())
