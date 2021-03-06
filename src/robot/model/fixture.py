#  Copyright 2008-2015 Nokia Networks
#  Copyright 2016-     Robot Framework Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

def create_fixture(fixture, parent, type):
    # TestCase and TestSuite have 'keyword_class', Keyword doesn't.
    keyword_class = getattr(parent, 'keyword_class', parent.__class__)
    if fixture is None:
        fixture = keyword_class(parent=parent, type=type)
    elif isinstance(fixture, keyword_class):
        fixture.parent = parent
        fixture.type = type
    else:
        raise TypeError("Only %s objects accepted, got %s."
                        % (keyword_class.__name__, fixture.__class__.__name__))
    return fixture
