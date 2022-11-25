# Copyright (C) 2014 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import importlib.machinery
import importlib.util
import os


def WrapperPath():
  return os.path.join(os.path.dirname(__file__), 'repo')


_wrapper_module = None


def Wrapper():
  global _wrapper_module
  if not _wrapper_module:
    modname = 'wrapper'
    loader = importlib.machinery.SourceFileLoader(modname, WrapperPath())
    spec = importlib.util.spec_from_loader(modname, loader)
    _wrapper_module = importlib.util.module_from_spec(spec)
    loader.exec_module(_wrapper_module)
  return _wrapper_module
