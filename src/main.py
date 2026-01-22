import re
from pathlib import Path
from typing import Any, Dict, Optional, Union

from openad_service_utils import (
    DomainSubmodule,
    FileResponse,
    PredictorTypes,
    SimplePredictor,
    PropertyInfo
)
from pydantic.v1 import Field
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class DemoMeshPredictor(SimplePredictor):
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
        logger.info("\nSetting up DemoMeshPredictor...")

    def predict(
        self,
        input: str,
        output_dir: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[FileResponse, Dict[str, Any]]:
        if not output_dir:
            raise ValueError("output_dir must be provided")

        input_path = Path(input)  # input for Mesh type is a filepath
        logger.info(f"\nRunning prediction in DemoMeshPredictor for input: { input_path.absolute().as_posix()}")
        logger.info(f"Test parameter test_x: {self.test_x}")


        # save input file to output directory as a dummy "prediction"
        output_path = Path(output_dir)
        output_filename = f"predicted_{input_path.name}"
        output_file_path = output_path / output_filename
        with open(input_path, "rb") as src_file:
            with open(output_file_path, "wb") as dst_file:
                dst_file.write(src_file.read())
                logger.info(f"Saved predicted mesh to: {output_file_path.absolute().as_posix()}")

        return FileResponse(file_path=output_filename)


# register the predictor
DemoMeshPredictor.register(no_model=True)

if __name__ == "__main__":
    from openad_service_utils import start_server
    start_server(port=8080)
