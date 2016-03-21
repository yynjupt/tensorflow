# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Switch between depending on googletest or unittest."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# pylint: disable=g-import-not-at-top
# pylint: disable=wildcard-import
from . import control_imports
from tensorflow.python.platform import benchmark

# Import the Benchmark class
Benchmark = benchmark.Benchmark  # pylint: disable=invalid-name

if control_imports.USE_OSS and control_imports.OSS_GOOGLETEST:
  from tensorflow.python.platform.default._googletest import *
  from tensorflow.python.platform.default._googletest import main as g_main
else:
  from tensorflow.python.platform.google._googletest import *
  from tensorflow.python.platform.google._googletest import main as g_main


# Redefine main to allow running benchmarks
def main():
  # Benchmarks determine whether to run tests or not, by calling g_main
  benchmark.benchmarks_main(true_main=g_main)
