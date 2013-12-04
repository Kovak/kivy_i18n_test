#!/bin/bash

VERSION_flufl=1.0
URL_flufl=
DEPS_flufl=(python)
MD5_flufl=
BUILD_flufl=$BUILD_PATH/flufl
RECIPE_flufl=$RECIPES_PATH/flufl

function prebuild_flufl() {
	true
}

function build_flufl() {
	cd $BUILD_flufl

	push_arm
	try $BUILD_hostpython/hostpython setup.py install -O2 --root=$BUILD_PATH/python-install --install-lib=lib/python2.7/site-packages
	pop_arm
}

function postbuild_flufl() {
	true
}
