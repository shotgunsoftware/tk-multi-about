#!/usr/bin/env bash
#
# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

# The path to output all built .py files to:
UI_PYTHON_PATH=../python/tk_multi_about/ui
PYTHON_BASE="/Applications/Shotgun.app/Contents/Resources/Python"


# Helper functions to build UI files
function build_qt {
    echo " > Building " $2

    # compile ui to python
    $1 $2 > $UI_PYTHON_PATH/$3.py

    # replace PySide imports with tank.platform.qt and remove line containing Created by date
    sed -i $UI_PYTHON_PATH/$3.py -e "s/from PySide import/from tank.platform.qt import/g" -e "/# Created:/d"
}

function build_ui {
    build_qt "${PYTHON_BASE}/bin/python ${PYTHON_BASE}/bin/pyside-uic --from-imports" "$1.ui" "../ui/$1"
}

function build_res {
	# Include the "-py3" flag so that we add the `b` prefix to strings for
	# PySide2 / Python3 compatibility.  This means these files will no longer
	# be compatible with Python 2.5 and below, but the `b` prefix is ignored in
	# Python 2.6+.
    build_qt "${PYTHON_BASE}/bin/pyside-rcc -py3" "$1.qrc" "../ui/$1_rc"
}


# build UI's:
echo "building user interfaces..."
build_ui dialog

# build resources
echo "building resources..."
build_res resources
