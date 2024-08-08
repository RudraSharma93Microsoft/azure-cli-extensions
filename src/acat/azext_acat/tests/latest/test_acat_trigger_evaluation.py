# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import *
from azure.cli.testsdk.scenario_tests import AllowLargeResponse


class AcatQuickEvaluationScenario(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(AcatQuickEvaluationScenario, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'resources': '["/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/mcatsandbox/providers/microsoft.web/sites/mcatsandboxapp"]'
        })
        
    @AllowLargeResponse()
    def test_quick_evaluation(self):
        # acat quick-evaluation
        ret=self.cmd(
            'acat quick-evaluation --resource-ids {resources}')
        output=ret.get_output_in_json()
        print(output)
        assert(output['properties'] != None)
        assert(",".join(output['properties']['resourceIds']).lower() == ",".join(self.kwargs['resources'][2:-2].split('","')).lower())
        assert(len(output['properties']['quickAssessments']) >0)
        assert(output['properties']['triggerTime'] != None)
