from pathlib import Path
from typing import Any, Dict, Optional, Union

from openad_service_utils import (
    DomainSubmodule,
    FileResponse,
    PredictorTypes,
    SimplePredictor,
)
from pydantic.v1 import Field


class TestMeshPredictor(SimplePredictor):
    """
    test mesh predictor
    """

    domain: DomainSubmodule = DomainSubmodule("meshes")
    algorithm_name: str = "Transolver"
    algorithm_application: str = "test"
    algorithm_version: str = "v1"
    property_type: PredictorTypes = PredictorTypes.MESH
    
    # exposed api override parameters
    test_x: Optional[float] = Field(0.0, description="A test float parameter")

    def setup(self):
        print("\nSetting up TestMeshPredictor...")

    def predict(
        self,
        input: str,
        output_dir: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[FileResponse, Dict[str, Any]]:
        if not output_dir:
            raise ValueError("output_dir must be provided")

        input_path = Path(input)  # input for Mesh type is a filepath
        print("\nRunning prediction in TestMeshPredictor for input:", input_path.name)
        print("File input path", input_path.absolute().as_posix())
        print("Test parameter test_x:", self.test_x)

        return FileResponse(file_path=input_path.absolute().as_posix())


# register the predictor
TestMeshPredictor.register(no_model=True)

if __name__ == "__main__":
    from openad_service_utils import start_server
    start_server()
